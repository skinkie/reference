from dataclasses import dataclass, field
from netex.individual_passenger_info_ref import IndividualPassengerInfoRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class IndividualPassengerInfoRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of INDIVIDUAL PASSENGER  INFOs.
    """
    class Meta:
        name = "IndividualPassengerInfoRefs_RelStructure"

    individual_passenger_info_ref: IndividualPassengerInfoRef = field(
        metadata={
            "name": "IndividualPassengerInfoRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
