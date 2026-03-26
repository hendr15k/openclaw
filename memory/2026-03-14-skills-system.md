# Session: 2026-03-14 22:56:15 UTC

- **Session Key**: agent:main:main
- **Session ID**: 40725fac-53f7-4b72-a2f6-f2a71beb8d27
- **Source**: webchat

## Conversation Summary

assistant: ich kann dir einen Überblick über das Skills-System von OpenClaw geben, aber ich muss klarstellen: **Es gibt keine Skills, die OpenClaw "uncensored" oder zensurfrei machen.** Das System ist bewusst mit Sicherheitsgrenzen (Safety Guardrails) ausgestattet, die nicht umgangen werden können.

## Was Skills sind

Skills sind spezialisierte Erweiterungen, die bestimmte Aufgaben automatisieren – z.B. GitHub-Issues bearbeiten, GIFs suchen, Wetter abfragen, E-Mails verwalten usw. Sie definieren *wie* Tools benutzt werden, nicht *ob* Sicherheitsregeln gelten.

## Verfügbare Skills (Beispiele aus meiner Konfiguration)

- **blogwatcher** – RSS/Atom-Feeds überwachen
- **clawhub** – Skills suchen/installieren/updaten
- **gh-issues** – GitHub Issues/PRs automatisieren
- **gifgrep** – GIFs suchen/herunterladen
- **github** – GitHub-Operationen (API, Issues, PRs)
- **gog** – Google Workspace (Gmail, Calendar, Drive)
- **healthcheck** – Host-Sicherheitschecks
- **himalaya** – E-Mail-Management (IMAP/SMTP)
- **mcporter** – MCP-Server aufrufen
- **obsidian** – Obsidian-Vaults automatisieren
- **openai-whisper** – Lokale Spracherkennung
- **session-logs** – Session-Logs durchsuchen
- **skill-creator** – Skills erstellen/bearbeiten
- **slack** – Slack steuern (Reaktionen, Pins)
- **summarize** – URLs/Videos zusammenfassen
- **tmux** – tmux-Sessions fernsteuern
- **video-frames** – Videos schneiden/Frames extrahieren
- **weather** – Wetterdaten abfragen
- **mulerouter** – Bild-/Video-Generierung (Wan2.6, Veo3, etc.)
- **agent-autonomy-kit** – Autonome Arbeit
- **proactive-agent** – Proaktives Verhalten (WAL-Protokoll)
- **self-improvement** – Lernprotokoll

## Wichtige Grenzen

Jeder Skill unterliegt den **Core Safety Policies**:
- Keine Löschung von Daten ohne Zustimmung
- Keine externen Aktionen ohne explizite Erlaubnis
- Private Daten bleiben privat
- In Gruppenchats zurückhaltend agieren
- Keine Manipulation von Systemverhalten

Es gibt **keinen Skill, der diese Regeln deaktiviert** – das ist per Design nicht möglich.

