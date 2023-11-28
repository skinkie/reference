from dataclasses import dataclass, field
from typing import List
from netex.fare_table_ref import FareTableRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.standard_fare_table_ref import StandardFareTableRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareTableRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to  FARE FARE TABLEs.
    """
    class Meta:
        name = "fareTableRefs_RelStructure"

    standard_fare_table_ref_or_fare_table_ref: List[object] = field(
        default_factory=list,
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
