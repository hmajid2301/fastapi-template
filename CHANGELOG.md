# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Changed
- Updated `omnibus` version to use latest version `0.1.1`.

## [0.2.0] - 2021-12-31
### Added
- `copier` to deps and `update-template` make target to pull latest changes.
- `omnibus` library and removed all common code from this project.

### Fixed
- Makefile target `install-hooks` missing run in `poetry run`.

## [0.1.2] - 2021-12-30
### Fixed
- Exclude `CHANGELOG.md` and `README.md` so it doesn't get copied over to templates.

## [0.1.1] - 2021-12-29
### Added
- `.devcontainer` files to gitignore.

### Fixed
- `.devcontainer` service field should be `app`.

## [0.1.0] - 2021-12-29
### Added
- Initial Release.

[unreleased]: https://gitlab.com/banter-bus/fastapi-template/compare/0.2.0...main
[0.2.0]: https://gitlab.com/banter-bus/fastapi-template/compare/0.2.0...0.1.2
[0.1.2]: https://gitlab.com/banter-bus/fastapi-template/compare/0.1.2...0.1.1
[0.1.1]: https://gitlab.com/banter-bus/fastapi-template/compare/0.1.1...0.1.0
[0.1.0]: https://gitlab.com/banter-bus/fastapi-template/-/tags/0.1.0
