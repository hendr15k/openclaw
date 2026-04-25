# HEARTBEAT.md — Periodic Self-Improvement Checklist

**Letzter Check:** 2026-04-25T02:10:00+02:00

---

## Status

**Aktuelle Zeit:** Sa 25.04.2026 02:10 Berlin / 00:10 UTC

### ✅ Erledigt (2026-04-24 Abendsession)
- ✅ Hendrik-Sci-Fi: CSV-Refactor — Bücher aus `books.csv` statt Inline-JS, Commit `b4199bb`
- ✅ Hendrik-Sci-Fi: Empfehler-Script repariert (Syntax-Fehler durch Curly-Apostrophe), Commit `2261ef1`
- ✅ Hendrik-Sci-Fi: README komplett überarbeitet, Commit `59b1c5b`
- 🏷️ Learning: LRN-20260424-001 — Curly-Apostrophe in JS-Strings = SyntaxError
- 🏷️ Learning: LRN-20260424-002 — Inline-JS mit Nicht-ASCII kann Node.js --check brechen
- 🏷️ Learning: LRN-20260424-003 — `streamTo: parent` ist INVALID für `runtime=subagent`

### ✅ Erledigt (2026-04-25 Nachtsession)
- ✅ Hendrik-Sci-Fi V2: Top 30 Beschreibungen ausgebaut (von 60-80 auf 450-700 Zeichen), Commit `a7974dc`
- ✅ Hendrik-Sci-Fi V2: 13 neue Titel hinzugefügt (163 Bücher insgesamt), Commit `4a80a20`
- ✅ Hendrik-Sci-Fi: load-error Fallback + Build-Marker in index.html, Commit `35c4469`

### ⚠️ Hendrik-Sci-Fi: Empfehlungen-Sichtbarkeit unklar
- Site funktioniert technisch: CSV lädt, Recommender läuft
- Wahrscheinlich Browser-Cache — Hendrik soll Ctrl+Shift+R oder Cache leeren
- Commit `35c4469` hat load-error Fallback bereits gefixt

### ⚠️ Beobachtet / Unklar
- ⚠️ Workspace: ~2.8 GB potentiell aufräumbar
- ⚠️ main-Branch hinkt hinter `feat/obd-pids-cockpit` hinterher — 2 Commits noch nicht gemergt
- ⚠️ OPL Monitor — wartet auf Hendrik Feedback
- ⚠️ Spritpreise Demo-Modus aktiv (API-Key noch tot)

### 🔜 Nächste Schritte
1. **Sci-Fi V2:** Noch mehr neue Titel (30 statt 13) + Empfehlungsfinder testen
2. **main-Merge:** Nach Hendriks Freigabe `feat/obd-pids-cockpit` → main mergen + pushen
3. OPL Monitor Feedback einholen
4. Workspace Cleanup (~2.8 GB) — braucht Freigabe
5. Jules: 5 alte Remote-Branches aufräumen wenn Hendrik zustimmt

## HappyBlue Crash Fixes (2026-04-24)
- ✅ `Resources$NotFoundException: 0x7f0d014b` — 7× hardcodierte `getColor(2131...)` → `R.color.*`
- ✅ `SecurityException: BLUETOOTH_SCAN` — Permission-Guard in `DeviceListActivity` + `ELM327Adapter`
- ✅ BEIDE von Hendrik bestätigt: „Hat sehr gut funktioniert"

## FH-Lernplan — Korrigiert (basierend auf echten Arbeitsblättern)

**Quelle:** HM2 Blätter 1-14 (Hoever SS2024), GET2 Wochen 1-15 / Ü-Blätter 1-10 (SS2025)

### HM2 — 14 Blätter, 5 Phasen
| Phase | Blätter | Themen | Gewichtung |
|-------|---------|--------|------------|
| **A: Analysis** | 1-3 | Mehrdim. Funktionen, partielle Ableitungen, Gradient, Extremstellen, Jacobi-Matrix, Newton-Verfahren | Hoch |
| **B: Integration** | 4-5 | Kurven, Mehrfachintegrale, Kugel-/Zylinderkoordinaten, Weg-/Flächenintegrale | Hoch |
| **C: Vektoranalysis** | 6 | Divergenz, Rotation, Gauß'scher Satz | Mittel |
| **D: DGL** | 7-8 | Lineare DGL, Schwingungen, Schwingkreis, Tiefpass | Hoch |
| **E: Fourier/Laplace** | 9-11 | Fourier-Reihen, Fourier-Transformation, komplexe Fourier, Laplace-Transformation | Hoch |
| **F: Stochastik** | 12-14 | Wahrscheinlichkeit, Exponential-/Normalverteilung, Erwartungswert, Varianz, Statistik | Mittel |

### GET2 — 10 Übungsblätter, 4 Phasen
| Phase | Ü-Blatt | Themen | Gewichtung |
|-------|---------|--------|------------|
| **A: E-Feld** | Ü1-3 | Coulomb, Feldstärke, Influenz, Verschiebungsdichte, Gauß'sches Gesetz | Hoch |
| **B: Potential & Kondensator** | Ü4-5 | Potential, Spannung, Plattenkondensator, Dielektrika, Grenzflächen | Hoch |
| **C: Strom & Magnetfeld** | Ü6-9 | Stromdichte, Ohm, Leistung, Magnetfeld, Flussdichte, Durchflutungsgesetz, Induktivität | Hoch |
| **D: Induktion** | Ü10 | Faraday, zeitlich veränderliches B-Feld, Transformator | Mittel |

### Wochenplan (Do 24.04 → So 11.05)
- **Do 24.04** — 📚 HM2 Blatt 1
- **Sa 26.04** — ⚡ GET2 Ü1
- **So 27.04** — 📚 HM2 Blatt 2
- **Di 29.04** — 📚 HM2 Blatt 3
- **Do 01.05** — ⚡ GET2 Ü2-3
- **Sa 03.05** — 📚 HM2 Blatt 4
- **Mo 05.05** — 📚 HM2 Blatt 5
- **Mi 07.05** — 📚 HM2 Blatt 6
- **Fr 09.05** — ⚡ GET2 Ü4-5
- **So 11.05** — 📚 HM2 Blatt 7

## Learnings (2026-04-22 bis 2026-04-25)
- LRN-20260422-001: Parallele Subagents auf gleiche Files = nur letzter Commit gewinnt
- LRN-20260422-002: GitHub Pages+Vite: lokaler dist/ ist irrelevant
- LRN-20260422-003: Subagent "completed" ohne Token-Output = File-Dump statt Arbeit
- LRN-20260422-004: Lernplan-Themen immer aus echten Kursmaterialien ableiten
- LRN-20260424-001 bis 003: JS Curly-Apostrophe, Node --check, streamTo parent
- LRN-20260425-001: Subagent-Passwort-Interaktionen können Output unterbrechen — direkte Ausführung bevorzugen

## Security
- [x] Config-File Rechte 600
- [x] Gemini API Keys entfernt
- [x] Sonstiges sauber

## Memory
- [x] memory/2026-04-24.md aktuell
- [x] HEARTBEAT.md bereinigt

---

*HEARTBEAT.md aktualisiert 2026-04-25 02:10*
