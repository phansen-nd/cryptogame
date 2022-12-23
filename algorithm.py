#!/usr/bin/env python3

XOR_KEY = '10101010'


def ordinals(message):
    return ''.join([str(ord(c)) + " " for c in message])

def caesar(message):
    return ''.join([chr(ord(c) + 3) + " " for c in message])

def binary(message):
    return ''.join([bin(ord(c))[2:].zfill(8) + " " for c in message])

def xor(message):
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