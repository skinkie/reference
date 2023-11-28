from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.medium_application_instance import MediumApplicationInstance

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MediumApplicationInstanceRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of a MEDIUM APPLICATION INSTANCEs in Sequence.

    :ivar medium_application_instance: A component (mobile phone, smart
        card, etc) with the necessary facilities (hardware and software)
        to host a MEDIUM APPLICATION INSTANCE and communicate with a
        control device. +v1.2.2
    """
    class Meta:
        name = "mediumApplicationInstance_RelStructure"

    medium_application_instance: List[MediumApplicationInstance] = field(
        default_factory=list,
        metadata={
            "name": "MediumApplicationInstance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
