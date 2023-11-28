from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from netex.purchase_action_enumeration import PurchaseActionEnumeration
from netex.purchase_moment_enumeration import PurchaseMomentEnumeration
from netex.purchase_when_enumeration import PurchaseWhenEnumeration
from netex.time_interval_ref_structure import TimeIntervalRefStructure
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PurchaseWindowVersionStructure(UsageParameterVersionStructure):
    """
    Type for PURCHASE WINDOW.

    :ivar purchase_action: Action governed by Purchase Window. default
        is purchase. See allowed values.+v1.1
    :ivar purchase_when: When ticket can be purchased. See allowed
        values.
    :ivar latest_time: Latest time on specified last day when ticket
        can be purchased.
    :ivar minimum_period_before_departure: Minimum period before
        departure that purchase must be made.
    :ivar minimum_period_interval_ref: Minimum period before departure
        that purchase must be made - as arbitrary interval.
    :ivar maximum_period_before_departure: Maximum period before
        departure that purchase can be made.
    :ivar maximum_period_interval_ref: Maximum period before departure
        that purchase must be made - as arbitrary interval.
    :ivar purchase_moment: Permitted  moments of purchase. See allowed
        values +v1.1
    """
    class Meta:
        name = "PurchaseWindow_VersionStructure"

    purchase_action: Optional[PurchaseActionEnumeration] = field(
        default=None,
        metadata={
            "name": "PurchaseAction",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purchase_when: Optional[PurchaseWhenEnumeration] = field(
        default=None,
        metadata={
            "name": "PurchaseWhen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    latest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LatestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_period_before_departure: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumPeriodBeforeDeparture",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_period_interval_ref: Optional[TimeIntervalRefStructure] = field(
        default=None,
        metadata={
            "name": "MinimumPeriodIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_period_before_departure: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumPeriodBeforeDeparture",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_period_interval_ref: Optional[TimeIntervalRefStructure] = field(
        default=None,
        metadata={
            "name": "MaximumPeriodIntervalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purchase_moment: List[PurchaseMomentEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseMoment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
