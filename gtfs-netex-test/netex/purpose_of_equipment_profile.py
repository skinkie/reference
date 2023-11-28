from dataclasses import dataclass, field
from netex.purpose_of_equipment_profile_value_structure import PurposeOfEquipmentProfileValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PurposeOfEquipmentProfile(PurposeOfEquipmentProfileValueStructure):
    """
    A functional purpose which requires a certain set of EQUIPMENT of different
    types put together in a VEHICLE EQUIPMENT PROFILE or STOP POINT EQUIPMENT
    PROFILE.

    :ivar id: Identifier of PURPOSE OF EQUIMENT PROFILE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
