from pathlib import Path

from pytiled_parser import common_types, layer, tiled_map, tileset

EXPECTED = tiled_map.Map(
    hex_side_length=6,
    stagger_axis="y",
    stagger_index="odd",
    infinite=False,
    layers=[
        layer.TileLayer(
            name="Tile Layer 1",
            opacity=1,
            visible=True,
            size=common_types.Size(10, 10),
            id=1,
            data=[
                3,
                3,
                3,
                3,
                9,
                9,
                9,
                9,
                17,
                17,
                3,
                3,
                3,
                9,
                9,
                9,
                9,
                17,
                17,
                17,
                3,
                3,
                3,
                9,
                9,
                9,
                9,
                9,
                17,
                17,
                3,
                3,
                1,
                7,
                9,
                9,
                9,
                15,
                17,
                17,
                1,
                1,
                12,
                5,
                7,
                7,
                7,
                15,
                15,
                15,
                12,
                1,
                5,
                5,
                7,
                7,
                7,
                15,
                15,
                15,
                2,
                2,
                5,
                5,
                5,
                5,
                4,
                14,
                14,
                14,
                2,
                2,
                5,
                5,
                5,
                4,
                14,
                14,
                14,
                14,
                2,
                2,
                2,
                5,
                5,
                5,
                4,
                14,
                14,
                14,
                2,
                2,
                2,
                2,
                5,
                5,
                4,
                4,
                14,
                14,
            ],
        )
    ],
    map_size=common_types.Size(10, 10),
    next_layer_id=2,
    next_object_id=1,
    orientation="hexagonal",
    render_order="right-down",
    tiled_version="1.4.1",
    tile_size=common_types.Size(14, 12),
    version=1.4,
    tilesets={
        1: tileset.TileSet(
            columns=5,
            image=Path("../../images/hexmini.png"),
            image_width=106,
            image_height=72,
            margin=0,
            spacing=0,
            name="tileset",
            tile_count=20,
            tiled_version="1.4.1",
            tile_height=18,
            tile_width=18,
            version=1.4,
            type="tileset",
            tile_offset=common_types.OrderedPair(0, 1),
        )
    },
)