# Key Project Decisions

This document tracks the major design and process decisions for the HK Racing Project, along with context, alternatives considered, and rationale.

| Date       | Decision                                   | Aspect             | Alternatives Considered               | Rationale / Notes                    |
|------------|--------------------------------------------|--------------------|---------------------------------------|--------------------------------------|
| 2025-05-04 | Use MkDocs + Material theme for docs site  | Documentation      | GitHub Pages from `/docs`, Jekyll     | Better theming, built-in nav sidebar |
| 2025-05-04 | Deploy docs via GitHub Actions to `gh-pages` | CI/CD             | Manual Pages from `/docs` folder      | Full control over build, future plugins |
| 2025-05-05 | Design repo for AI-only assistance; skip human-centric features | Repository Setup   | Public repo setup, contributor templates, open-source guidelines | Ensures proprietary strategies remain private, limits liability; sharing steps can be added later |
| 2025-05-XX | (future decision)                          |                    |                                       |                                      |
