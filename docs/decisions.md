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