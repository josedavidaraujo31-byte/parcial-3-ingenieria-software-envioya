# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2026-11-11

### Added

- Business customers receive a 12% discount.
- Business shipments weighing more than 10 kg are exempt from rural and national zone surcharges.
- Acceptance tests CP39–CP44 and change-impact documentation.

## [2.0.0] - 2026-11-11

### Added

- Zone pricing strategies for urban, rural, and national shipments.
- Regression tests for the four reported defects, zone strategies, and the public API.

### Changed

- Refactored `calc` into named calculation steps and constants.
- Removed the legacy `flag` parameter and its print side effect. This is a breaking API change.
- Use decimal arithmetic and half-up rounding to the nearest $100.

### Fixed

- Reject invalid zones and days.
- Apply the weekend surcharge on both Saturday and Sunday.
- Return the exact invalid-weight message `peso inválido`.

## [1.0.0] - 2026-11-11

### Added

- Legacy EnvíaYa calculation baseline with the personalized configuration for student code ending in 410026.
