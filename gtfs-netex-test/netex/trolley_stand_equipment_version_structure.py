from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from netex.payment_method_enumeration import PaymentMethodEnumeration
from netex.site_equipment_version_structure import SiteEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrolleyStandEquipmentVersionStructure(SiteEquipmentVersionStructure):
    """
    Type for a Trolley Stand EQUIPMENT.

    :ivar free_to_use: Whether Trolley is free or if a payment is
        required.
    :ivar charge: Charge for using a trolley.
    :ivar currency: Currency of Charge for using the facility.
    :ivar payment_methods: Allowed methods of payment.
    """
    class Meta:
        name = "TrolleyStandEquipment_VersionStructure"

    free_to_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FreeToUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    charge: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Charge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
        }
    )
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
