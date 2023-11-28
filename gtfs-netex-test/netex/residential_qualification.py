from dataclasses import dataclass, field
from netex.residential_qualification_version_structure import ResidentialQualificationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResidentialQualification(ResidentialQualificationVersionStructure):
    """
    The number and characteristics (weight, volume) of luggage that a holder of an
    access right is entitled to carry.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
