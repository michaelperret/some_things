#!/usr/bin/env python3
import argparse
import re
import sys

def calc_moves_knight(initial_pos_x, initial_pos_y):
    offset_x = [2, 1, -1, -2, -2, -1, 1, 2];
    offset_y = [-1, -2, -2, -1, 1, 2, 2, 1];
    moves = []
    for x in range(0, MAX_BOUNDS):
        x1 = initial_pos_x + offset_x[x]
        y1 = initial_pos_y + offset_y[x]
        if y1 > 0 and y1 < MAX_BOUNDS and x1 > 0 and x1 < MAX_BOUNDS:
            position = '{}{}'.format(number_alphabet_mapping[x1], y1)
            moves.append(position)
    return moves

def calc_moves_queen(input_pos_x, input_pos_y):
    moves = calc_moves_rook(input_pos_x, input_pos_y)
    moves += try_up_right(input_pos_x, input_pos_y)
    moves += try_up_left(input_pos_x, input_pos_y)
    moves += try_down_right(input_pos_x, input_pos_y)
    moves += try_down_left(input_pos_x, input_pos_y)
    return moves

def calc_moves_rook(input_pos_x, input_pos_y):
    moves = try_horizontal(input_pos_x, input_pos_y)
    moves += try_vertical(input_pos_x, input_pos_y)
    return moves


def try_horizontal(input_pos_x, input_pos_y):
    moves = []
    for x in range(1, MAX_BOUNDS + 1):
        if x == input_pos_x:
            continue
        position = '{}{}'.format(number_alphabet_mapping[x], input_pos_y)
        moves.append(position)
    return moves

def try_vertical(input_pos_x, input_pos_y):
    moves = []
    for x in range(1, MAX_BOUNDS + 1):
        if x == input_pos_y:
            continue
        position = '{}{}'.format(number_alphabet_mapping[input_pos_x], x)
        moves.append(position)
    return moves

def try_up_right(input_pos_x, input_pos_y):
    moves = []
    for x in range(max(input_pos_x, input_pos_y), MAX_BOUNDS):
        input_pos_x += 1
        input_pos_y += 1
        position = '{}{}'.format(number_alphabet_mapping[input_pos_x], input_pos_y)
        moves.append(position)
    return moves

def try_up_left(input_pos_x, input_pos_y):
    moves = []
    for x in range(input_pos_y, MAX_BOUNDS):
        input_pos_x -= 1
        input_pos_y += 1
        if input_pos_x > 0 and input_pos_y <= MAX_BOUNDS:
            position = '{}{}'.format(number_alphabet_mapping[input_pos_x], input_pos_y)
            moves.append(position)
    return moves

def try_down_right(input_pos_x, input_pos_y):
    moves = []
    for x in range(1, input_pos_y):
        input_pos_x += 1
        input_pos_y -= 1
        if input_pos_x <= MAX_BOUNDS and input_pos_y > 0:
            position = '{}{}'.format(number_alphabet_mapping[input_pos_x], input_pos_y)
            moves.append(position)
    return moves

def try_down_left(input_pos_x, input_pos_y):
    moves = []
    for i in range(1, min(input_pos_x, input_pos_y)):
        input_pos_x -= 1
        input_pos_y -= 1
        position = '{}{}'.format(number_alphabet_mapping[input_pos_x], input_pos_y)
        moves.append(position)
    return moves

# helper for print, sort on numbers, not alphabetically
def sort_func(coordinate):
    return coordinate[1]

def print_moves(moves):
    moves.sort()
    print(','.join(sorted(moves, key=sort_func)))

# helper regex for argparser
def valid_spaces_regex(inp, test=re.compile(r"[a-h][1-8]")):
    if not test.match(inp):
        raise argparse.ArgumentTypeError
    return inp

# have to keep these global otherwise tests fail due to inaccessability
MAX_BOUNDS = 8
alphabet_number_mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
number_alphabet_mapping= dict(map(reversed, alphabet_number_mapping.items()))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This script can be used to determine possible moves for the Queen, Rook, or Knight on a chess board")
    parser.add_argument("-piece", help="Chess Piece to test", choices=['QUEEN', 'ROOK', 'KNIGHT'], required=True)
    parser.add_argument("-position", help="Algebraic notation for location on chess board ie: a8", type=valid_spaces_regex, required=True)
    args = parser.parse_args()

    piece = args.piece
    input_position = args.position

    # map letter to a numeric y value
    initial_pos_x = alphabet_number_mapping[input_position[0]]

    initial_pos_y = int(input_position[1])

    if piece == 'KNIGHT':
        print_moves(calc_moves_knight(initial_pos_x, initial_pos_y))
    elif piece =='ROOK':
        print_moves(calc_moves_rook(initial_pos_x, initial_pos_y))
    else:
        print_moves(calc_moves_queen(initial_pos_x, initial_pos_y))