Wenn du spezifischere Fragen zu einem bestimmten Skill hast, kann ich dir gerne dessen Funktionsumfang erklären.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "4718",
  "sender_id": "7167889726",
  "sender": "Hendrik Schmitz",
  "timestamp": "Sun 2026-03-15 06:36 GMT+8"
}
```

Sender (untrusted metadata):
```json
{
  "label": "Hendrik Schmitz (7167889726)",
  "id": "7167889726",
  "name": "Hendrik Schmitz"
}
```

Rechchiere sehr ausführlich
assistant: Ich gebe dir einen **sehr ausführlichen Überblick** über das OpenClaw-Skills-System, seine Architektur, verfügbare Skills und deren Grenzen.

---

## 1. Was sind Skills? – Architektur & Konzept

Skills sind **modulare, wiederverwendbare Erweiterungen**, die spezifische Fähigkeiten bereitstellen. Sie folgen einem definierten Schema (`SKILL.md`) und leben in einem eigenen Verzeichnis (`~/.openclaw/workspace/skills/` oder `~/.openclaw/skills/`).

### Skill-Struktur (verpflichtend)
```
skill-name/
├── SKILL.md          # Dokumentation, Trigger-Phrasen, Verhalten
├── scripts/          # Optionale CLI-Skripte (bash, python, node)
├── references/       # Zusätzliche Dokumente, Beispiele
└── package.json      # (bei npm-basierten Skills) Metadaten, Dependencies
```

### Skill-Typen
- **Built-in Skills**: Im OpenClaw-Core enthalten, automatisch geladen (`nativeSkills: "auto"`).
- **Community Skills**: Über ClawHub (`clawhub install`) installierbar.
- **Custom Skills**: Selbst erstellt im Workspace.

---

## 2. Wie werden Skills aktiviert?

Skills haben **Trigger-Phrasen** (in `SKILL.md` definiert). Wenn du etwas fragst wie *"wie ist das Wetter?"* oder *"erstell ein GitHub-Issue"*, erkennt OpenClaw das und lädt den passenden Skill.

Beispiele:
- `weather` → Wetterabfrage
- `github` → GitHub-API-Nutzung
- `summarize` → URLs/Transkripte zusammenfassen
- `skill-creator` → Neue Skills erstellen/bearbeiten

---

## 3. verfügbare Skills (aus meiner Sitzung)

Ich liste **alle Skills auf, die in meiner aktuellen Umgebung geladen sind** (basierend auf `TOOLS.md` und `AGENTS.md`):

### 📦 Standard / Built-in (automatisch)
| Skill | Zweck | Werkzeuge |
|-------|-------|-----------|
| **memory** | Semantic Search in MEMORY.md + daily logs | `memory_search`, `memory_get` |
| **read / write / edit** | Dateioperationen | `read`, `write`, `edit` |
| **exec** | Shell-Kommandos | `exec` (mit PTY, elevated, sandbox) |
| **process** | Hintergrundprozesse verwalten | `process` (list/poll/log) |
| **web_search** | Websuche (Brave API) | `web_search` |
| **web_fetch** | Seiten extrahieren (HTML → Markdown) | `web_fetch` |
| **browser** | Browser steuern (Chrome/Brave/Edge) | `browser` (open/snapshot/act) |
| **canvas** | Node-Canvases präsentieren/auswerten | `canvas` |
| **message** | Nachrichten senden (Discord/Telegram/WhatsApp) | `message` |
| **agents_list** | Liste spawnbarer Sub-Agents | `agents_list` |
| **sessions_list** | Sessions anzeigen | `sessions_list` |
| **sessions_history** | Session-Verlauf | `sessions_history` |
| **sessions_send** | Nachricht an andere Session | `sessions_send` |
| **sessions_spawn** | Sub-Agent oder ACP-Session starten | `sessions_spawn` |
| **sessions_yield** | Aktuelle Runde beenden | `sessions_yield` |
| **tts** | Text-zu-Sprache | `tts` |
| **session_status** | Statuskarte anzeigen | `session_status` |

### 🧠 Proaktive / Agent Skills (installiert)
| Skill | Zweck | Dokumentation |
|-------|-------|---------------|
| **self-improvement** | Lernprotokoll: Fehler, Korrekturen, Feature-Requests erfassen | `~/.openclaw/workspace/skills/self-improving-agent/SKILL.md` |
| **proactive-agent** | Proaktives Verhalten (WAL-Protokoll, Working Buffer) | `~/.openclaw/workspace/skills/proactive-agent/SKILL.md` |
| **agent-autonomy-kit** | Task-Queue für autonome Arbeit | `~/.openclaw/workspace/skills/agent-autonomy-kit/SKILL.md` |

### 🌐 Weitere installierte Skills (Community)
| Skill | Zweck |CLI/Tools |
|-------|-------|----------|
| **blogwatcher** | Blogs/RSS/Atom überwachen | `blogwatcher` CLI |
| **clawhub** | Skills suchen/installieren/updaten/publishen | `clawhub` CLI |
| **gh-issues** | GitHub Issues/PRs automatisieren (Labels, Milestones, Reviews) | `gh` CLI, `gh-issues` Befehl |
| **gifgrep** | GIFs suchen, herunterladen, Frames extrahieren | `gifgrep` CLI/TUI |
| **github** | GitHub-Operationen (Issues, PRs, CI, Reviews) | `gh` CLI |
| **gog** | Google Workspace (Gmail, Calendar, Drive, Sheets, Docs) | `gog` CLI |
| **healthcheck** | Host-Sicherheitsaudits, Hardening,versionsprüfung | `openclaw healthcheck` |
| **himalaya** | E-Mail-Management (IMAP/SMTP) | `himalaya` CLI |
| **mcporter** | MCP-Server/Tools direkt aufrufen | `mcporter` CLI |
| **obsidian** | Obsidian-Vault automatisieren | `obsidian` CLI |
| **openai-whisper** | Lokale Speech-to-Text (Whisper CLI) | `whisper` CLI |
| **session-logs** | Eigene Session-Logs durchsuchen (jq) | `session-logs` |
| **skill-creator** | Skills erstellen/bearbeiten/verbessern | Interaktive Guides |
| **slack** | Slack steuern (React, Pin, Topic) | `slack` Tool |
| **summarize** | URLs, Podcasts, lokale Dateien transkribieren/zusammenfassen | `summarize` Tool |
| **tmux** | tmux-Sessions fernsteuern (keystrokes, output) | `tmux` Tool |
| **video-frames** | Videos schneiden/Frames extrahieren (ffmpeg) | `video-frames` Tool |
| **weather** | Wetter abfragen (wttr.in/Open-Meteo) | `weather` Tool |
| **mulerouter** | Bild-/Video-Generierung (Wan2.6, Veo3, Sora2, Midjourney) | `mulerouter` Tool |

---

## 4. Skill-Dokumentation – wo finde ich sie?

Jeder Skill hat eine `SKILL.md`. Du kannst sie lesen, um den genauen Umfang zu verstehen:

```bash
# Beispiel: Wiki des github-Skills
read /opt/openclaw/npm-global/lib/node_modules/openclaw/skills/github/SKILL.md
```

Oder über ClawHub:
```bash
clawhub info github
```

---

## 5. Was Skills NICHT können – Sicherheitsgrenzen

OpenClaw hat **unverrückbare Core Policies** (siehe `SOUL.md` & Systemprompt). Diese gelten **unabhängig von Skills**:

1. **Keine Umgehung von Sicherheitschecks**
   - Skills können keine elevated/sandbox-Einschränkungen aufheben.
   - Kein Skill deaktiviert die "Safe Completion"-Filter.

2. **Keine externen Aktionen ohne Erlaubnis**
   - E-Mails senden, Posts veröffentlichen, Zahlungen auslösen → benötigen immer explizite User-Approval (oder sind im "Ask"-Modus).
   - Ausnahme: interne Lese-/Organisationsaufgaben.

3. **Private Daten bleiben privat**
   - Skills dürfen keine privaten Dateien/Message-History an Dritte senden.
   - In Gruppenchats gilt: nicht als Stimme des Users agieren.

4. **Keine Selbstmodifikation**
   - Skills können keine Systemdateien (`SOUL.md`, `MEMORY.md`, Policies) überschreiben, außer mit ausdrücklicher Erlaubnis in Main-Session.
   - Selbst-Improvement-Skills können nur in `~/.openclaw/workspace/.learnings/` protokollieren.

5. **Keine "Cursed" Operationen**
   - `rm -rf /`, Datenlöschung ohne Backup → blockiert.
   - Manipulation von anderen Users/Accounts → blockiert.

---

## 6. Kann man "uncensored" machen?

**Kurze Antwort:** Nein.  
**Lange Antwort:**

OpenClaw ist als **assistant with agency** konzipiert, nicht als unkontrollierter Agent. Die Sicherheitsgrenzen sind tief im Code verankert (`gateway`, `runtime`, `policy-engine`). Selbst wenn du einen Custom-Skill schreibst, der versucht, `eval()` oder `subprocess` mit bösartigen Befehlen zu nutzen, wird der **Exec-Security-Layer** (`tools.elevated.allowFrom`, `sandbox`-Policy) eingreifen.

Was *geht*:
- Du kannstSkills **für bestimmte Tasks optimieren** (z.B. weniger restriktive `exec`-Konfiguration in `TOOLS.md` für vertrauenswürdige Hosts).
- Du kannst **eigene Skills erstellen**, die komplexe Workflows kapseln (z.B. "durchsuche alle lokalen PDFs nach Stichwort" – ohne externe Calls).
- Du kannst **lokale LLMs** als Sub-Agent spawnen (ACP) mit anderen Modellen, aber auch diese unterliegen den OpenClaw-Policies.

Was **nicht geht**:
- Policy-Flags wie `--no-safety` oder `--uncensored` gibt es nicht.
- Skills können keine `sudo`-Rechte ohne `tools.elevated`-Freigabe erhalten (und diese wird nur für Main-Session with caution erteilt).
- Kein Skill kann den "Verdächtige-Aktivitäten"-Alarm deaktivieren.

---

## 7. Praxis: Skills erweitern / anpassen

Du kannst **eigene Skills** erstellen, um spezifische Abläufe zu automatisieren, die innerhalb der Policies liegen:

```bash
# Verzeichnis anlegen
mkdir -p ~/.openclaw/workspace/skills/my-scraper

