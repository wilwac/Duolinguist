# Duolinguist

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

_Component to integrate with a Duolingo account, providing the status of your daily streak._

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `duolinguist`.
4. Download _all_ the files from the `custom_components/duolinguist/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Duolinguist".

## Configuration

This integration utilizes the UI configuration flow, and no YAML configuration is needed!

You will need to input your JWT (JSON Web Token).
Generate it by logging in to duolingo.com and use your browser to open the console and input the following:
`document.cookie.match(new RegExp('(^| )jwt_token=([^;]+)'))[0].slice(11);`
as per the [instructions here](https://github.com/KartikTalwar/Duolingo/issues/128).

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

This repo is a fork from duolinguist repo from [Sam Hanley](https://github.com/sphanley) which has been archived.

***

[integration_blueprint]: https://github.com/wilwac/duolinguist
[commits-shield]: https://img.shields.io/github/commit-activity/y/wilwac/duolinguist.svg?style=for-the-badge
[commits]: https://github.com/wilwac/duolinguist/commits/master
[license-shield]: https://img.shields.io/github/license/wilwac/duolinguist.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/wilwac/duolinguist.svg?style=for-the-badge
[releases]: https://github.com/wilwac/duolinguist/releases
