from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FixedStartWindowStructure:
    """
    Type for Fiexd Start WIndow.

    :ivar maximum_services_before: If UsageStartConstraintType is
        "fixedWindow", maximum number of services before the booked
        train that may also be used. +v1.1
    :ivar flexible_period_before: If UsageStartConstraintType is
        "fixedWindow", maximum period before the booked train during
        which other trains may also be caught. +v1.1
    :ivar maximum_services_after: If UsageStartConstraintType is
        "fixedWindow", maximum number of services after the booked train
        that may also be used. +v1.1
    :ivar flexible_period_after: If UsageStartConstraintType is
        "fixedWindow", maximum period after the booked train during
        which other trains may also be caught. +v1.1
    """
    maximum_services_before: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumServicesBefore",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_period_before: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FlexiblePeriodBefore",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_services_after: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumServicesAfter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_period_after: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FlexiblePeriodAfter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
