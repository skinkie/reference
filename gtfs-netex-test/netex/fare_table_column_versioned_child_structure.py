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
class FareTableColumnVersionedChildStructure(VersionedChildStructure):
    """
    Type for a FARE TABLE COLUMN HEADING.

    :ivar name: Name of FARE TABLE COLUMN.
    :ivar description: Description of FARE TABLE COLUMN.
    :ivar standard_fare_table_ref_or_fare_table_ref:
    :ivar notice_assignments: NOTICEs that apply to whole FARE TABLE
        COLUMN
    :ivar representing: ENTITIES that column represents. +v1.1
    :ivar columns: Column headings to use when presenting table.
    :ivar order: Order in which FARE TABLE COLUMN HEADING is to appear.
    """
    class Meta:
        name = "FareTableColumn_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
    columns: Optional["FareTableColumnsRelStructure"] = field(
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
class FareTableColumn(FareTableColumnVersionedChildStructure):
    """
    An individual combination of  features in a FARE TABLE, used to associate a
    FARE PRICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class FareTableColumnsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of FARE FARE TABLE COLUMN HEADINGs.

    :ivar fare_table_column: A Column heading for a FARE TABLE,
    """
    class Meta:
        name = "fareTableColumns_RelStructure"

    fare_table_column: List[FareTableColumn] = field(
        default_factory=list,
        metadata={
            "name": "FareTableColumn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
