# Key Project Decisions

This document tracks the major design and process decisions for the HK Racing Project, along with context, alternatives considered, and rationale.

| Date       | Decision                                   | Aspect             | Alternatives Considered               | Rationale / Notes                    |
|------------|--------------------------------------------|--------------------|---------------------------------------|--------------------------------------|
| 2025-05-04 | Use MkDocs + Material theme for docs site  | Documentation      | GitHub Pages from `/docs`, Jekyll     | Better theming, built-in nav sidebar |
| 2025-05-04 | Deploy docs via GitHub Actions to `gh-pages` | CI/CD             | Manual Pages from `/docs` folder      | Full control over build, future plugins |
| 2025-05-05 | Design repo for AI-only assistance; skip human-centric features | Repository Setup   | Public repo setup, contributor templates, open-source guidelines | Ensures proprietary strategies remain private, limits liability; sharing steps can be added later |
| 2025-05-06 | Configure pre-commit hooks for code and notebooks       | Tooling      | Manual formatting, commit-by-commit cleaning                         | Automate code style enforcement and strip notebook outputs            |
| 2025-05-06 | Add GitHub Actions workflows for CI and docs deploy     | CI/CD        | Manual test and docs builds                                           | Automatically lint, test, and deploy docs on push                    |
| 2025-05-06 | Establish branch protection rules on main               | Process      | Unrestricted direct pushes                                             | Ensure all changes are reviewed and pass CI before merge              |
| 2025-05-06 | Create GitHub issue and PR templates                    | Process      | Freeform issues and PR descriptions                                    | Standardize issue reporting and PR reviews                            |
| 2025-05-06 | Scaffold Makefile and setup scripts for environment     | Developer DX | Manual venv creation and pip installs                                  | Provide reproducible one-command environment bootstrapping            |
| 2025-05-06 | Rolled back branch protection rules for personal repo      | Process      | Enforced PR and status checks                             | Simplify workflow for solo development; allow direct pushes  |
| 2025-05-08 | Updated GitHub Pages setup and streamlined milestone tracking | Documentation, Project Management | Manual tracking, individual project boards | Simplify the process with GitHub Issues and checkboxes for clarity and task management |
| 2025-05-08 | Remove GitHub Project board and house issues in Markdown    | Process      | Online project board                                 | Centralize issue tracking within repository docs        |
| 2025-05-XX | (future decision)                          |                    |                                       |                                      |
