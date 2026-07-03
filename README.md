# P2P Foundation Documentation

Source repository for [docs.p2p.foundation](https://docs.p2p.foundation), the official documentation of the P2P Foundation.

Documentation is authored as one markdown file per audience in `content/` and compiled into a multi-section [Docusaurus](https://docusaurus.io/) site by `build_docs.py`, driven by `docs.config.json`. The site covers the protocol whitepaper and dedicated guides for token holders, builders, merchants, users, and the community, published in English, Spanish, Portuguese, and Indonesian. Offline search, Mermaid diagrams, and an embedded AI assistant are configured through the same pipeline.

## Requirements

- Node.js 20 or later
- Python 3 (3.11 in CI, standard library only)

## Quick Start

```bash
npm install
python3 build_docs.py   # use `python` on Windows
npm start
```

The site is served at `http://localhost:3000`.

## Project Structure

```
content/                  Source of truth: one markdown file per doc section
docs.config.json          Pipeline configuration: docs, navbar, footer, integrations
build_docs.py             Compiles content/ into pages, sidebars, and site config
translations/             Hand-maintained Spanish, Portuguese, and Indonesian pages
scripts/lint_content.py   Content style linter, enforced in CI
src/                      React components, theme customizations, custom pages
static/                   Static assets (brand, images)
netlify.toml              Production build and deploy configuration
.github/workflows/        Pull request build validation
```

`generated/`, `sidebars/`, and `docusaurus.config.ts` are build outputs and are gitignored. Do not edit `docusaurus.config.ts` by hand. It is regenerated from `docs.config.json` on every build.

## Adding or Editing Documentation

1. Edit or create a markdown file in `content/`. Use a single H1 (`#`) for the document title, H2 (`##`) for chapters, and H3 (`###`) for subsections. Each H2 becomes its own page (`splitByHeading: 2`). List the H1 title in `skipSections` so it does not become a page.
2. For a new document, register it in the `docs` array of `docs.config.json`:

   ```json
   {
     "id": "my-doc",
     "source": "content/my-doc.md",
     "outputDir": "my-doc",
     "routeBasePath": "my-doc",
     "navbarLabel": "My Doc",
     "navbarPosition": "left",
     "sidebarId": "myDocSidebar",
     "extractImages": false,
     "splitByHeading": 2,
     "numberSections": false,
     "generateTocLinks": false,
     "sidebarStyle": "flat",
     "skipSections": ["My Doc"]
   }
   ```

3. Build and preview with `python3 build_docs.py && npm start`.

### Content Style

CI rejects content that violates the house style, enforced by `scripts/lint_content.py`:

- No emoji or decorative glyphs
- No em or en dashes, and no semicolons in prose
- Write "token holders", never "investors", and link to `/for-token-holders/`
- FAQ must be the final section of every "For ..." guide (the whitepaper is exempt)

Run it locally before pushing:

```bash
python3 scripts/lint_content.py
```

## Translations

Translated pages live in `translations/{es,pt,id}` as final Docusaurus markdown and are tracked in git.

- To update a page, edit its file directly (for example `translations/es/whitepaper/00-abstract.md`).
- To add a page, also register it in the matching `preGeneratedFiles` list in `docs.config.json` and in `translations/<lang>/sidebar.ts`.

## Commands

| Command | Purpose |
| --- | --- |
| `python3 build_docs.py` | Compile content into the site |
| `python3 build_docs.py --clean` | Delete generated output and rebuild |
| `python3 build_docs.py --validate-only` | Validate markdown structure without building |
| `python3 scripts/lint_content.py` | Check content style rules |
| `npm start` | Local development server |
| `npm run build` | Production build into `build/` |
| `npm run serve` | Preview the production build |
| `npm run typecheck` | TypeScript checks |

## CI and Deployment

- **Pull requests:** GitHub Actions runs the Build Validation workflow: content lint, markdown validation, and a full site build.
- **Production:** Netlify builds and deploys `main` using the command in `netlify.toml` and publishes `build/`.

## License

© P2P Foundation. All rights reserved.
