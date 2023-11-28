from dataclasses import dataclass, field
from typing import List, Optional, Type
from netex.class_ref_structure import ClassRefStructure
from netex.classes_in_repository_rel_structure import ClassesInRepositoryRelStructure
from netex.layer_ref import LayerRef
from netex.modification_set_enumeration import ModificationSetEnumeration
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_entity_refs_rel_structure import TypeOfEntityRefsRelStructure
from netex.type_of_entity_version_structure import TypeOfEntityVersionStructure
from netex.type_of_frame_ref import TypeOfFrameRef
from netex.type_of_validity_ref import TypeOfValidityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypesOfFrameRelStructure(OneToManyRelationshipStructure):
    """
    A collection of one or more TYPEs OF VERSION FRAME.
    """
    class Meta:
        name = "typesOfFrame_RelStructure"

    type_of_frame_ref_or_type_of_frame: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfFrameRef",
                    "type": TypeOfFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFrame",
                    "type": Type["TypeOfFrame"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFrameValueStructure(TypeOfEntityVersionStructure):
    """
    Type for a TYPE OF VERSION FRAME.

    :ivar type_of_validity_ref:
    :ivar frame_class_ref: Class of VERSION FRAME to contain classes.
    :ivar classes: Classes that should  be present  in FRAME.
    :ivar types_of_entity: TYPES OF ENTITY to include in frame.
    :ivar includes: Types of frame included in frame.
    :ivar locating_system_ref: Required spatial coordinate system
        (srsName).  E.g.  WGS84 Value to use for   location elements
        using coordinates if not specified on individual elements.
    :ivar modification_set: Whether contained elements must be whole set
        or can be just a Delta.
    :ivar layer_ref:
    """
    class Meta:
        name = "TypeOfFrame_ValueStructure"

    type_of_validity_ref: Optional[TypeOfValidityRef] = field(
        default=None,
        metadata={
            "name": "TypeOfValidityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frame_class_ref: Optional[ClassRefStructure] = field(
        default=None,
        metadata={
            "name": "FrameClassRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    classes: Optional[ClassesInRepositoryRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    types_of_entity: Optional[TypeOfEntityRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfEntity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    includes: Optional[TypesOfFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    locating_system_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocatingSystemRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    modification_set: Optional[ModificationSetEnumeration] = field(
        default=None,
        metadata={
            "name": "ModificationSet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    layer_ref: Optional[LayerRef] = field(
        default=None,
        metadata={
            "name": "LayerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFrame(TypeOfFrameValueStructure):
    """
    Classification of TYPE OF VERSION FRAME.

    :ivar id: Reference to a TYPE OF FRAME.
    :ivar name_of_classified_entity_class: Name of Class of the ENTITY.
        Allows reflection. Fixed for each ENTITY type.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name_of_classified_entity_class: str = field(
        init=False,
        default="VersionFrame",
        metadata={
            "name": "nameOfClassifiedEntityClass",
            "type": "Attribute",
        }
    )
