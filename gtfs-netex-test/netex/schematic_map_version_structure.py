from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.multilingual_string import MultilingualString
from netex.schematic_map_members_rel_structure import SchematicMapMembersRelStructure
from netex.version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SchematicMapVersionStructure(DataManagedObjectStructure):
    """
    Type for a SCHEMATIC MAP.

    :ivar name: Name of SCHEMATIC MAP.
    :ivar short_name: Short Name.
    :ivar image_uri: image for map.
    :ivar depicted_object_ref: Parent Entity for map that is depicted by
        it , e.g. a Station, Site,o, Line or Line group.
    :ivar members: Elements found in SCHEMATIC MAP.
    """
    class Meta:
        name = "SchematicMap_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    image_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImageUri",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    depicted_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "DepictedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    members: Optional[SchematicMapMembersRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
