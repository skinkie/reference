from dataclasses import dataclass, field
from netex.personal_mode_of_operation_value_structure import PersonalModeOfOperationValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PersonalModeOfOperation(PersonalModeOfOperationValueStructure):
    """A non-advertised mode of operation of vehicles by persons using their own
    vehicle.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
