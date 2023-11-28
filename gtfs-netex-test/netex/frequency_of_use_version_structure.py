from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.discount_basis_enumeration import DiscountBasisEnumeration
from netex.frequency_of_use_type_enumeration import FrequencyOfUseTypeEnumeration
from netex.time_interval_ref import TimeIntervalRef
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FrequencyOfUseVersionStructure(UsageParameterVersionStructure):
    """
    Type for FREQUENCY OF USE.

    :ivar frequency_of_use_type: Nature of FREQUENCY OF USE Transfers.
    :ivar minimal_frequency: Minimum number of times product can be
        used.
    :ivar maximal_frequency: Maximum number of times  product can be
        used.
    :ivar frequency_interval: Interval within which frequency is
        measured. If absent forever.
    :ivar time_interval_ref:
    :ivar discount_basis: Nature of discount for this profile.
    """
    class Meta:
        name = "FrequencyOfUse_VersionStructure"

    frequency_of_use_type: Optional[FrequencyOfUseTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FrequencyOfUseType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimal_frequency: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinimalFrequency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximal_frequency: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximalFrequency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frequency_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FrequencyInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_interval_ref: Optional[TimeIntervalRef] = field(
        default=None,
        metadata={
            "name": "TimeIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    discount_basis: Optional[DiscountBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "DiscountBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
