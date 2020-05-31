# pylint: disable=too-few-public-methods

from pathlib import Path
from typing import Dict, List, NamedTuple, Optional, Union

import attr

from .common_types import Color, Size
from .layer import Layer
from .properties import Properties
from .tileset import TileSet

TileSetDict = Dict[int, TileSet]


@attr.s(auto_attribs=True)
class Map:
    """Object for storing a TMX with all associated layers and properties.

    See: https://doc.mapeditor.org/en/stable/reference/tmx-map-format/#map

    Attributes:
        parent_dir: The directory the TMX file is in. Used for finding relative paths
            to TSX files and other assets.
        version: The TMX format version.
        tiled_version: The Tiled version used to save the file. May be a date (for
            snapshot builds).
        orientation: Map orientation. Tiled supports "orthogonal", "isometric",
            "staggered" and "hexagonal"
        render_order: The order in which tiles on tile layers are rendered. Valid values
            are right-down, right-up, left-down and left-up. In all cases, the map is
            drawn row-by-row. (only supported for orthogonal maps at the moment)
        map_size: The map width in tiles.
        tile_size: The width of a tile.
        infinite: If the map is infinite or not.
        hex_side_length: Only for hexagonal maps. Determines the width or height
            (depending on the staggered axis) of the tile's edge, in pixels.
        stagger_axis: For staggered and hexagonal maps, determines which axis ("x" or
            "y") is staggered.
        stagger_index: For staggered and hexagonal maps, determines whether the "even"
            or "odd" indexes along the staggered axis are shifted.
        background_color: The background color of the map.
        next_layer_id: Stores the next available ID for new layers.
        next_object_id: Stores the next available ID for new objects.
        tile_sets: Dict of tile sets used in this map. Key is the first GID for the
            tile set. The value is a TileSet object.
        layers: List of layer objects by draw order.
    """

    parent_dir: Path
    tmx_file: Union[str, Path]

    version: str
    tiled_version: str
    orientation: str
    render_order: str
    map_size: Size
    tile_size: Size
    infinite: bool
    next_layer_id: Optional[int]
    next_object_id: int

    tile_sets: TileSetDict
    layers: List[Layer]

    hex_side_length: Optional[int] = None
    stagger_axis: Optional[int] = None
    stagger_index: Optional[int] = None
    background_color: Optional[Color] = None

    properties: Optional[Properties] = None


def parse() -> Map:
    pass