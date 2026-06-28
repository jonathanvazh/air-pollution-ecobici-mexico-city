# Decision Log

A running record of non-obvious technical and methodological decisions for
this project, with the reasoning and the alternatives considered.

Format inspired by Architecture Decision Records (ADRs).

---

## 2026-06-26 — Tooling and project setup

### Repository is public, licensed MIT
- **Decision:** Public GitHub repo under the MIT License.
- **Why:** This is a portfolio piece meant to be seen and reused. Without a
  license, default copyright applies and no one may legally reuse the code.
  MIT is the most permissive common license: reuse freely, keep the notice,
  no warranty.
- **Note / open item:** MIT covers *code*, not *data* or written content.
  Public data (SEDEMA, Ecobici) carries its own terms of use; prose and
  figures may later warrant a CC-BY license. To revisit.

### Custom .gitignore instead of a generated one
- **Decision:** Hand-written .gitignore tailored to this stack.
- **Why:** Commit the *recipe*, never the *cooked meal*. The virtual
  environment (.venv/), the DuckDB files, raw data, and Quarto build output
  (_site/, .quarto/) are all reproducible or machine-specific, so they stay
  out of version control. Keeps the repo light, clean, and free of secrets
  or heavy data.

### Python managed with uv
- **Decision:** uv for Python version, environment, and dependencies.
- **Why:** Single fast tool. The pair pyproject.toml + uv.lock pins exact
  versions, so the environment rebuilds identically on any machine or in a
  year. Reproducibility by default.

### Local repo lives outside OneDrive
- **Decision:** Clone to C:\dev\, not under the OneDrive-synced user folder.
- **Why:** OneDrive syncing a .git folder in the background can corrupt Git
  history. Earlier projects lived under OneDrive; this one deliberately does
  not.

### Publishing with Quarto to GitHub Pages
- **Decision:** Quarto website published via `quarto publish gh-pages`.
- **Why:** Quarto turns analysis (text + code) into a clean website with one
  command. The gh-pages branch keeps published output separate from source.
  Walking-skeleton method: ship a thin end-to-end slice first, then fatten.

---

## Open items / decisions still to make
- License for data and written content (CC-BY?) — see MIT note above.
- station_id namespace bug: SINAICA catalog id 32 = Aguascalientes, not CDMX.
  Verify which real monitor each Ecobici station maps to before building on it.
- PM2.5 scale discrepancy (daily ~12–78 µg/m³ vs hourly <1) — confirm which
  file fed the 40/50/75 flags.
- Line endings: add a .gitattributes to normalize CRLF/LF (cosmetic, deferred).

---

## 2026-06-27 — First real data slice (air quality)

### Data folder structure: one subfolder per source
- **Decision:** `data/air_quality/`, `data/ecobici/`, `data/weather/`.
- **Why:** Keeping three sources in a flat `data/` folder becomes a mess fast.
  Separating by source keeps things navigable as the project grows.
- **Future option:** add `raw/` vs `processed/` inside each source later.

### Code lives in `scripts/`, not the project root
- **Decision:** Python scripts go in `scripts/`.
- **Why:** Loose scripts in the root turn into clutter. `scripts/` is the
  standard place for run-from-start-to-finish programs (vs `src/` for
  importable packages).

### Manual download now, documented; scripted fetch later
- **Decision:** Download data files by hand for this slice, but record
  provenance in a `SOURCE.md` next to each file (committed to Git even though
  the data itself is gitignored).
- **Why:** Walking-skeleton method — validate the full pipeline first, harden
  the extraction layer next. Manual-but-documented closes the traceability gap
  without stalling progress. A scripted `scripts/extract/` fetch comes next.

### Gitignore data contents but keep provenance docs
- **Decision:** `.gitignore` ignores `data/**` but makes exceptions for folders
  and `*.md` files.
- **Why:** Version the *provenance* (where data came from), never the heavy
  data. Recruiters can see how data was sourced without the repo carrying it.

### Publish with local render, not GitHub Actions
- **Decision:** `quarto publish gh-pages` (renders locally, pushes HTML).
- **Why:** The page executes Python against a gitignored CSV. Rendering locally
  means the computation happens where the data lives; only the finished HTML
  (with the number already baked in) is published. GitHub Actions would fail —
  it has no access to the local data. Keeps private data on the local machine.

### Data quality finding: file name is misleading
- **Finding:** The portal file is named `rama_2023_05.csv` but contains the FULL
  daily series 2015–2023 (3073 rows), not May 2023. The misleading name comes
  from the portal itself.
- **Lesson:** Verify file *content*, never trust the *name*. Recorded in the
  file's SOURCE.md.