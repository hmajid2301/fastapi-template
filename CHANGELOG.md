# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
## [0.3.1] - 2022-06-27
### Fixed
- Small mistakes specific to core-api.

## [0.3.0] - 2022-06-27
### Changed
- Upgraded to python 3.10.
- Upgraded to copier version 6 syntax.

## [0.2.6] - 2022-05-06
### Fixed
- Broken coverage job in Gitlab CI `coberature` is not a report type anymore.


## [0.2.5] - 2022-05-05
### Changed
- Reference ENV variables using `${VAR}` rather than `$VAR`.
- Bump `omnibus` to latest version.
- Use poetry for pre-commit hooks, so we don't have to maintain multiple versions of our dev tools.

### Fixed
- Set the operation id to be the function handler name. The function should be called after all routes have been imported.

## [0.2.4] - 2022-01-04
### Changed
- `docker-compose.yml` to use hashamp for env variables.
- `Dockerfile` to copy after installing the deps, so we dont have to rebuild everytime any file changes.
- Bumped `omnibus` to `0.2.1`.

### Fixed
- Typo in `service.yaml` double `__` for env variables.

## [0.2.3] - 2022-01-04
### Fixed
- Turn boolean into string in the `service.yaml` for the `USE_AUTH` env variable, to make it compliant with the knative specification.

## [0.2.2] - 2022-01-03
### Added
- `auth.py` which is a factory function which will validate a JWT token for an incoming request.

### Fixed
- Update `service.yaml` file with latest values for auth i.e. client id and use auth.

- Missing `git` in base stage of Dockerfile, so we can install `omnibus` properly.

### Changed
- Updated `omnibus` version to use latest version `0.2.0`, which includes Google OAuth2 support.

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

[unreleased]: https://gitlab.com/banter-bus/fastapi-template/compare/0.3.1...main
[0.3.0]: https://gitlab.com/banter-bus/fastapi-template/compare/0.3.1...0.3.0
[0.3.0]: https://gitlab.com/banter-bus/fastapi-template/compare/0.3.0...0.2.6
[0.2.6]: https://gitlab.com/banter-bus/fastapi-template/compare/0.2.6...0.2.5
[0.2.5]: https://gitlab.com/banter-bus/fastapi-template/compare/0.2.5...0.2.4
[0.2.4]: https://gitlab.com/banter-bus/fastapi-template/compare/0.2.4...0.2.3
[0.2.3]: https://gitlab.com/banter-bus/fastapi-template/compare/0.2.3...0.2.2
[0.2.2]: https://gitlab.com/banter-bus/fastapi-template/compare/0.2.2...0.2.1
[0.2.1]: https://gitlab.com/banter-bus/fastapi-template/compare/0.2.1...0.2.0
[0.2.0]: https://gitlab.com/banter-bus/fastapi-template/compare/0.2.0...0.1.2
[0.1.2]: https://gitlab.com/banter-bus/fastapi-template/compare/0.1.2...0.1.1
[0.1.1]: https://gitlab.com/banter-bus/fastapi-template/compare/0.1.1...0.1.0
[0.1.0]: https://gitlab.com/banter-bus/fastapi-template/-/tags/0.1.0
