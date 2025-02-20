#! /usr/bin/env python

import sys
import json

def get_layout():
    with open('keymap.layout') as f:
        layers = []
        for i, segment in enumerate(f.read().split('layer')[1:]):
            segs = []
            for line in filter(lambda l: not l.startswith('|-'), segment.split('\n')):
                segs += [list(filter(None, line.replace(' ', '').split('|')))]
            layers += [segs[1:-1]]
            print('{} keys defined in layer {}'.format(sum(map(len, segs[1:-1])), i))
    return layers

def get_keymap():
    with open('keymap.json') as f:
        return json.load(f).get('layers', [[]])

def write_keymap(layers: list) -> None:
    with open('layers.json', 'w') as f:
        rows = json.dumps({'layers': [['{}'.format(', '.join(row)) for row in rows] for rows in layers]}, indent=2)
        f.write(rows.replace(', ', '", "'))

def write_layout(keys: list) -> None:
    empty = '| | |\n'
    layer_break = lambda i: '| layer | {} |\n'.format(i)
    line_break = '|--|--|\n'
    row_indices = list(range(0, 42, 12))
    rows_from_layer = lambda l: zip([l[i:i+12] for i in row_indices])
    with open('keymap.layout.out', 'w') as f:
        f.write(empty + line_break)
        for i, layer in enumerate(keys):
            f.write(layer_break(i) + line_break)
            for j, row in enumerate(rows_from_layer(layer)):
                row = row[0]
                print('row:', row)
                if j == 3:
                    row = [''] * 3 + row + [''] * 3
                    f.write('| {} | '.format(' |'.join(row[:6])))
                    f.write(' | {} |\n'.format(' |'.join(row[6:])))
                    f.write(line_break)
                else:
                    f.write('| {} |'.format(' |'.join(row[:6])))
                    f.write(' | {} |\n'.format(' |'.join(row[6:])))
                    f.write(line_break)

def main():
    if sys.argv[1:] == ['make-keymap']:
        layers = get_layout()
        write_keymap(layers)
    elif sys.argv[1:] == ['make-layout']:
        keys = get_keymap()
        write_layout(keys)
    else:
        print('options are:\n\tmake-keymap\n\tmake-layout')
        print('not: ', *sys.argv[1:])

if __name__ == '__main__':
    main()
