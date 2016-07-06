'''Functions to produce a visual plot of a board.'''

import re
from math import sin, cos, pi
import matplotlib.pyplot as plt
import pandas as pd

CMAP = {'.':'lightblue', 'H':'firebrick', 'P':'lightgreen', 'M':'grey', 'F':'gold', 'W':'darkgreen',
        'D':'khaki', '3':'black', 'G':'black'}
ANGLES = {'→': 0, '↗': pi*1/3, '↖': pi*2/3, '←': pi, '↙': pi*4/3, '↘': pi*5/3}

def board_to_coords(board):
    '''Convert a board to a pandas DataFrame of coordinates and features.'''
    for y_index, line in enumerate(board.split('\n')): # for each row
        tiles = line.split()
        x_pad = len(re.match(r'^\s*', line).group(0))/4

        for x_index, tile in enumerate(tiles): # for each tile in the row
            is_tokened = re.match(r'\d', tile[1])
            is_harbor = tile[1] in ANGLES
            x_pos = x_index + x_pad
            y_pos = -y_index

            yield {'tile':  tile,
                   'x':     x_pos,
                   'y':     y_pos,
                   'color': CMAP[tile[0]],
                   'label': int(tile[1:]) if is_tokened else '',
                   'is_harbor':    is_harbor,
                   'harbor_x':     x_pos + cos(ANGLES[tile[1]])*0.3 if is_harbor else None,
                   'harbor_y':     y_pos + sin(ANGLES[tile[1]])*0.3 if is_harbor else None,
                   'harbor_color': CMAP[tile[2]] if is_harbor else None}

def show_board(board):
    '''Produce an image representation of a board.'''
    tiles = pd.DataFrame(board_to_coords(board))

    fig = plt.figure(figsize=(max(tiles['x'])/1.4, -min(tiles['y'])/1.6))

    # plot tiles
    plt.scatter(tiles['x'], tiles['y'], color=tiles['color'], marker='h', s=1000, lw=0)

    # plot tile labels
    for _, row in tiles.iterrows():
        plt.text(row['x'], row['y'], row['label'], color='white', size=14, ha='center', va='center')

    # plot harbors
    harbors = tiles[tiles['is_harbor']]
    plt.scatter(harbors['harbor_x'], harbors['harbor_y'], c=harbors['harbor_color'], s=100, lw=0)

    plt.axis('off')
    plt.show()
