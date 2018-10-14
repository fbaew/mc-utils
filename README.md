# Minecraft Utilities

Collection of various tools for doing interesting things with a minecraft server.

## texture.py

This tool munges several resource/texture packs into one mutant one suitable
for consumption by `overviewer.py` ([website](https://overviewer.org)).

The general operation of `TextureRectifier` is to enumerate the keys in `self.items`, 
and move the textures associates with the named object from one place to another. 

Earlier (?) versions of Minecraft used a totally flat texture folder (no
subfolders), while later (?) versions  group related objects in their own
subfolder -- for example, all `door` textures are now within
`/textures/blocks/door/`, as there are now distinct textures for doors made
from different types of wood.
