from dataclasses import dataclass, field
from typing import Optional
from netex.all_modes_enumeration import AllModesEnumeration
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.multilingual_string import MultilingualString
from netex.operational_context_ref import OperationalContextRef
from netex.time_demand_type_ref import TimeDemandTypeRef
from netex.timeband_ref import TimebandRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyTimingVersionedChildStructure(VersionedChildStructure):
    """
    Type for JOURNEY TIMING.

    :ivar name: Name of JOURNEY TIMING.
    :ivar time_demand_type_ref_or_timeband_ref:
    :ivar vehicle_mode:
    :ivar operational_context_ref:
    """
    class Meta:
        name = "JourneyTiming_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_type_ref_or_timeband_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimeDemandTypeRef",
                    "type": TimeDemandTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimebandRef",
                    "type": TimebandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    vehicle_mode: Optional[AllModesEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
