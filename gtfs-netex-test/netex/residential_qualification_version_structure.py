from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.multilingual_string import MultilingualString
from netex.residence_type_enumeration import ResidenceTypeEnumeration
from netex.topographic_place_ref import TopographicPlaceRef
from netex.usage_parameter_ref_structure import UsageParameterRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResidentialQualificationVersionStructure(VersionedChildStructure):
    """
    Type for RESIDENTIAL QUALIFICATION.

    :ivar name: Name of RESIDENTIAL QUALIFICATIO.
    :ivar description: Description of RESIDENTIAL QUALIFICATIO.
    :ivar parent_ref: Parent USER PROFILE  or GROUP TICKET for which
        this  specifes the member rules.
    :ivar must_reside: Whthere the user must reside or must not reside
        in given place.
    :ivar topographic_place_ref:
    :ivar residence_type: Classifcation of type of residence required,
        e.g. live, work, study.
    :ivar minimum_duration: Minimum period of residency needed to
        qualify.
    """
    class Meta:
        name = "ResidentialQualification_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parent_ref: Optional[UsageParameterRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    must_reside: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MustReside",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_place_ref: Optional[TopographicPlaceRef] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    residence_type: Optional[ResidenceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ResidenceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
