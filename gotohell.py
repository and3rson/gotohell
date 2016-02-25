#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from evdev import uinput, ecodes as e
import time
from random import choice


MAP = {
    u'й': e.KEY_Q,
    u'ц': e.KEY_W,
    u'у': e.KEY_E,
    u'к': e.KEY_R,
    u'е': e.KEY_T,
    u'н': e.KEY_Y,
    u'г': e.KEY_U,
    u'ш': e.KEY_I,
    u'щ': e.KEY_O,
    u'з': e.KEY_P,
    u'х': e.KEY_LEFTBRACE,
    u'ъ': e.KEY_RIGHTBRACE,

    u'ф': e.KEY_A,
    u'ы': e.KEY_S,
    u'в': e.KEY_D,
    u'а': e.KEY_F,
    u'п': e.KEY_G,
    u'р': e.KEY_H,
    u'о': e.KEY_J,
    u'л': e.KEY_K,
    u'д': e.KEY_L,
    u'ж': e.KEY_SEMICOLON,
    u'э': e.KEY_APOSTROPHE,

    u'я': e.KEY_Z,
    u'ч': e.KEY_X,
    u'с': e.KEY_C,
    u'м': e.KEY_V,
    u'и': e.KEY_B,
    u'т': e.KEY_N,
    u'ь': e.KEY_M,
    u'б': e.KEY_COMMA,
    u'ю': e.KEY_DOT,

    u'ё': e.KEY_GRAVE
}


def press(a, key):
    a.append((e.EV_KEY, key, 1))


def release(a, key):
    a.append((e.EV_KEY, key, 0))


def hit(a, key):
    a.append((e.EV_KEY, key, 1))
    a.append((e.EV_KEY, key, 0))


def type(s):
    args = []
    for c in s:
        if c in MAP.keys():
            # Lower
            hit(args, MAP[c])
        elif c.lower() in MAP.keys():
            # Upper
            press(args, e.KEY_LEFTSHIFT)
            hit(args, MAP[c.lower()])
            release(args, e.KEY_LEFTSHIFT)
        elif c == ' ':
            hit(args, e.KEY_SPACE)
        elif c == '.':
            hit(args, e.KEY_SLASH)
        elif c == ',':
            hit(args, e.KEY_COMMA)
        elif c == '?':
            press(args, e.KEY_LEFTSHIFT)
            hit(args, e.KEY_7)
            release(args, e.KEY_LEFTSHIFT)
        elif c == '!':
            press(args, e.KEY_LEFTSHIFT)
            hit(args, e.KEY_1)
            release(args, e.KEY_LEFTSHIFT)

    with uinput.UInput() as ui:
        for triple in args:
            ui.write(*triple)
        ui.write(e.EV_KEY, e.KEY_ENTER, 1)
        ui.write(e.EV_KEY, e.KEY_ENTER, 0)
        ui.syn()


time.sleep(1)

f = open('phrases.txt', 'r')
phrases = f.read().decode('utf-8').split('\n')
f.close()

type(choice(phrases))
