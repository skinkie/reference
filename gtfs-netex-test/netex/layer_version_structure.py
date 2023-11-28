from dataclasses import dataclass, field
from typing import Optional
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.object_refs_rel_structure import ObjectRefsRelStructure
from netex.version_frame_refs_rel_structure import VersionFrameRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LayerVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for  LAYER.

    :ivar location_system: Reference to a PURPOSE OF GROUPING.
    :ivar version_frames: Members of  GROUP OF ENTITies.
    :ivar members: Members of  GROUP OF ENTITies.
    """
    class Meta:
        name = "Layer_VersionStructure"

    location_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationSystem",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    version_frames: Optional[VersionFrameRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "versionFrames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    members: Optional[ObjectRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
