from dataclasses import dataclass, field
from typing import List, Optional
from netex.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.machine_readable_enumeration import MachineReadableEnumeration
from netex.media_type_enumeration import MediaTypeEnumeration
from netex.type_of_entity_version_structure import TypeOfEntityVersionStructure
from netex.types_of_machine_readabilities_rel_structure import TypesOfMachineReadabilitiesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfTravelDocumentVersionStructure(TypeOfEntityVersionStructure):
    """
    Type for TYPE OF TRAVEL DOCUMENT.

    :ivar is_card: Whether  the  MACHINE READABILITY is a card.
    :ivar is_smart_card: Whether  the  MACHINE READABILITY can contain
        applications and or stored value.
    :ivar has_photo: Whether the  MACHINE READABILITY has a photo.
    :ivar media_type: Classification of the MACHINE READABILITY by Media
        Type.
    :ivar machine_readable: Classification of the MACHINE READABILITY by
        Machine Readable mechanism.
    :ivar types_of_machine_readabilities: Openended classiifcation of
        machine readable capabilties compatible with TRAVEL DOCUMENT.
    :ivar alternative_names: ALTERNATIVE NAMES for MACHINE READABILITY.
    """
    class Meta:
        name = "TypeOfTravelDocument_VersionStructure"

    is_card: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCard",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_smart_card: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSmartCard",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_photo: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasPhoto",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    media_type: Optional[MediaTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "MediaType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    machine_readable: List[MachineReadableEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "MachineReadable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    types_of_machine_readabilities: Optional[TypesOfMachineReadabilitiesRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfMachineReadabilities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