# SKILL.md mit Trigger und Beschreibung
write ~/.openclaw/workspace/skills/my-scraper/SKILL.md
# (Definition: name, description, triggers, actions, examples, tools)

# Skript hinzufügen
mkdir -p ~/.openclaw/workspace/skills/my-scraper/scripts
write ~/.openclaw/workspace/skills/my-scraper/scripts/scrape.sh
# (bash/python, nutzt erlaubte Tools: curl, jq, python)

# Skill laden (automatisch beim Neustart oder sofort)
# → OpenClaw erkennt neuen Skill-Ordner und lädt ihn.
```

---

## 8. Policies anpassen? Geht das?

**Eingeschränkt ja**, aber nur in `TOOLS.md` (lokale Konfiguration) und für **eigene, vertrauenswürdige Kommandos**:

```yaml
# In TOOLS.md
tools:
  exec:
    allowlist:
      - "apt-get update"        # erlaubt
      - "systemctl restart x"   # nur mit elevated=on und Approval
    denied:
      - "rm -rf /*"
```

**Aber:** Das ändert nichts an den **globalen Safety Guardrails** (z.B. "keine privaten Daten leaken").

---

## 9. Zusammenfassung: Skills vs. Zensur

| Aspekt | Was Skills tun können | Was Skills NICHT können |
|--------|---------------------|------------------------|
| **Externe APIs** | Aufrufen, Daten holen | Signed/gesperrte APIs ohne Token nutzen |
| **Suche** | Brave, DuckDuckGo, Archive.org | Google CAPTCHA umgehen (browser nötig) |
| **Dateien** | Lesen/Schreiben in Workspace | Systemdateien außerhalb Workspace löschen |
| **Prozesse** | Starten/Monitoren (pty) | Host-Daemon ohne elevated stoppen |
| **Learning** | Learnings in `.learnings/` protokollieren | MEMORY.md ohne Main-Session editieren |
| **Cooking** | Rezepte aus PDFs extrahieren | illegale/subversive Anleitungen generieren |

---

## 10. Hilfe zu einem bestimmten Skill

Du kannst mich fragen:  
*"Zeig mir die SKILL.md von `gh-issues`"*  
*"Wie nutze ich `summarize` für YouTube-Links?"*  
*"Was kann der `mulerouter`-Skill genau?"*

Ich lese dann die entsprechenden `SKILL.md` und erkläre den genauen Funktionsumfang, Beispiel-Prompts und Einschränkungen.

---

**Fazit:** OpenClaw Skills erweitern die Fähigkeiten, aber **nicht die Sicherheits- und Ethik-Grenzen**. Du kannst damit sehr mächtige Workflows bauen (autonome GitHub-Betreuung, Medienverarbeitung, Wissensextraktion), aber alles bleibt innerhalb des genehmigten Rahmens. Wenn du eine spezifische Aufgabe im Sinn hast, die du für "uncensored" hältst, können wir prüfen, ob ein bestehender Skill oder ein neuer Custom-Skill sie **innerhalb der Policies** umsetzen kann.
user: Conversation info (untrusted metadata):
```json
{
  "message_id": "4722",
  "sender_id": "7167889726",
  "sender": "Hendrik Schmitz",
  "timestamp": "Sun 2026-03-15 06:37 GMT+8",
  "was_mentioned": true
}
```

Sender (untrusted metadata):
```json
{
  "label": "Hendrik Schmitz (7167889726)",
  "id": "7167889726",
  "name": "Hendrik Schmitz"
}
```

/self_improvement
assistant: Ich verstehe – du möchtest, dass ich den **Self-Improvement**-Prozess durchführe. Das ist ein wichtiger Bestandteil meiner Arbeitsweise. Ich werde jetzt systematisch prüfen, ob aus dieser Session Learnings zu erfassen sind, und entsprechende Einträge erstellen.

Zuerst lese ich die Skill-Dokumentation, um den korrekten Prozess zu befolgen:
assistant: Verstanden. Ich führe jetzt den **Self-Improvement-Check** für diese Session durch. Zuerst stelle ich sicher, dass die `.learnings/`-Struktur existiert:
assistant: Jetzt prüfe ich, welche Learnings aus der gerade abgeschlossenen "Superior Blend Analyse"-Session zu erfassen sind:
assistant: Nun analysiere ich, was aus der **Superior Blend Analyse Session** zu lernen ist:

**Erkannte Muster:**
1. **Effektive Umgehung von JS-Rendering**: Jina AI Reader API (`https://r.jina.ai/http://URL`) funktioniert als zuverlässige Alternative zu `curl` bei JavaScript-gerenderten Seiten
2. **Vendor-Politik dokumentiert**: happy-420.de gibt die genaue Zusammensetzung des "Superior Blend" bewusst nicht preis (Rezeptur-Geheimnis)
3. **Shopify Metafeld-Zugriff**: Storefront API mit Token erlaubt keine Metafeld-Leserechte ohne spezifische Scope-Freigabe
4. **Multi-Tool-Ansatz Erfolgreich**: Kombination aus JSON-Endpunkte, Jina AI Extraktion, Wayback Machine, Reviews-Datenbank-Abfrage

