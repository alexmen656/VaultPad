import board
from kmk.kmk_keyboard import KMKKeyboard # type: ignore
from kmk.scanners.keypad import KeysScanner # type: ignore
from kmk.keys import KC # type: ignore
from kmk.modules.macros import Press,Release,Tap,Macros # type: ignore

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)
PINS=[board.D3, board.D4, board.D1, board.D2]

keyboard.matrix = KeysScanner(
    pins = PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.MACRO(# Screenshot & Screen Recording Macro
            Tap(KC.LCMD(KC.LSFT(KC.N5)))  # macOS screenshot of selected area
        ),
        KC.MACRO(# Open Terminal & VS Code
            Tap(KC.LCMD(KC.SPC)),
            Tap(KC.T), Tap(KC.E), Tap(KC.R), Tap(KC.M), Tap(KC.I), Tap(KC.N), Tap(KC.A), Tap(KC.L),
            Tap(KC.ENTER),     
            Tap(KC.C), Tap(KC.O), Tap(KC.D), Tap(KC.E), Tap(KC.SPC), Tap(KC.DOT),
            Tap(KC.ENTER)
        ),
        KC.MACRO(# Quick Emoji Reactions
            Tap(KC.LCMD(KC.LCTL(KC.SPC))),
        ),
        KC.MACRO(# Media Control & Focus Mode
            Tap(KC.F8),
            Tap(KC.LCMD(KC.LALT(KC.D))),
        )
    ]
]

if __name__ == '__main__':
    keyboard.go()