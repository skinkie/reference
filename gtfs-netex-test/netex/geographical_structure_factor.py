from dataclasses import dataclass, field
from netex.geographical_structure_factor_version_structure import GeographicalStructureFactorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalStructureFactor(GeographicalStructureFactorVersionStructure):
    """
    The value of a GEOGRAPHICAL INTERVAL or a DISTANCE MATRIX ELEMENT expressed by
    a GEOGRAPHICAL UNIT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
