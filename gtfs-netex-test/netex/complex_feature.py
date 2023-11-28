from dataclasses import dataclass, field
from netex.complex_feature_version_structure import ComplexFeatureVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ComplexFeature(ComplexFeatureVersionStructure):
    """
    An aggregate of SIMPLE FEATUREs and/or other COMPLEX FEATUREs; e.g. a STOP AREA
    : combination of STOP POINTs ; a train station : combination of SIMPLE FEATUREs
    (POINTs, LINKs) and COMPLEX FEATUREs (STOP AREAs).

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
