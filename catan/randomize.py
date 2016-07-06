'''Functions to unpack, format, and randomize a scenario.'''

from random import shuffle
import re

def randomize(scenario):
    '''Format and randomize a scenario stored in a dict.'''
    tile_deck = unpack_deck(scenario['tiles'])
    harbor_deck = unpack_deck(scenario['harbors'])
    tokens = unpack_tokens(scenario['tokens'], tile_deck)

    return format_board(scenario['board'], tile_deck, harbor_deck, tokens)

def unpack_deck(packed_deck):
    '''Unpack and randomize a tile or harbor deck.'''
    deck = sum([[k]*v for k, v in packed_deck.items()], [])
    shuffle(deck)
    return deck

def unpack_tokens(packed_tokens, tile_deck):
    '''Unpack a list of tokens/'''
    tokens = [int(token) for token in packed_tokens.split(',')]

    # add in blank number when tile is a desert
    for index, tile in enumerate(tile_deck):
        if tile == 'desert':
            tokens.insert(index, None)

    return tokens

def format_board(board, tile_deck, harbor_deck, tokens):
    '''Format a board given randomized decks and tokens.'''
    # replace blank tiles with tile deck
    for index, (token, tile) in enumerate(zip(tokens, tile_deck)):
        label = '{:s}{:02d}'.format(tile[0].upper(), token) if token else 'DES'
        board = board.replace('{:03d}'.format(index + 1), label, 1)

    # replace blank harbors with harbor deck
    harbor_tiles = re.findall(r'\.[←↖↗→↘↙]\.', board)
    for index, (harbor, tile) in enumerate(zip(harbor_deck, harbor_tiles)):
        label = '{:2s}{:s}'.format(tile[0:2], harbor[0].upper())
        board = board.replace(tile, label, 1)

    return board