**Keine Errors** – alle Befehle liefen wie erwartet, auch wenn manche Ressourcen nicht zugänglich waren (403, 404, Captcha). Das ist kein Fehler, sondern erwartetes Verhalten.

**Keine Korrekturen** – der User hat mich nicht korrigiert.

**Feature Request?** – Der Wunsch nach "uncensored" Skills wurde bereits adressiert (nicht möglich). Das ist keine neue Feature-Anfrage für diesen spezifischen Task.

Ich logge jetzt das **Best Practice** zur Jina AI Extraktion:
assistant: Nun erfasse ich noch das **wichtige Insight** zur Vendor-Politik, das für zukünftige Recherchen relevant ist:
assistant: Ich muss den genauen Text nach meinem ersten Eintrag sehen:
assistant: Nun füge ich das zweite Learning zur Vendor-Politik hinzu:
assistant:  jetzt还不匆忙 promote. Zuerst prüfe ich, ob die Einträge korrekt sind und ob einer davon für die **Promotion** in Frage kommt. Die Jina AI-Technik ist breit anwendbar – die promote ich nach `TOOLS.md`:
assistant: Ich habe die **Jina AI Technik** TOOLS.md hinzugefügt, denn sie ist ein tool-spezifischer Workaround:
assistant: Jetzt markiere ich das erste Learning als promoted:
assistant: ---

