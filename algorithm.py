#!/usr/bin/env python3

from time import sleep

XOR_KEY = '10101010'

def sleep_for(seconds):
    for i in range(seconds):
        print(str(seconds - i) + '...')
        sleep(1)

def ordinals(message):
    sleep_for(15)
    return ''.join([str(ord(c)) + " " for c in message])

def caesar(message):
    sleep_for(30)
    return ''.join([chr(ord(c) + 3) + " " for c in message])

def binary(message):
    sleep_for(60)
    return ''.join([bin(ord(c))[2:].zfill(8) + " " for c in message])

def xor(message):
    sleep_for(120)
    return ''.join([chr(int(bin(ord(c))[2:].zfill(8), 2) ^ int(XOR_KEY, 2)) + " " for c in message])


def decrypt_ordinals(message):
    ords = message.strip().split(' ')
    return ''.join([chr(int(o)) for o in ords])

def decrypt_caesar(message):
    return ''.join([chr(ord(c) - 3) for c in message.strip().replace(' ', '')])

def decrypt_binary(message):
    bins = message.strip().split(' ')
    return ''.join([chr(int(b, 2)) for b in bins])

def decrypt_xor(message):
    return ''.join([chr(int(bin(ord(c))[2:], 2) ^ int(XOR_KEY, 2)) for c in message.strip().replace(' ', '')])