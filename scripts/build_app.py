"""
Build a macOS .app bundle for the DSA Catalog launcher.

Output: <workspace>/DSA Catalog.app/
Structure:
  Contents/
    Info.plist
    MacOS/launcher         # bash script that runs serve.py
    Resources/icon.icns    # the icon
"""
import io
import os
import struct
import stat
import shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

WORKSPACE = Path("/sessions/ecstatic-tender-cray/mnt/Data Structure & Algorithm")
APP_DIR = WORKSPACE / "DSA Catalog.app"

# ----------------------------------------------------------------------
# Generate the icon as a 1024x1024 PNG
# ----------------------------------------------------------------------

def gradient(size, top, bottom):
    img = Image.new("RGB", (1, size), top)
    for y in range(size):
        r = top[0] + (bottom[0] - top[0]) * y // size
        g = top[1] + (bottom[1] - top[1]) * y // size
        b = top[2] + (bottom[2] - top[2]) * y // size
        img.putpixel((0, y), (r, g, b))
    return img.resize((size, size))


def macos_rounded_mask(size):
    """macOS Big Sur+ icons use a squircle. Approximate with a heavy rounded rect."""
    # macOS app icon margin: ~10% on each side, corner radius ~22.5% of canvas
    margin = int(size * 0.10)
    inner = size - 2 * margin
    radius = int(inner * 0.225)
    mask = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle(
        [(margin, margin), (margin + inner - 1, margin + inner - 1)],
        radius=radius,
        fill=255,
    )
    return mask


def find_font(size):
    """Best-effort font discovery — fall back to PIL default if missing."""
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except OSError:
                continue
    return ImageFont.load_default()


def make_icon(size=1024):
    """Build the icon at the requested pixel size."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))

    # Background gradient on a squircle
    grad = gradient(size, (47, 85, 151), (95, 50, 165)).convert("RGBA")
    mask = macos_rounded_mask(size)
    img.paste(grad, (0, 0), mask)

    # Soft inner highlight — adds depth
    highlight = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    hd = ImageDraw.Draw(highlight)
    margin = int(size * 0.10)
    inner = size - 2 * margin
    radius = int(inner * 0.225)
    hd.rounded_rectangle(
        [(margin, margin), (margin + inner - 1, margin + int(inner * 0.45))],
        radius=radius,
        fill=(255, 255, 255, 28),
    )
    img = Image.alpha_composite(img, highlight)

    # Draw "DSA" text big and centered
    d = ImageDraw.Draw(img)
    font_size = int(size * 0.36)
    font = find_font(font_size)
    text = "DSA"
    bbox = d.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (size - tw) // 2 - bbox[0]
    ty = int(size * 0.46) - th // 2 - bbox[1]

    # subtle drop shadow
    shadow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.text((tx + int(size * 0.006), ty + int(size * 0.008)), text, font=font, fill=(0, 0, 0, 100))
    shadow = shadow.filter(ImageFilter.GaussianBlur(int(size * 0.006)))
    img = Image.alpha_composite(img, shadow)

    d = ImageDraw.Draw(img)
    d.text((tx, ty), text, font=font, fill=(255, 255, 255, 255))

    # Small caption below — "Catalog"
    cap_font_size = int(size * 0.11)
    cap_font = find_font(cap_font_size)
    cap = "Catalog"
    cb = d.textbbox((0, 0), cap, font=cap_font)
    cw = cb[2] - cb[0]
    ch = cb[3] - cb[1]
    cx = (size - cw) // 2 - cb[0]
    cy = int(size * 0.78) - ch // 2 - cb[1]
    d.text((cx, cy), cap, font=cap_font, fill=(255, 255, 255, 220))

    return img


# ----------------------------------------------------------------------
# Pack PNGs into a minimal .icns
# ----------------------------------------------------------------------
# macOS .icns: 'icns' magic + size + sequence of (type:4, len:4, payload).
# Types we use:
#   ic08 = 256x256 PNG
#   ic09 = 512x512 PNG
#   ic10 = 1024x1024 (also 512@2x) PNG
#   ic11 = 32x32 @1x  PNG  (also 16@2x)
#   ic12 = 64x64 @1x  PNG  (also 32@2x)
#   ic13 = 256x256 @2x PNG (i.e. 512px)
#   ic14 = 512x512 @2x PNG (i.e. 1024px)
# Modern macOS picks the appropriate one at render time. We supply a few sizes.

def png_bytes(img):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def build_icns(master_png):
    """master_png: PIL.Image at 1024x1024. Returns bytes of an .icns file."""
    sizes = {
        b"ic07": 128,    # 128x128
        b"ic08": 256,    # 256x256
        b"ic09": 512,    # 512x512
        b"ic10": 1024,   # 1024x1024
        b"ic11": 32,     # 16@2x (small toolbar)
        b"ic12": 64,     # 32@2x
        b"ic13": 256,    # 128@2x
        b"ic14": 512,    # 256@2x
    }
    parts = []
    for type_code, px in sizes.items():
        resized = master_png.resize((px, px), Image.LANCZOS)
        payload = png_bytes(resized)
        parts.append(type_code + struct.pack(">I", len(payload) + 8) + payload)
    body = b"".join(parts)
    header = b"icns" + struct.pack(">I", len(body) + 8)
    return header + body


# ----------------------------------------------------------------------
# Build the .app bundle
# ----------------------------------------------------------------------

INFO_PLIST = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>DSA Catalog</string>
    <key>CFBundleDisplayName</key>
    <string>DSA Catalog</string>
    <key>CFBundleIdentifier</key>
    <string>local.malo.dsa-catalog</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>CFBundleExecutable</key>
    <string>launcher</string>
    <key>CFBundleIconFile</key>
    <string>icon.icns</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.13</string>
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>LSUIElement</key>
    <false/>
</dict>
</plist>
"""

