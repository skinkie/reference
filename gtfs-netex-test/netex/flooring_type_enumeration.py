from enum import Enum


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FlooringTypeEnumeration(Enum):
    CARPET = "carpet"
    CONCRETE = "concrete"
    ASPHALT = "asphalt"
    CORK = "cork"
    FIBREGLASS_GRATING = "fibreglassGrating"
    GLAZED_CERAMIC_TILES = "glazedCeramicTiles"
    PLASTIC_MATTING = "plasticMatting"
    CERAMIC_TILES = "ceramicTiles"
    RUBBER = "rubber"
    STEEL_PLATE = "steelPlate"
    VINYL = "vinyl"
    WOOD = "wood"
    STONE = "stone"
    GRASS = "grass"
    EARTH = "earth"
    GRAVEL = "gravel"
    UNEVEN = "uneven"
    UNKNOWN = "unknown"
    OTHER = "other"
