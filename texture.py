from os import path, listdir
from shutil import copy as fscopy


class TextureRectifier:


    def __init__(self, source_pack, target_pack):

        self.resource_root = '/mnt/mcserver/resource'
        self.default_texture = 'default.png'
        self.packs = ['sapix', 'soartex']
        self.source = source_pack
        self.target = target_pack

        self.texture_path = path.join(
            'assets', 'minecraft', 'textures'
        )

        self.items = {
            'door': {
                'materials': [
                    'birch',
                    'jungle',
                    'dark_oak',
                    'acacia',
                    'iron',
                    'spruce',
                    'wood'
                ],
                'parts': ['lower', 'trim', 'upper'],
                'dest_format': lambda obj, material, part: '_'.join(
                    [obj,material, part]
                ) + '.png'
            },
            'terracotta': {
                'colors': [
                    'black',
                    'brown',
                    'gray',
                    'light_blue',
                    'magenta',
                    'pink',
                    'red',
                    'white',
                    'blue',
                    'cyan',
                    'green',
                    'lime',
                    'orange',
                    'purple',
                    'silver',
                    'yellow'
                ],
                'src_format': lambda color: color + '.png',
                'dest_format': lambda obj, color: '_'.join(
                    ['glazed', obj, color]
                ) + '.png'
            },
            'concrete': {
                'colors': [
                    'silver'
                ],
                'src_format': lambda color: 'concrete_' + color + '.png',
                'dest_format': lambda obj, color: '_'.join(
                    [obj, color]
                ) + '.png'
            },
            '_simple': [
                'iron_trapdoor.png',
                'water_still.png',
                'rail_normal_turned.png',
                'potatoes_stage_0.png',
                'potatoes_stage_1.png',
                'potatoes_stage_2.png',
                'potatoes_stage_3.png',
                'cocoa_stage_0.png',
                'cocoa_stage_1.png',
                'cocoa_stage_2.png',
                'repeater_off.png',
                'redstone_torch_off.png',
                'trapdoor.png',
                'iron_bars.png',
                'dropper_front_horizontal.png',
                'dropper_front_vertical.png',
                'flower_rose.png',
                'chorus_plant.png',
                'jukebox_top.png',
                'noteblock.png'
            ]
        }

        self.block_texture_path = path.join(self.texture_path, 'blocks')

        self.search_paths = [
            path.join(
                self.resource_root, pack, self.texture_path
            ) for pack in self.packs
        ]


    def populate_missing(self):
        deficits = self.items['_simple']

        for filename in deficits:
            self.copy_asset(
                path.join('blocks', filename),
                path.join('blocks', filename)
            )

        self.collect_complex_assets()


    def copy_asset(self, asset_path, dest_path):
        current_pack = 0
        while current_pack < len(self.search_paths):
            try:
                source_item = path.join(
                    self.search_paths[current_pack],
                    asset_path
                )
                dest_item = path.join(
                    self.resource_root,
                    self.target,
                    self.texture_path,
                    dest_path
                )
                fscopy(source_item, dest_item)
                print('copied {} to {}'.format(source_item, dest_item))
                break
            except FileNotFoundError:
                current_pack += 1

        if current_pack == len(self.search_paths):
            print('ERROR: could not find file {}'.format(source_item))
            fscopy(self.default_texture, dest_item)

    def collect_complex_assets(self):
        filetype = '.png'
        args = []
        for item in self.items:
            if item == '_simple':
                continue

            if 'materials' in self.items[item]:

                for material in self.items[item]['materials']:
                    for part in self.items[item]['parts']:
                        args = [item, material, part]
                        source = path.join(
                            item, material, part) + filetype
                        self.copy_asset(
                            path.join('blocks', source),
                            path.join(
                                'blocks',
                                self.items[item]['dest_format'](*args)
                            )
                        )

            elif 'colors' in self.items[item]:
                for color in self.items[item]['colors']:
                    args = [item, color]
                    source = path.join(
                        item, self.items[item]['src_format'](color))
                    self.copy_asset(
                        path.join('blocks', source),
                        path.join(
                            'blocks',
                            self.items[item]['dest_format'](*args)
                        )
                    )


def main():
    rectifier = TextureRectifier('sapix', 'capri')
    rectifier.populate_missing()

if __name__ == '__main__':
    main()