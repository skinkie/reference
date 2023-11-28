from dataclasses import dataclass, field
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.taxi_stand_ref import TaxiStandRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiRankRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TAXI STANDs.
    """
    class Meta:
        name = "taxiRankRefs_RelStructure"

    taxi_stand_ref: TaxiStandRef = field(
        metadata={
            "name": "TaxiStandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
