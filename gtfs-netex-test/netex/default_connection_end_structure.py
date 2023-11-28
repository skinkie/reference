from dataclasses import dataclass, field
from typing import Optional
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.operator_view import OperatorView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DefaultConnectionEndStructure:
    """
    Type for a DEFAULT TRANSFER.

    :ivar transport_mode: Identifier of MODE of end point of TRANSFER.
    :ivar operator_view:
    """
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_view: Optional[OperatorView] = field(
        default=None,
        metadata={
            "name": "OperatorView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
