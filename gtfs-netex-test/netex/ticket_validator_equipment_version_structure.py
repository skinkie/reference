from dataclasses import dataclass, field
from typing import List, Optional
from netex.multilingual_string import MultilingualString
from netex.passenger_equipment_version_structure import PassengerEquipmentVersionStructure
from netex.ticket_validator_enumeration import TicketValidatorEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TicketValidatorEquipmentVersionStructure(PassengerEquipmentVersionStructure):
    """
    Type for a TICKET VALIDATOR EQUIPMENT.

    :ivar ticket_validator_type: Types of validation supported by
        validator.
    :ivar audio_validation_feedback: Whether there is audio validation
        feedback.+v1.1.
    :ivar visual_validation_feedback: Whether there is visual validation
        feedback. +v1.1.
    :ivar tactile_validation_feedback: Whether there is tactical
        validation feedback.+v1.1.
    :ivar validation_guidance: Free text describing use of validator
        (how title may be presented, how to find validator, etc.).
        +v1.1.
    """
    class Meta:
        name = "TicketValidatorEquipment_VersionStructure"

    ticket_validator_type: List[TicketValidatorEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketValidatorType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    audio_validation_feedback: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AudioValidationFeedback",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    visual_validation_feedback: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VisualValidationFeedback",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tactile_validation_feedback: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileValidationFeedback",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validation_guidance: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ValidationGuidance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
