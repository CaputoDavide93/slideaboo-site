<div align="center">

<img src="docs/assets/brand/icon.png" width="96" alt="The Slideaboo app icon: a white duck peeking out of a sliding yellow tile">

# 🧩 Slideaboo site

**Privacy policy, support and philosophy pages for the Slideaboo toddler puzzle app, in English and Italian**

![HTML](https://img.shields.io/badge/HTML-static-E34F26?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-light_and_dark-1572B6?logo=css3&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-hosted-222222?logo=github&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
[![CI](https://github.com/CaputoDavide93/slideaboo-site/actions/workflows/ci.yml/badge.svg)](https://github.com/CaputoDavide93/slideaboo-site/actions/workflows/ci.yml)

</div>

---

## ✨ Features

This is the website for **Slideaboo**, a calm sliding-picture puzzle for small children and the grown-up beside them, on iPhone, iPad and Android. The app's Settings and its store listings link here for the privacy policy and the support page, so those addresses stay fixed.

The privacy page says what stays on the device (the grown-ups' settings only), that the app asks for no permissions, how the optional child's name is stored and erased, and how to delete everything. Each page exists in English and Italian.

Live at [caputodavide93.github.io/slideaboo-site](https://caputodavide93.github.io/slideaboo-site/).

| | Page | What it is |
|---|---|---|
| 🏠 | [Home](https://caputodavide93.github.io/slideaboo-site/) | What the app is, in a few lines |
| 🔒 | [Privacy policy](https://caputodavide93.github.io/slideaboo-site/privacy/) | What the app keeps on the device (the grown-ups' settings only), permissions (none), links, payments (none), children. Linked from the app's settings and the store listings |
| ✉️ | [Contact](https://caputodavide93.github.io/slideaboo-site/contact/) | Support address and common questions. Linked from the app's settings and the store listings |
| 🌱 | [Philosophy](https://caputodavide93.github.io/slideaboo-site/philosophy/) | Why the app exists: the app's own "Why" screen, word for word |
| 🌍 | English and Italian | Each page in both languages (`it/`), linked to each other. The app opens the Italian privacy and contact pages when it runs in Italian, and the English ones otherwise |
| 🌗 | Light and dark | Follows the reader's system setting, in the app's own colours |
| 🚫 | No tracking | No scripts, forms, cookies or analytics, and a check that fails if one appears |
| 🔎 | Findable | Canonical URLs, `hreflang` alternates, a sitemap, `robots.txt` and `llms.txt` |
| 🧪 | Self-checking | `make check` verifies every page exists, every local link resolves, metadata is present and the support address is the only one |

The pages are plain HTML and CSS: no scripts, forms, cookies or analytics, and a check fails the build if one appears. Only English and Italian exist. GitHub Pages may keep standard server logs for visitors, and the privacy page says so.

---

## 📸 Screenshots

Taken from the served site by `make screenshots` (Chromium, 900 px wide). The
contact page is left out because it shows the support address.

<table>
<tr>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/screenshots/home-dark.png">
  <img src="docs/assets/screenshots/home-light.png" alt="The Slideaboo home page: the headline 'Slide the tiles, and the picture is whole again.' and a card of short facts about the app">
</picture>
</td>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/screenshots/privacy-dark.png">
  <img src="docs/assets/screenshots/privacy-light.png" alt="The privacy policy page with an 'In short' card: no account, no internet, no analytics, ads or tracking, nothing to buy, no AI">
</picture>
</td>
</tr>
<tr>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/screenshots/philosophy-dark.png">
  <img src="docs/assets/screenshots/philosophy-light.png" alt="The philosophy page: why Slideaboo exists, with four short cards">
</picture>
</td>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/screenshots/home-it-dark.png">
  <img src="docs/assets/screenshots/home-it-light.png" alt="The Italian home page: 'Fai scorrere le tessere e l'immagine torna intera.'">
</picture>
</td>
</tr>
</table>

---

## 🗺️ Architecture

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/architecture-dark.svg">
  <img src="docs/assets/architecture-light.svg" width="100%" alt="The app's Settings and the store listings link to this site; a reader's browser fetches static HTML and CSS from GitHub Pages, in English or Italian.">
</picture>

How it is built is in [docs/how-it-works.md](docs/how-it-works.md).

---

## 🚀 Quick Start

You need Python 3 and a browser. There is no build step, and `make check` uses only the standard library.

```bash
git clone https://github.com/CaputoDavide93/slideaboo-site.git
cd slideaboo-site
make serve     # preview at http://localhost:8000
make check     # the same checks CI runs
```

Editing a page, retaking the images and what each check covers are in [docs/setup.md](docs/setup.md).

---

## 🧪 Tested on

| Environment | Status |
|---|---|
| Chromium (Playwright 1.64.1) on macOS, light and dark | ✅ Screenshots and layout checked |
| `make check` on Python 3.12 (CI, Ubuntu) | ✅ Runs on every pull request |
| Safari and Firefox | ❔ Unverified: plain HTML and CSS, not tried here |
| Screen readers | ❔ Unverified |

---

## 📁 Repo structure

```text
slideaboo-site/
├── index.html             # 🏠 home
├── privacy/index.html     # 🔒 privacy policy
├── contact/index.html     # ✉️ contact and support
├── philosophy/index.html  # 🌱 why the app exists
├── it/                    # 🇮🇹 the same four pages in Italian
├── assets/                # 🎨 site.css and the app icon in three sizes
├── docs/                  # 📚 setup, how it works, FAQ, troubleshooting
│   └── assets/            # 🖼️ diagram, screenshots, social preview, README icon
├── tools/                 # 🔧 check_site.py, gen_diagram.py, brand/, screenshots/
├── .github/workflows/     # 🤖 ci.yml runs make check
├── Makefile               # ⚙️ check, serve, diagram, screenshots, social
├── llms.txt               # 🤖 the site in one plain-text page for search tools
├── robots.txt  sitemap.xml  # 🔎 crawler files
├── AGENTS.md              # 🧭 contributor and agent notes
├── CONTRIBUTING.md  SECURITY.md  LICENSE
├── .nojekyll              # serve files as they are
└── .gitignore
```

---

## 📦 Deployment

GitHub Pages serves the root of `main`, so a merged pull request is the release.
CI runs `make check` on every pull request and on every push to `main`. The
privacy pages must stay true to the app's own `docs/privacy.md`: change both
together, in both languages, with a new effective date. Settings labels are
quoted from the app's ARB files (`lib/l10n/app_*.arb`), and the philosophy pages
are its `whyTitle` to `whyClosing` copy, in the order the screen shows it.

---

## 🛠️ Troubleshooting

[docs/troubleshooting.md](docs/troubleshooting.md) lists symptoms and fixes:
a page that 404s on GitHub Pages, a failing `make check`. Common questions are
in [docs/faq.md](docs/faq.md). The full index is [docs/README.md](docs/README.md).

---

## 🔒 Security

See [SECURITY.md](SECURITY.md).

---

## 🤝 Contributing

Found a wrong sentence, a broken link or a page that reads badly on your
device? [Open an issue](https://github.com/CaputoDavide93/slideaboo-site/issues/new)
with the page address, your browser and operating system with versions, and a
screenshot if it is a layout problem. Reports from browsers and devices not
listed under Tested on are especially useful. Details are in
[CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📄 License

[MIT](LICENSE)

---

<p align="center"><sub>Made with ❤️ by <a href="https://github.com/CaputoDavide93">Davide Caputo</a></sub></p>
