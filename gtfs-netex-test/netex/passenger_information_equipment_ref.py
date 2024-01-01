from dataclasses import dataclass
from .passenger_information_equipment_ref_structure import (
    PassengerInformationEquipmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerInformationEquipmentRef(
    PassengerInformationEquipmentRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
