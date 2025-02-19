#! /usr/bin/env python

from pprint import pprint as pp
import json

def get_data():
    with open('keymap.layout') as f:
        layers = []
        for i, segment in enumerate(f.read().split('layer')[1:]):
            segs = []
            for line in filter(lambda l: not l.startswith('|-'), segment.split('\n')):
                segs += [list(filter(None, line.replace(' ', '').split('|')))]
            layers += [segs[1:-1]]
            print('{} keys defined in layer {}'.format(sum(map(len, segs[1:-1])), i))
    return layers

def write_data(layers):
    with open('layers.json', 'w') as f:
        rows = json.dumps({'layers': [['{}'.format(', '.join(row)) for row in rows] for rows in layers]}, indent=2)
        f.write(rows.replace(', ', '", "'))

def main():
    layers = get_data()
    write_data(layers)

if __name__ == '__main__':
    main()
