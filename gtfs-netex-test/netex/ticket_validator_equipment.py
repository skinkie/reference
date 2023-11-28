from dataclasses import dataclass, field
from netex.ticket_validator_equipment_version_structure import TicketValidatorEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TicketValidatorEquipment(TicketValidatorEquipmentVersionStructure):
    """
    Specialisation of INSTALLED EQUIPMENT describing a ticket validator.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
