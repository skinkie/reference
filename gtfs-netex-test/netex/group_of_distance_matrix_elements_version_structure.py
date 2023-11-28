from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.cell_versioned_child_structure import (
    FareTablesRelStructure,
    PriceGroupsRelStructure,
)
from netex.distance_matrix_element_prices_rel_structure import DistanceMatrixElementPricesRelStructure
from netex.distance_matrix_elements_rel_structure import DistanceMatrixElementsRelStructure
from netex.geographical_structure_factors_rel_structure import GeographicalStructureFactorsRelStructure
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfDistanceMatrixElementsVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for GROUP OF DISTANCE MATRIX ELEMENTs.

    :ivar use_to_exclude: Whether contents of Group should be used to
        exclude (true) from a large list . The default is include
        (i.e.false)
    :ivar price_groups: PRICE GROUPSs  making up FARE PRODUCT.
    :ivar fare_tables: Other FARE TABLESs for DISTANCE MATRIX ELEMENT.
    :ivar distance: GROUP OF DISTANCE MATRIX ELEMENTs to use when
        advertising Train -If different from Id.
    :ivar structure_factors: Use of GEOGRAPHICAL STRUCTURE FACTORss in a
        particular sequence.
    :ivar notice_assignments: NOTICEs applying to element.
    :ivar members: TARIFFs applying to element.
    :ivar prices: prices associated with DSISTANCE MATRIX ELEMENT.
    """
    class Meta:
        name = "GroupOfDistanceMatrixElements_VersionStructure"

    use_to_exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseToExclude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_groups: Optional[PriceGroupsRelStructure] = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_tables: Optional[FareTablesRelStructure] = field(
        default=None,
        metadata={
            "name": "fareTables",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    structure_factors: Optional[GeographicalStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "structureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    members: Optional[DistanceMatrixElementsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[DistanceMatrixElementPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
