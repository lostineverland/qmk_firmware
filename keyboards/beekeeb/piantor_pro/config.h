// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#pragma once

#define RP2040_BOOTLOADER_DOUBLE_TAP_RESET
#define RP2040_BOOTLOADER_DOUBLE_TAP_RESET_TIMEOUT 1000U

#define SERIAL_USART_FULL_DUPLEX
#define SERIAL_USART_TX_PIN GP0
#define SERIAL_USART_RX_PIN GP1
#define SERIAL_USART_PIN_SWAP

#define USB_VBUS_PIN GP19

#define SPLIT_HAND_PIN GP17
#define SPLIT_HAND_PIN_LOW_IS_LEFT
#define PERMISSIVE_HOLD

#define TAPPING_TOGGLE 2           // Number of taps to toggle layer locking
#define ONESHOT_TIMEOUT 5000       // Time in milliseconds before the one-shot modifier times out (adjust as needed)
#define ONESHOT_TAP_TOGGLE 2       // Number of taps to toggle the modifier on permanently (set to 0 to disable)
