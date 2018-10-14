from os import path 
from shutil import copy as fscopy


class TextureRectifier:
    """
    Provides cross-compatibility between different versions of minecraft
    texture organization and naming conventions. Different object types can be
    defined in self.items, and depending on what keys are present in the
    definition, different file path and name templates are evaluated.
    """


    def __init__(self, target_pack, pack_priority):

        self.resource_root = '/mnt/mcserver/resource'
        self.default_texture = 'default.png'
        self.packs = pack_priority
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
            'fire': {
                'stages': 2,
                'stage_format': lambda obj, stage: '{}_layer_{}.png'.format(obj, stage)
            },
            'frosted_ice': {
                'stages': 4,
                'stage_format': lambda obj, stage: '{}_{}.png'.format(obj, stage)
            },
            'beetroots': {
                'stages': 4,
                'stage_format': lambda obj, stage: '{}_stage_{}.png'.format(obj, stage)
            },
            'potatoes': {
                'stages': 4,
                'stage_format': lambda obj, stage: '{}_stage_{}.png'.format(obj, stage)
            },
            'cocoa': {
                'stages': 3,
                'stage_format': lambda obj, stage: '{}_stage_{}.png'.format(obj, stage)
            },

           'carrots': {
                'stages': 4,
                'stage_format': lambda obj, stage: '{}_stage_{}.png'.format(obj, stage)
            },
           'nether_wart': {
                'stages': 3,
                'stage_format': lambda obj, stage: '{}_stage_{}.png'.format(obj, stage)
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
                    'black',
                    'blue',
                    'brown',
                    'cyan',
                    'gray',
                    'green',
                    'light_blue',
                    'lime',
                    'magenta',
                    'orange',
                    'pink',
                    'purple',
                    'red',
                    'silver',
                    'white',
                    'yellow'
                ],
                'src_format': lambda color: 'concrete_' + color + '.png',
                'dest_format': lambda obj, color: '_'.join(
                    [obj, color]
                ) + '.png'
            },
            'concrete_powder': {
                'colors': [
                    'black',
                    'blue',
                    'brown',
                    'cyan',
                    'gray',
                    'green',
                    'light_blue',
                    'lime',
                    'magenta',
                    'orange',
                    'pink',
                    'purple',
                    'red',
                    'silver',
                    'white',
                    'yellow'
                ],
                'src_format': lambda color: 'concrete_powder_' + color + '.png',
                'dest_format': lambda obj, color: '_'.join(
                    [obj, color]
                ) + '.png'
            },

            '_simple': [
                'dirt_podzol_side',
                'dirt_podzol_top',
                'iron_trapdoor',
                'water_still',
                'rail_normal_turned',
                'repeater_off',
                'repeater_on',
                'redstone_torch_off',
                'redstone_torch_on',
                'redstone_lamp_on',
                'redstone_lamp_off',
                'trapdoor',
                'iron_bars',
                'dropper_front_horizontal',
                'dropper_front_vertical',
                'dispenser_front_horizontal',
                'dispenser_front_vertical',
                'chorus_plant',
                'jukebox_top',
                'noteblock',
                'lever',
                'prismarine_dark',
                'prismarine_rough',
                'comparator_on',
                'comparator_off',
                'magma',
                'mushroom_block_skin_brown',
                'mushroom_block_skin_stem',
                'mushroom_block_inside',
                'mushroom_block_skin_red',
                'mushroom_red',
                'mushroom_brown',
                'quartz_block_chiseled_top',
                'quartz_block_chiseled',
                'command_block_front',
                'command_block_side',
                'command_block_back',
                'chain_command_block_conditional',
                'chain_command_block_front',
                'chain_command_block_back',
                'chain_command_block_side',
                'repeating_command_block_front',
                'repeating_command_block_back',
                'repeating_command_block_conditional',
                'repeating_command_block_side',
                'farmland_wet',
                'farmland_dry',
                'lava_still',
                'portal',
                'beacon',
                'hay_block_top',
                'hay_block_side',
                'dragon_egg',
                'observer_front',
                'observer_top',
                'observer_back',
                'observer_back_lit',
                'observer_side',
                'chorus_flower',
                'chorus_flower_dead',
                'flower_rose',
                'flower_dandelion',
                'flower_blue_orchid',
                'flower_allium',
                'flower_pot',
                'flower_dandelion_pot',
                'flower_paeonia',
                'flower_tulip_pink',
                'flower_tulip_white',
                'flower_tulip_orange',
                'flower_tulip_red',
                'flower_oxeye_daisy',
                'flower_rose_pot',
                'flower_rose',
                'flower_houstonia',
                'flower_oxeye_daisy',
                'bone_block_side',
                'bone_block_top',
                'melon_stem_disconnected',
                'melon_stem_connected',
                'double_plant_fern_top',
                'double_plant_sunflower_front',
                'double_plant_sunflower_bottom',
                'double_plant_sunflower_back',
                'double_plant_paeonia_bottom',
                'double_plant_sunflower_top',
                'double_plant_syringa_bottom',
                'double_plant_paeonia_top',
                'double_plant_rose_top',
                'double_plant_fern_bottom',
                'double_plant_syringa_top',
                'double_plant_rose_bottom',
                'double_plant_grass_top',
                'double_plant_grass_bottom',
                'daylight_detector_inverted_top',
                'daylight_detector_top',
                'daylight_detector_side',
                'bookshelf',
                'nether_wart_block',
                'hopper_top',
                'hopper_outside',
                'hopper_inside',
                'stonebrick_carved'
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
                path.join('blocks', filename) + '.png',
                path.join('blocks', filename) + '.png'
            )

        self.collect_complex_assets()


    def copy_asset(self, asset_path, dest_path):
        current_pack = 0
        dest_item = None
        source_item = None
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

        """
        Ignoring the simple items (i.e. resources where the relative path structure
        does not change from source to target), attempt to identify each minecraft object
        class defined, and construct the appropriate source and destination paths for
        the associated textures/resources.

        """
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
            elif 'stages' in self.items[item]:
                for stage in range(self.items[item]['stages']):
                    args = [item, stage]
                    self.copy_asset(
                        path.join('blocks', self.items[item]['stage_format'](*args)),
                        path.join('blocks', self.items[item]['stage_format'](*args))
                    )
    

def main():
    rectifier = TextureRectifier('capri', pack_priority=['sapix', 'soartex'])
    rectifier.populate_missing()


if __name__ == '__main__':
    main()
