<div align="center">

# 🧩 Slideaboo site

**The public home, privacy policy, contact and philosophy pages for the Slideaboo app**

![HTML](https://img.shields.io/badge/HTML-static-E34F26?logo=html5&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-hosted-222222?logo=github&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue)

</div>

---

## ✨ Features

| | Page | What it is |
|---|---|---|
| 🏠 | [Home](https://caputodavide93.github.io/slideaboo-site/) | What the app is, in a few lines |
| 🔒 | [Privacy policy](https://caputodavide93.github.io/slideaboo-site/privacy/) | What the app keeps on the device (the grown-ups' settings only), permissions (none), links, payments (none), children. Linked from the app's settings and the store listings |
| ✉️ | [Contact](https://caputodavide93.github.io/slideaboo-site/contact/) | Support address and common questions. Linked from the app's settings and the store listings |
| 🌱 | [Philosophy](https://caputodavide93.github.io/slideaboo-site/philosophy/) | Why the app exists: the app's own "Why" screen, word for word |
| 🌍 | English and Italian | Each page in English and Italian (`it/`), linked to each other. The app opens the Italian privacy and contact pages when it runs in Italian, and the English ones otherwise |
| 🌗 | Light and dark | Follows the reader's system setting, in the app's own colours |
| 🚫 | No tracking | No scripts, cookies or analytics |

---

## 🚀 Quick Start

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
```

GitHub Pages publishes the `main` branch root. The privacy pages must stay true to the app's own `docs/privacy.md`; change both together, in both languages. Settings labels are quoted from the app's ARB files (`lib/l10n/app_*.arb`), and the philosophy pages are its `whyTitle` to `whyClosing` copy, in the order the screen shows it.

---

## 📁 Repo structure

```text
slideaboo-site/
├── index.html             # 🏠 home
├── privacy/index.html     # 🔒 privacy policy
├── contact/index.html     # ✉️ contact and support
├── philosophy/index.html  # 🌱 why the app exists
├── it/                    # 🇮🇹 the same four pages in Italian
├── assets/
│   ├── apple-touch-icon.png  # 🧩 the app icon for a phone's home screen
│   ├── favicon.png        # 🧩 the app icon in the browser tab
│   ├── icon.png           # 🧩 the app icon beside the name on every page
│   └── site.css           # 🎨 light and dark styles
├── .nojekyll              # serve files as they are
├── .gitignore
├── README.md
├── SECURITY.md
└── LICENSE
```

---

## 🔒 Security

See [SECURITY.md](SECURITY.md).

---

## 📄 License

[MIT](LICENSE)

---

<p align="center"><sub>Made with ❤️ by <a href="https://github.com/CaputoDavide93">Davide Caputo</a></sub></p>
