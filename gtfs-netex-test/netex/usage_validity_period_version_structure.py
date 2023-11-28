from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDuration, XmlTime
from netex.activation_means_enumeration import ActivationMeansEnumeration
from netex.alternative_texts_rel_structure import DayTypesRelStructure
from netex.blackout_start_enumeration import BlackoutStartEnumeration
from netex.fixed_start_window_structure import FixedStartWindowStructure
from netex.usage_end_enumeration import UsageEndEnumeration
from netex.usage_parameter_version_structure import UsageParameterVersionStructure
from netex.usage_start_constraint_type_enumeration import UsageStartConstraintTypeEnumeration
from netex.usage_trigger_enumeration import UsageTriggerEnumeration
from netex.usage_validity_type_enumeration import UsageValidityTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UsageValidityPeriodVersionStructure(UsageParameterVersionStructure):
    """
    Type for USAGE VALIDITY PERIOD.

    :ivar validity_period_type: Nature of USAGE VALIDITY PERIOD.
    :ivar usage_trigger: Event triggering usage period.
    :ivar usage_end: Event triggering end of usage period.
    :ivar standard_duration: Duration of  USAGE VALIDITY PERIOD.
    :ivar activation_means: Means of activatiing start of period.
    :ivar start_date: Start date of  USAGE VALIDITY PERIOD.
    :ivar start_time: Start time of  USAGE VALIDITY PERIOD.
    :ivar end_date: End Date of  USAGE VALIDITY PERIOD.
    :ivar end_time: End time of  USAGE VALIDITY PERIOD.
    :ivar usage_start_constraint_type: Whether start type of trip or
        pass  is  variable or fixed. +v1.1
    :ivar start_only_on: If UsageStartConstraintType is "fixed", then
        allowed days to start on can be indicated by a DAY TYPE, for
        example Monday, 1st of Month, Start of Quarter, etc. (Applies
        mainly  to Passes.)
    :ivar fixed_start_window: If UsageStartConstraintType is
        "fixedWindow" , then can specify a window relative to booked
        train for alternative services that may be used. +v1.1
    :ivar blackout_use: Interaction with blackout periods.
    """
    class Meta:
        name = "UsageValidityPeriod_VersionStructure"

    validity_period_type: Optional[UsageValidityTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ValidityPeriodType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_trigger: Optional[UsageTriggerEnumeration] = field(
        default=None,
        metadata={
            "name": "UsageTrigger",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_end: Optional[UsageEndEnumeration] = field(
        default=None,
        metadata={
            "name": "UsageEnd",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    standard_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_means: Optional[ActivationMeansEnumeration] = field(
        default=None,
        metadata={
            "name": "ActivationMeans",
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
    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
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
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_start_constraint_type: Optional[UsageStartConstraintTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "UsageStartConstraintType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_only_on: Optional[DayTypesRelStructure] = field(
        default=None,
        metadata={
            "name": "startOnlyOn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fixed_start_window: Optional[FixedStartWindowStructure] = field(
        default=None,
        metadata={
            "name": "FixedStartWindow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    blackout_use: Optional[BlackoutStartEnumeration] = field(
        default=None,
        metadata={
            "name": "BlackoutUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
