from dataclasses import dataclass, field
from netex.level_version_structure import LevelVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Level(LevelVersionStructure):
    """An identified storey (ground, first, basement, mezzanine, etc) within an
    interchange building or SITE on which SITE COMPONENTs reside.

    A PATH LINK may connect components on different levels.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
