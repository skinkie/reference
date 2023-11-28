from dataclasses import dataclass
from netex.ticket_validator_equipment_ref_structure import TicketValidatorEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TicketValidatorEquipmentRef(TicketValidatorEquipmentRefStructure):
    """
    Identifier of a TICKET VALIDATOR.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
