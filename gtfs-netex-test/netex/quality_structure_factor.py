from dataclasses import dataclass, field
from netex.quality_structure_factor_version_structure import QualityStructureFactorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class QualityStructureFactor(QualityStructureFactorVersionStructure):
    """
    The value of a QUALITY INTERVAL or a DISTANCE MATRIX ELEMENT expressed by a
    QUALITY UNIT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
