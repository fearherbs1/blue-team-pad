#pragma once

#include "config_common.h"

// set number of keymap layers
#define DYNAMIC_KEYMAP_LAYER_COUNT 6

// increase usb polling rate
#define USB_POLLING_INTERVAL_MS 1

// eeprom size config
// This is the max allowable size by qmk as of Nov-3-2022
#define WEAR_LEVELING_LOGICAL_SIZE 65536
#define WEAR_LEVELING_BACKING_SIZE 131072

// Encoder Config
//#define ENCODER_DIRECTION_FLIP
//#define ENCODER_RESOLUTION 4

#ifdef OLED_ENABLE
#    define OLED_DISPLAY_128X32
#define I2C1_SCL_PIN        GP27
#define I2C1_SDA_PIN        GP26
#define I2C_DRIVER I2CD2
#define OLED_BRIGHTNESS 128
#endif
