#!/usr/bin/env python3

from simple_term_menu import TerminalMenu
import socket
import select
import sys

from algorithm import *

HOST = "10.0.0.91"  # The server's hostname or IP address
PORT = 8081  # The port used by the server

def encrypt_with_level(message, level):
    if level == 1: return ordinals(message)
    elif level == 2: return caesar(message)
    elif level == 3: return binary(message)
    elif level == 4: return xor(message)

def decrypt_with_level(message, level):
    try:
        if level == 1: return decrypt_ordinals(message)
        elif level == 2: return decrypt_caesar(message)
        elif level == 3: return decrypt_binary(message)
        elif level == 4: return decrypt_xor(message)
    except:
        print('Error decrypting message!')

def run_base(server):
    print('You are in charge of distributing encrypted information to your field agent in order to acheive your objective.\n')
    print('Connecting...')
    while True:
 
        # maintains a list of possible input streams
        sockets_list = [sys.stdin, server]
    
        read_sockets, _, _ = select.select(sockets_list, [], [])
    
        for socket in read_sockets:
            # Message originates from server, just decode and print it.
            if socket == server:
                message = socket.recv(2048).decode()
                print(message)

            # Message originates from you, encrypt it, send it to the server, and print it in your window for posterity.
            else:
                raw_message = sys.stdin.readline().rstrip()
                components = raw_message.split(':')
                encrypt_level = int(components[0])
                message = components[1].strip()
                encrypted = encrypt_with_level(message, encrypt_level)
                server.send((str(encrypt_level) + ': ' + encrypted).encode())
                print("\n<You> ")
                print(encrypted)
                print()
                sys.stdout.flush()

def run_read_only(server, has_keys):
    print('Connecting...')
    while True:
            sockets_list = [server]
            read_sockets, _, _ = select.select(sockets_list, [], [])

            for socket in read_sockets:
                # Message originates from server, just decode and print it.
                if socket == server:
                    message_data = socket.recv(2048).decode()
                    print(message_data)
                    if has_keys and not message_data == "Connected to the messaging channel.\n":
                        print('Attempting to decrypt the message...\n')
                        components = message_data.split('\n')
                        raw_message = components[1]
                        msg_components = raw_message.split(':')
                        encryption_level = int(msg_components[0].strip())
                        message = msg_components[1].rstrip()
                        
                        print(decrypt_with_level(message, encryption_level))

                        print('\n')
                        

def run_field_agent(server):
    print('You will receive messages here that instruct you what to do in the field. Mix in diversions of your own design to throw the codebreakers off your scent!\n')
    run_read_only(server, True)

def run_codebreaker(server):
    print('You will see all encrypted messages in your terminal here; your objective is to crack them and tell your field agent what to reverse in the field.\n')
    run_read_only(server, False)

if __name__ == '__main__':
    print('\nWelcome to Codebreakers!\n')
    
    role_options = ['Base', 'Field Agent', 'Codebreaker']
    menu = TerminalMenu(role_options, title='Choose your role: ')
    index = menu.show()
    role = role_options[index]
    
    # Connect to server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((HOST, PORT))
    
    # Begin subroutines
    if role == 'Base': run_base(server)
    elif role == 'Field Agent': run_field_agent(server)
    elif role == 'Codebreaker': run_codebreaker(server)