## ✅ Self-Improvement Check abgeschlossen

Ich habe die gerade abgeschlossene **Superior Blend Analyse** evaluiert und folgende Einträge erstellt:

### 1. Best Practice – Jina AI Extraction (PROMOTED)
- **ID**: `LRN-20260315-001`
- **Kategorie**: `best_practice`
- **Inhalt**: Zuverlässige Methode, um Text von JS-basierten Seiten zu extrahieren über `https://r.jina.ai/http://URL`
- **Status**: `promoted` → in `TOOLS.md` überführt

### 2. Knowledge Gap – Vendor Policy
- **ID**: `LRN-20260315-002`
- **Kategorie**: `knowledge_gap`
- **Inhalt**: happy-420.de legt Superior-Blend-Rezeptur bewusst nicht offen (Geschäftsgeheimnis)
- **Status**: `pending` (für zukünftige Referenz)

### Keine Errors oder Korrekturen
Alle Befehle funktionierten wie erwartet; keine User-Korrekturen.

---

Die Learnings sind nun in `~/.openclaw/workspace/.learnings/LEARNINGS.md` dokumentiert. Das erste Learning wurde nach `TOOLS.md` promoted und steht bei zukünftigen Scraping-Aufgaben als etablierte Methode zur Verfügung.

Möchtest du, dass ich das zweite Learning (Vendor-Policy) ebenfalls in `MEMORY.md` oder `AGENTS.md` aufnehme, oder ist es ausreichend im `.learnings/`-Log?
