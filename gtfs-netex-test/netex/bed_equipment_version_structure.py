from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .bed_type_enumeration import BedTypeEnumeration
from .spot_equipment_version_structure import SpotEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BedEquipmentVersionStructure(SpotEquipmentVersionStructure):
    class Meta:
        name = "BedEquipment_VersionStructure"

    bed_type: Optional[BedTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "BedType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_stowable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsStowable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    headroom: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Headroom",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bed_length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BedLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
