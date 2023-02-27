// Copyright 2022-2023 Thomas Autiello Jr (@fearherbs1)
// SPDX-License-Identifier: GPL-2.0-or-later

#pragma once

#define VIAL_KEYBOARD_UID {0x70, 0xF0, 0x56, 0xB5, 0x19, 0x4C, 0x58, 0x7C}

// Unlock Combo of Bottom Left & Bottom Right Buttons
#define VIAL_UNLOCK_COMBO_ROWS { 4, 4 }
#define VIAL_UNLOCK_COMBO_COLS { 0, 4 }

// set number of keymap layers
#define DYNAMIC_KEYMAP_LAYER_COUNT 6

// increase usb polling rate
#define USB_POLLING_INTERVAL_MS 1

// eeprom size config
// This is the max allowable size by qmk as of Nov-3-2022
#define WEAR_LEVELING_LOGICAL_SIZE 65536
#define WEAR_LEVELING_BACKING_SIZE 131072

// set number of configurable macros in vial
// this max is 32 for vial version 0.6 and below 
#define DYNAMIC_KEYMAP_MACRO_COUNT 32
