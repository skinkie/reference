from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.customer_service_version_structure import CustomerServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LeftLuggageServiceVersionStructure(CustomerServiceVersionStructure):
    """
    Type for a LEFT LUGGAGE SERVICE.

    :ivar counter_service: Whether left luggage is a counter service.
    :ivar self_service_lockers: Whether there are self service lockers.
    :ivar fee_per_bag: Whether there is a fee per bag.
    :ivar locker_fee: Whether there is a locker fee.
    :ivar maximum_bag_width: Width of Locker.
    :ivar maximum_bag_height: Height of Locker.
    :ivar maximum_bag_depth: Depth of Locker.
    :ivar maximum_bag_weight: Maximum weight of the luggage. +v1.1
    :ivar maximum_duration: Maximum time for which luggage can be left.
        +V1.1
    """
    class Meta:
        name = "LeftLuggageService_VersionStructure"

    counter_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CounterService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    self_service_lockers: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelfServiceLockers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fee_per_bag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FeePerBag",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    locker_fee: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LockerFee",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_bag_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_bag_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_bag_depth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagDepth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_bag_weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumBagWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
