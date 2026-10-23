# 0001. Static site with data files for projects and releases

Status: accepted
Date: 2026-10-23

## Context
The site is a portfolio. Content changes are cards and release entries, not application logic.

## Options
1. CMS or framework with a build: more moving parts than the content needs.
2. Hand-edited HTML: easy until the lists grow.
3. Static HTML with small JSON data files and a validation script.

## Decision
Option 3.

## Consequences
Adding a project or release is a data change checked by CI. No server code to patch. Revisit if content volume or editors grow.
