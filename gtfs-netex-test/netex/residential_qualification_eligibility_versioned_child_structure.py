from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from netex.customer_eligibility_versioned_child_structure import CustomerEligibilityVersionedChildStructure
from netex.residence_type_enumeration import ResidenceTypeEnumeration
from netex.residential_qualification_ref import ResidentialQualificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResidentialQualificationEligibilityVersionedChildStructure(CustomerEligibilityVersionedChildStructure):
    """
    Type for RESIDENTIAL QUALIFICATION ELIGIBILITY.

    :ivar residential_qualification_ref:
    :ivar residency_type: Type of Residency. +v1.1
    :ivar start_date: Date residence started. +v1.1
    :ivar end_date: Date residence started +v1.1.
    """
    class Meta:
        name = "ResidentialQualificationEligibility_VersionedChildStructure"

    residential_qualification_ref: Optional[ResidentialQualificationRef] = field(
        default=None,
        metadata={
            "name": "ResidentialQualificationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    residency_type: Optional[ResidenceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ResidencyType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
