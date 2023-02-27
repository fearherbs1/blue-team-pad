print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.consts import UnicodeMode
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import send_string

keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

encoder_handler.pins = ((board.GP25, board.GP28, None, False), (board.GP1, board.GP0, None, False),)
keyboard.col_pins = (board.GP24, board.GP23, board.GP21, board.GP20, board.GP3)
keyboard.row_pins = (board.GP2, board.GP11, board.GP10, board.GP9, board.GP8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.extensions.append(MediaKeys())

encoder_handler.map = ( ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.NO),( KC.MEDIA_NEXT_TRACK, KC.MEDIA_PREV_TRACK,KC.NO),),
                        ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.NO),( KC.MEDIA_NEXT_TRACK, KC.MEDIA_PREV_TRACK,KC.NO),),
                        ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, KC.NO),( KC.MEDIA_NEXT_TRACK, KC.MEDIA_PREV_TRACK,KC.NO),),
                        )

keyboard.debug_enabled = False

M1 = send_string("gci \"C:\\Users\\*\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\*\"")

keyboard.keymap = [
    [
    KC.AUDIO_MUTE, KC.NO,KC.NO, KC.NO, KC.MEDIA_PLAY_PAUSE, 
	M1, KC.D, KC.E, KC.F, KC.G, 
	KC.H, KC.I, KC.J, KC.K, KC.L, 
	KC.M, KC.N, KC.O, KC.P, KC.Q, 
	KC.R, KC.S, KC.T, KC.U, KC.Z
    ],
    [
    KC.A, KC.NO,KC.NO, KC.NO, KC.C, 
	KC.C, KC.D, KC.E, KC.F, KC.G, 
	KC.H, KC.I, KC.J, KC.K, KC.L, 
	KC.M, KC.N, KC.O, KC.P, KC.Q, 
	KC.R, KC.S, KC.T, KC.U, KC.Z
    ],
    [
    KC.A, KC.NO,KC.NO, KC.NO, KC.C, 
	KC.C, KC.D, KC.E, KC.F, KC.G, 
	KC.H, KC.I, KC.J, KC.K, KC.L, 
	KC.M, KC.N, KC.O, KC.P, KC.Q, 
	KC.R, KC.S, KC.T, KC.U, KC.Z
    ]
]

if __name__ == '__main__':
    keyboard.go()