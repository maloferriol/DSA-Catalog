# Debug: DSA Catalog.app launches briefly then dies

Open Claude Code with this folder as the working directory:

```
cd "/Users/user/Documents/Claude/Projects/Data Structure & Algorithm"
claude
```

Then paste everything below the `---`.

---

# Debug: my macOS .app dies on launch

## Context

Working directory: `/Users/user/Documents/Claude/Projects/Data Structure & Algorithm/`. It contains:

- `DSA Catalog.app` — a hand-built macOS `.app` bundle (unsigned, not from the App Store)
- `serve.py` — a stdlib-only Python HTTP server the .app's launcher runs
- `start.command` — a bash launcher that does the same thing from Terminal
- `DSA_Reference_Catalog.html` — the page `serve.py` serves
- `progress.json` — user data; do NOT modify

The .app's internal structure:

```
DSA Catalog.app/
  Contents/
    Info.plist
    MacOS/launcher          ← bash script, the .app's executable
    Resources/icon.icns
```

The launcher (recently updated) explicitly searches Homebrew + python.org install paths, augments `$PATH`, and logs every step to `~/Library/Logs/DSA-Catalog.log`.

## Symptom

I double-click `DSA Catalog.app`. The icon flashes in the Dock for a fraction of a second, then disappears. No window, no dialog, no popup. Browser does not open.

## Your task

Diagnose the cause, apply the minimal fix, confirm it works. Don't apply random fixes — work through the steps in order and tell me what each one reveals.

### Step 1 — Read the launch log

```bash
cat ~/Library/Logs/DSA-Catalog.log
```

The log appends across runs. Focus on the last `=== Launch attempt:` block. If the log doesn't exist, the launcher itself isn't running — that points at permissions or quarantine, not script logic.

### Step 2 — Verify bundle structure

```bash
ls -laR "DSA Catalog.app"
```

Check:
- `Contents/MacOS/launcher` is `-rwx` (executable bit set)
- `Contents/Info.plist` exists
- `Contents/Resources/icon.icns` exists

### Step 3 — Check for quarantine attribute

iCloud Drive sometimes adds `com.apple.quarantine` to files it syncs, which makes macOS refuse to launch unsigned apps.

```bash
xattr "DSA Catalog.app"
xattr -lr "DSA Catalog.app"
```

If `com.apple.quarantine` appears, strip it:

```bash
xattr -dr com.apple.quarantine "DSA Catalog.app"
```

### Step 4 — Confirm Python 3 is installed

```bash
which python3
python3 --version
ls -la /opt/homebrew/bin/python3 /usr/local/bin/python3 /usr/bin/python3 2>/dev/null
```

If python3 isn't installed at all, that's a likely root cause. Modern macOS doesn't ship Python anymore. Fix: `xcode-select --install` (installs Apple's developer tools including python3).

### Step 5 — Run the launcher directly from Terminal

The launcher is just a bash script. Run it directly to see live output instead of going through Finder:

```bash
"./DSA Catalog.app/Contents/MacOS/launcher"
```

If this works from Terminal but not from a double-click, the failure is environment-specific (Finder's stripped `$PATH`, different working directory, etc.).

### Step 6 — Simulate Finder's launch environment

Finder launches `.app`s with a minimal `$PATH`. Reproduce it:

```bash
env -i HOME="$HOME" USER="$USER" TMPDIR=/tmp PATH="/usr/bin:/bin:/usr/sbin:/sbin" \
  "./DSA Catalog.app/Contents/MacOS/launcher"
```

If this fails but step 5 worked, there's a PATH-augmentation bug in the launcher.

### Step 7 — Try `open` from Terminal

`open` returns specific LaunchServices errors that Finder hides:

```bash
open "DSA Catalog.app"
```

If you see something like `LSOpenURLsWithRole() failed with error -10810` or `-10827`, look the error code up — those indicate specific macOS protection mechanisms.

### Step 8 — Inspect Info.plist

```bash
plutil -p "DSA Catalog.app/Contents/Info.plist"
```

Confirm `CFBundleExecutable` is `"launcher"` (matches the filename in `Contents/MacOS/`, no path prefix).

### Step 9 — Check LaunchServices cache

If macOS has a stale entry for the bundle ID, it can silently refuse to relaunch. Reset:

```bash
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister \
  -kill -r -domain local -domain system -domain user
touch "DSA Catalog.app"
```

## Likely root causes, in order of probability

1. **`com.apple.quarantine` attribute** — iCloud Drive added it. Fix: `xattr -dr com.apple.quarantine "DSA Catalog.app"`
2. **`python3` not installed** — Apple removed system Python. Fix: `xcode-select --install` or install from python.org
3. **Executable bit lost on iCloud sync** — Fix: `chmod +x "DSA Catalog.app/Contents/MacOS/launcher"`
4. **`CFBundleExecutable` / filename mismatch** in Info.plist
5. **LaunchServices cache** holding a stale entry — Fix: lsregister command in step 9
6. **iCloud placeholder** — file in iCloud Drive isn't actually downloaded yet; `ls -la` shows a small size and a "Download" cloud icon in Finder

## When you've found it

1. **State the diagnosis** plainly in one sentence (e.g., "The launcher script lost its executable bit during iCloud sync — `ls -la` shows `-rw-` instead of `-rwx-`.").
2. **Apply the minimal fix** (one command, not a shotgun of fixes).
3. **Confirm**: `open "DSA Catalog.app"` should launch it; `tail -20 ~/Library/Logs/DSA-Catalog.log` should show the launcher reaching its final `Running: ... serve.py` line, with no errors after.
4. **Smoke test**: visit http://localhost:8765/ in a browser; the catalog page should load with progress checkboxes pre-filled.

## If none of 1-6 above is the cause

Don't keep guessing. Stop and dump these for me:

```bash
cat ~/Library/Logs/DSA-Catalog.log
ls -laR "DSA Catalog.app"
xattr -lr "DSA Catalog.app"
plutil -p "DSA Catalog.app/Contents/Info.plist"
sw_vers
which python3 && python3 --version
```

Paste all of that into your reply so I can see the full state.