LAUNCHER = r"""#!/bin/bash
# Launcher for DSA Catalog.app
# When Finder launches a .app, $PATH is minimal — it does NOT include the
# Homebrew or python.org install locations. So we explicitly check well-known
# spots and log everything to a file you can read.

LOG="$HOME/Library/Logs/DSA-Catalog.log"
mkdir -p "$(dirname "$LOG")"

# Logging: redirect stdout+stderr to the log
exec >> "$LOG" 2>&1
echo
echo "=================================================="
echo "Launch attempt: $(date)"
echo "PATH (as seen by Finder-launched .app):"
echo "  $PATH"

# Add common python3 install locations to PATH
export PATH="/opt/homebrew/bin:/usr/local/bin:/Library/Frameworks/Python.framework/Versions/Current/bin:$PATH"
echo "PATH (after augmenting):"
echo "  $PATH"

# Find python3
PY=""
for candidate in python3 /opt/homebrew/bin/python3 /usr/local/bin/python3 /usr/bin/python3 \
                 /Library/Frameworks/Python.framework/Versions/Current/bin/python3 \
                 /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 \
                 /Library/Frameworks/Python.framework/Versions/3.12/bin/python3 \
                 /Library/Frameworks/Python.framework/Versions/3.11/bin/python3; do
    if command -v "$candidate" >/dev/null 2>&1 && "$candidate" --version >/dev/null 2>&1; then
        PY="$candidate"
        break
    fi
done

if [ -z "$PY" ]; then
    echo "ERROR: python3 not found anywhere"
    osascript -e 'display alert "Python 3 not found" message "Install Python 3 from python.org (or Homebrew) and try again. A log is at ~/Library/Logs/DSA-Catalog.log."'
    exit 1
fi
echo "Using python3: $PY"
"$PY" --version

# Resolve the folder this .app lives in
APP_PATH="$(cd "$(dirname "$0")/../.." && pwd)"   # ...DSA Catalog.app
PARENT="$(dirname "$APP_PATH")"                    # the project folder
echo "App lives at: $APP_PATH"
echo "Working dir : $PARENT"
cd "$PARENT" || { echo "ERROR: cannot cd to $PARENT"; exit 1; }

if [ ! -f "serve.py" ]; then
    echo "ERROR: serve.py not found in $PARENT"
    osascript -e "display alert \"serve.py not found\" message \"Expected it next to DSA Catalog.app in $PARENT — keep the .app and serve.py in the same folder, or run python3 serve.py from Terminal.\""
    exit 1
fi

# Check port isn't in use already (gives clearer error than letting Python crash)
if command -v lsof >/dev/null 2>&1; then
    if lsof -nP -iTCP:8765 -sTCP:LISTEN >/dev/null 2>&1; then
        echo "WARNING: port 8765 already in use — another instance may be running"
        # Don't fail — let Python's error surface naturally; the user might just want to focus the running tab
    fi
fi

echo "Running: $PY serve.py"
exec "$PY" serve.py
"""


def main():
    # Wipe any old bundle so we don't accumulate stale files
    if APP_DIR.exists():
        shutil.rmtree(APP_DIR)
    (APP_DIR / "Contents" / "MacOS").mkdir(parents=True, exist_ok=True)
    (APP_DIR / "Contents" / "Resources").mkdir(parents=True, exist_ok=True)

    # Info.plist
    (APP_DIR / "Contents" / "Info.plist").write_text(INFO_PLIST)

    # Launcher script — executable
    launcher_path = APP_DIR / "Contents" / "MacOS" / "launcher"
    launcher_path.write_text(LAUNCHER)
    launcher_path.chmod(launcher_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    # Icon
    print("Generating icon...")
    master = make_icon(1024)
    # Save the master PNG separately too (useful for re-using elsewhere)
    master.save(APP_DIR / "Contents" / "Resources" / "icon.png", format="PNG")
    icns_bytes = build_icns(master)
    (APP_DIR / "Contents" / "Resources" / "icon.icns").write_bytes(icns_bytes)
    print(f"  icon.icns size: {len(icns_bytes):,} bytes")

    # PkgInfo (optional but classic)
    (APP_DIR / "Contents" / "PkgInfo").write_text("APPL????")

    print(f"\nBuilt: {APP_DIR}")
    print("Structure:")
    for p in sorted(APP_DIR.rglob("*")):
        rel = p.relative_to(APP_DIR)
        marker = "/" if p.is_dir() else ""
        size = f"  ({p.stat().st_size:,} bytes)" if p.is_file() else ""
        print(f"  {rel}{marker}{size}")


if __name__ == "__main__":
    main()
