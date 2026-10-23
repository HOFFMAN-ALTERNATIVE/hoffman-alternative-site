# Hoffman Alternative site

Static portfolio site driven by JSON data: projects and releases. Skeleton.

## Status

Skeleton. This repository holds the layout, interfaces and decisions. The working implementation is not published.

## Why

A portfolio whose lists are data, so adding a project or a release does not touch the page code.

## Architecture

Static HTML and CSS served by any web server. Project cards and the release list render from JSON files validated in CI. A strict Content-Security-Policy applies and the page loads no third-party scripts except embedded players that are explicitly allow-listed.

More in [docs/architecture.md](docs/architecture.md).

## Layout

- `site/` static HTML and CSS
- `data/` JSON schema examples with fake entries
- `scripts/` data validation
- `docs/` architecture and ADRs

## Run

```sh
python3 scripts/validate_data.py
python3 -m http.server --directory site 8000
```

## Design decisions

- [0001 Static site with data files for projects and releases](docs/adr/0001-static-site-with-data-files-for-projects-and-releases.md)

## Roadmap

- [ ] Project cards from JSON
- [ ] Release list from JSON with platform links
- [ ] Image pipeline to compressed WebP
- [ ] Link checker in CI
- [ ] Accessibility pass (keyboard, contrast, reduced motion)

## Security

See [SECURITY.md](SECURITY.md). CI runs a leak scan on every push.

## License

MIT, see [LICENSE](LICENSE).
