# Autoresearch Configuration

## Goal
Optimale Sci-Fi Empfehlungsliste für Hendrik — maximiere Vorhersage-Genauigkeit seiner Ratings

## Metric
- **Name**: prediction_accuracy
- **Direction**: lower (MSE zwischen predicted und actual rating)
- **Extract command**: Manual feedback from Hendrik after reading
- **Secondary metric**: coverage — Anzahl Bücher in der Liste

## Target Files
- **Google Docs:** Sci-Fi Empfehlungen (live Dokument)
- **Doc ID:** `1Ld0j3JXFb_qkeprynaTf-PGWnd0RIlxSS03cU-FRWaY`
- **URL:** https://docs.google.com/document/d/1Ld0j3JXFb_qkeprynaTf-PGWnd0RIlxSS03cU-FRWaY/edit
- Lokale `sci-fi-recommendations.md` als Backup/Cache

## Read-Only Files
- `memory/ontology/graph.jsonl` — Präferenzen nur lesen

## Run Command
```
# Ein Experiment = Ein Buch vorschlagen, Predicted Rating, auf Feedback warten
# Target: Google Docs via Maton API
```

## Time Budget
- **Per experiment**: Kein festes Limit — Hendrik gibt Feedback wenn er möchte
- **Max experiments**: Endlos bis gestoppt

## Constraints
- Nur Hard Sci-Fi / analytisch / Mind-Fuck / Simulationstheorie / First Contact
- Keine Fantasy, keine Low-Sci-Fi-Romantik
- Keine YA

## Branch
autoresearch/sci-fi-recommendations

## Preferences (aus Ontology)
- Hard Sci-Fi, analytisch, Mind-Fuck, Simulationstheorie, First Contact
-喜: Blindsight, Project Hail Mary, Three-Body Problem, Children of Time
- Dislike: unbekannt

## Current Baseline
Bücher mit已知 Ratings:
- Project Hail Mary: 9/10
- Three-Body Problem: 8/10
