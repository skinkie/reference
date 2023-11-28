from dataclasses import dataclass, field
from typing import List, Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.fare_table_ref import FareTableRef
from netex.multilingual_string import MultilingualString
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.object_refs_rel_structure import ObjectRefsRelStructure
from netex.standard_fare_table_ref import StandardFareTableRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareTableRowVersionedChildStructure(VersionedChildStructure):
    """
    Type for a FARE TABLE ROW .

    :ivar name: Name of FARE TABLE ROW.
    :ivar label: Description of FARE TABLE ROW.
    :ivar standard_fare_table_ref_or_fare_table_ref:
    :ivar notice_assignments: NOTICEs that apply to whole FARE TABLE
        ROW.
    :ivar representing: ENTITIES that row represents +v1.1
    :ivar rows: Rowheadings to use when presenting table.
    :ivar order: Order in which FARE TABLE ROW  is to appear.
    """
    class Meta:
        name = "FareTableRow_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    standard_fare_table_ref_or_fare_table_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StandardFareTableRef",
                    "type": StandardFareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableRef",
                    "type": FareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    representing: Optional[ObjectRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rows: Optional["FareTableRowsRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class FareTableRow(FareTableRowVersionedChildStructure):
    """
    An individual combination of  features in a FARE TABLE, used to associate a
    FARE PRICE.

    :ivar id:
    :ivar order: Order in which FARE TABLE ROW  is to appear.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    order: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class FareTableRowsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FARE FARE TABLE ROWs.
    """
    class Meta:
        name = "fareTableRows_RelStructure"

    fare_table_row: List[FareTableRow] = field(
        default_factory=list,
        metadata={
            "name": "FareTableRow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
