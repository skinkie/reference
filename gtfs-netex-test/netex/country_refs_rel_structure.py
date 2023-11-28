from dataclasses import dataclass, field
from typing import List
from netex.country_ref import CountryRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CountryRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of COUNTRY references.

    :ivar country_ref: Reference to a COUNTRY.
    """
    class Meta:
        name = "countryRefs_RelStructure"

    country_ref: List[CountryRef] = field(
        default_factory=list,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
