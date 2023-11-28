from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.open_transport_mode_ref import OpenTransportModeRef
from netex.transport_mode_structure import TransportModeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransportModesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TRANSPORT MODEs.
    """
    class Meta:
        name = "transportModes_RelStructure"

    open_transport_mode_ref_or_transport_mode: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OpenTransportModeRef",
                    "type": OpenTransportModeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportMode",
                    "type": TransportModeStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
