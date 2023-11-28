from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from netex.administrative_zone_ref import AdministrativeZoneRef
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.codespace import Codespace
from netex.codespace_ref import CodespaceRef
from netex.multilingual_string import MultilingualString
from netex.type_of_codespace_assignment_ref import TypeOfCodespaceAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CodespaceAssignmentVersionedChildStructure(VersionedChildStructure):
    """
    Type for a CODESPACE ASSIGNMENT.

    :ivar codespace_ref_or_codespace:
    :ivar administrative_zone_ref:
    :ivar start_date: Start date for effectiveness of CODESPACE
        ASSIGNMENT.
    :ivar end_date: End date for effectiveness of CODESPACE ASSIGNMENT.
        Date is INCLUSIVE.
    :ivar name_of_class: Name of class whose names are being assigned.
    :ivar code_prefix: Code prefix assigned uniquely to zone. Used to
        allocate new ids If CODESPACE also specified, used within
        CODESPACE. Only this ADMINISTRATIVE ZONE may allocate codes
        beginning with these prefixes.
    :ivar start_value_or_end_value:
    :ivar maximum_length: Maximum Length for code. +V1.1
    :ivar description: Description of CODESPACE ASSIGNMENT.
    :ivar type_of_codespace_assignment_ref:
    """
    class Meta:
        name = "CodespaceAssignment_VersionedChildStructure"

    codespace_ref_or_codespace: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CodespaceRef",
                    "type": CodespaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Codespace",
                    "type": Codespace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    administrative_zone_ref: Optional[AdministrativeZoneRef] = field(
        default=None,
        metadata={
            "name": "AdministrativeZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name_of_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameOfClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    code_prefix: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CodePrefix",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_value_or_end_value: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StartValue",
                    "type": str,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndValue",
                    "type": str,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 2,
        }
    )
    maximum_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_codespace_assignment_ref: Optional[TypeOfCodespaceAssignmentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfCodespaceAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
