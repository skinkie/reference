from dataclasses import dataclass, field
from netex.residential_qualification_eligibility_versioned_child_structure import ResidentialQualificationEligibilityVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResidentialQualificationEligibility(ResidentialQualificationEligibilityVersionedChildStructure):
    """
    Whether a specific TRANSPORT CUSTOMER is eligible for a FARE PRODUCT with a
    specific RESIDENTIAL QUALIFICATION as a validity parameter.

    :ivar id: Identifier of RESIDENTIAL QUALIFICATION ELIGIBILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
