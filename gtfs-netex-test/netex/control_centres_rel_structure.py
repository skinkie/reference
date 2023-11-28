from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.control_centre import ControlCentre
from netex.control_centre_ref import ControlCentreRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ControlCentresRelStructure(ContainmentAggregationStructure):
    """
    A list of CONTROL CENTREs.
    """
    class Meta:
        name = "ControlCentres_RelStructure"

    control_centre_ref_or_control_centre: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControlCentreRef",
                    "type": ControlCentreRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControlCentre",
                    "type": ControlCentre,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
