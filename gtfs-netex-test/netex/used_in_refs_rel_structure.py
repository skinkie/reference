from dataclasses import dataclass, field
from typing import List
from netex.group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef
from netex.group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.parking_tariff_ref import ParkingTariffRef
from netex.tariff_ref import TariffRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UsedInRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for use  of  fare table.
    """
    class Meta:
        name = "usedInRefs_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingTariffRef",
                    "type": ParkingTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffRef",
                    "type": TariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistanceMatrixElementsRef",
                    "type": GroupOfDistanceMatrixElementsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfSalesOfferPackagesRef",
                    "type": GroupOfSalesOfferPackagesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
