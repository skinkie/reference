from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.fare_contract_entry import FareContractEntry
from netex.fare_contract_entry_ref import FareContractEntryRef
from netex.offered_travel_specification import OfferedTravelSpecification
from netex.offered_travel_specification_ref import OfferedTravelSpecificationRef
from netex.requested_travel_specification import RequestedTravelSpecification
from netex.requested_travel_specification_ref import RequestedTravelSpecificationRef
from netex.sales_transaction import SalesTransaction
from netex.sales_transaction_ref import SalesTransactionRef
from netex.travel_specification_1 import TravelSpecification1
from netex.travel_specification_2 import TravelSpecification2
from netex.travel_specification_ref import TravelSpecificationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareContractEntriesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of FARE CONTRACT ENTRYs.
    """
    class Meta:
        name = "fareContractEntries_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SalesTransactionRef",
                    "type": SalesTransactionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OfferedTravelSpecificationRef",
                    "type": OfferedTravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RequestedTravelSpecificationRef",
                    "type": RequestedTravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecificationRef",
                    "type": TravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractEntryRef",
                    "type": FareContractEntryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransaction",
                    "type": SalesTransaction,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OfferedTravelSpecification",
                    "type": OfferedTravelSpecification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RequestedTravelSpecification",
                    "type": RequestedTravelSpecification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecification",
                    "type": TravelSpecification1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelSpecification_",
                    "type": TravelSpecification2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContractEntry_",
                    "type": FareContractEntry,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
