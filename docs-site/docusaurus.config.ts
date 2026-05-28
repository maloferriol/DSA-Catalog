import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

const config: Config = {
  title: "DSA Reference",
  tagline: "Data Structures & Algorithms — Search, Learn, Track",
  favicon: "img/favicon.png",

  future: {
    v4: true,
  },

  url: "https://maloferriol.github.io",
  baseUrl: "/learn/",

  organizationName: "maloferriol",
  projectName: "DSA-Catalog",

  onBrokenLinks: "warn",

  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      {
        docs: {
          sidebarPath: "./sidebars.ts",
          routeBasePath: "/",
          editUrl:
            "https://github.com/maloferriol/DSA-Catalog/tree/main/docs-site/",
        },
        blog: false,
        theme: {
          customCss: "./src/css/custom.css",
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: "DSA Reference",
      items: [
        {
          href: "/",
          label: "Exercises",
          position: "left",
          target: "_self",
        },
        {
          type: "docSidebar",
          sidebarId: "tutorialSidebar",
          position: "left",
          label: "Learn",
        },
        {
          href: "https://github.com/maloferriol/DSA-Catalog",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      copyright: `DSA Reference Catalog · Built with Docusaurus`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ["java", "python"],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
