# 🦞 OpenClaw Android APK (Fork)

> **[⬇️ Latest APK Release](../../releases/latest)** · [Original: openclaw/openclaw](https://github.com/openclaw/openclaw)

Dieser Fork ist **ausschließlich dafür gedacht, Android APKs** der neueste OpenClaw Version zu bauen. Die App wird als eigenständige App mit der Package-ID `ai.openclaw.app.hendr15k` installiert und kann **parallel zur offiziellen OpenClaw App** auf demselben Gerät laufen.

## ⬇️ APK Download

Gehe zu **[Releases](../../releases)** und lade das neueste `openclaw-*.apk` herunter.

**Installieren:** APK auf dem Android-Gerät öffnen und zustimmen ("aus unbekannten Quellen installieren" erlauben).

**Parallel-Installation:** Dieses APK hat die Package-ID `ai.openclaw.app.hendr15k` und blockiert **nicht** die offizielle OpenClaw App (`ai.openclaw.app`).

## 🔧 Build Workflow

Der Android Build läuft automatisch via GitHub Actions:

```yaml
# .github/workflows/android-build.yml
on:
  push:
    branches: [main]
  workflow_dispatch:
```

Build Steps:
1. Code checkout
2. Java 17 + Android SDK 36 setup
3. `./gradlew assemblePlayDebug`
4. APK Upload als Artifact (90 Tage Retention) + Release Asset

## 🔄 Upstream Syncen

Dieser Fork wird regelmäßig mit [openclaw/openclaw](https://github.com/openclaw/openclaw) synced:

```bash
git remote add upstream https://github.com/openclaw/openclaw.git
git fetch upstream main
git merge upstream/main
git push origin main
```

Jeder Push auf `main` löst automatisch einen neuen Android Build aus und erstellt automatisch ein Release mit APK.

## 📱 Android Node Konfiguration

Die App verbindet sich mit deinem lokalen OpenClaw Gateway:

- **Host:** Hostname oder IP deines Servers/VPS
- **Port:** Gateway-Port (default: `18789`)
- **Token:** Dein Gateway Auth Token aus `~/.openclaw/openclaw.json`

Nach dem ersten Setup erscheint "OpenClaw Hendr15k" als eigenständige App auf deinem Android-Gerät.

## 🆚 Unterschied zum Original

| | Offizielles OpenClaw | Dieser Fork |
|---|---|---|
| **Repo** | openclaw/openclaw | hendr15k/openclaw |
| **Package ID** | `ai.openclaw.app` | `ai.openclaw.app.hendr15k` |
| **Version** | `vYYYY.M.D` | `vYYYY.M.D-android` |
| **Zweck** | Full OpenClaw Distribution | Android APK Builds |
| **Installierbar** | Parallel | Parallel |

## 📋 Build Status

Aktueller Build-Status ist als Badge oben in diesem Repo sichtbar.

---

**Upstream:** [openclaw/openclaw](https://github.com/openclaw/openclaw) · [OpenClaw Docs](https://docs.openclaw.ai) · [Discord](https://discord.gg/clawd)
