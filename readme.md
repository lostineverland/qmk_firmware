# Quantum Mechanical Keyboard Firmware

[![Current Version](https://img.shields.io/github/tag/qmk/qmk_firmware.svg)](https://github.com/qmk/qmk_firmware/tags)
[![Discord](https://img.shields.io/discord/440868230475677696.svg)](https://discord.gg/Uq7gcHh)
[![Docs Status](https://img.shields.io/badge/docs-ready-orange.svg)](https://docs.qmk.fm)
[![GitHub contributors](https://img.shields.io/github/contributors/qmk/qmk_firmware.svg)](https://github.com/qmk/qmk_firmware/pulse/monthly)
[![GitHub forks](https://img.shields.io/github/forks/qmk/qmk_firmware.svg?style=social&label=Fork)](https://github.com/qmk/qmk_firmware/)

This is a keyboard firmware based on the [tmk\_keyboard firmware](https://github.com/tmk/tmk_keyboard) with some useful features for Atmel AVR and ARM controllers, and more specifically, the [OLKB product line](https://olkb.com), the [ErgoDox EZ](https://ergodox-ez.com) keyboard, and the Clueboard product line.

## Methodology

I went towards using the json file for the layout rather than the ascii map. To install on the Piantor:

- go to the [configurator](https://config.qmk.fm/)
- download the json kemap
- build:
  ```sh
  mv /Users/carlos/Downloads/lostineverland.json ./keyboards/beekeeb/piantor_pro/keymaps/lostineverland/keymap.json
  qmk compile
  ```
- flash firmware on both keyboard halves
  ```sh
  mv beekeeb_piantor_pro_lostineverland.uf2 /Volumes/RPI-RP2
  ```
- build `keymap.json`
  - I made a script `layers.py`
  - which makes use of a `keymap.layout` file
  - to build `layers.json`, which goes into `keymap.json`

## Fine Tuning

I love this keyboard, and as I become more adept at using it, I progressively type faster. Consequently, I started running into some limitations with the home row mods. I also started using a 
wireless version (DAO Choc) which uses ZMK instead of QMK. ZMK identifies a few behavior categories to customize a keyboard to a user's style. QMK identifies the tap/hold "balanced" behavior as one that is favorable for home row mods. In ZMK the equivalent is "permissive hold".

### Troublesome Words:

    - fast
    - some
    - dict
    - I'm
    - split
    - status

## Documentation

* [See the official documentation on docs.qmk.fm](https://docs.qmk.fm)

The docs are powered by [Docsify](https://docsify.js.org/) and hosted on [GitHub](/docs/). They are also viewable offline; see [Previewing the Documentation](https://docs.qmk.fm/#/contributing?id=previewing-the-documentation) for more details.

You can request changes by making a fork and opening a [pull request](https://github.com/qmk/qmk_firmware/pulls), or by clicking the "Edit this page" link at the bottom of any page.

## Supported Keyboards

* [Planck](/keyboards/planck/)
* [Preonic](/keyboards/preonic/)
* [ErgoDox EZ](/keyboards/ergodox_ez/)
* [Clueboard](/keyboards/clueboard/)
* [Cluepad](/keyboards/clueboard/17/)
* [Atreus](/keyboards/atreus/)

The project also includes community support for [lots of other keyboards](/keyboards/).

## Maintainers

QMK is developed and maintained by Jack Humbert of OLKB with contributions from the community, and of course, [Hasu](https://github.com/tmk). The OLKB product firmwares are maintained by [Jack Humbert](https://github.com/jackhumbert), the Ergodox EZ by [ZSA Technology Labs](https://github.com/zsa), the Clueboard by [Zach White](https://github.com/skullydazed), and the Atreus by [Phil Hagelberg](https://github.com/technomancy).

## Official Website

[qmk.fm](https://qmk.fm) is the official website of QMK, where you can find links to this page, the documentation, and the keyboards supported by QMK.
[configurator](https://config.qmk.fm/)