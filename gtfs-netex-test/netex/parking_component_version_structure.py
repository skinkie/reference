from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.multilingual_string import MultilingualString
from netex.site_component_version_structure import SiteComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingComponentVersionStructure(SiteComponentVersionStructure):
    """
    Type for a PARKING COMPONENT.

    :ivar parking_payment_code: Payment Code associated with PARKING
        COMPONENT.
    :ivar label: Additional Label of PARKING COMPONENT.
    :ivar maximum_length: Maximum length of VEHICLE that can use PARKING
        COMPONENT.
    :ivar maximum_width: Maximum width of VEHICLE that can use PARKING
        COMPONENT.
    :ivar maximum_height: Maximum height of VEHICLE that can use PARKING
        COMPONENT.
    :ivar maximum_weight: Maximum weight of VEHICLE to use PARKING AREA.
    """
    class Meta:
        name = "ParkingComponent_VersionStructure"

    parking_payment_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParkingPaymentCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
