from dataclasses import dataclass, field
from typing import Optional
from netex.derived_view_structure import DerivedViewStructure
from netex.multilingual_string import MultilingualString
from netex.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.tariff_zone_ref_structure import TariffZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DistanceMatrixElementDerivedViewStructure(DerivedViewStructure):
    """
    Type for CONNECTING JOURNEY VIEW.

    :ivar start_stop_point_ref_or_start_tariff_zone_ref:
    :ivar start_name: Name of Start Stop Point.
    :ivar end_stop_point_ref_or_end_tariff_zone_ref:
    :ivar end_name: Name of Stop Point.
    """
    class Meta:
        name = "DistanceMatrixElement_DerivedViewStructure"

    start_stop_point_ref_or_start_tariff_zone_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StartStopPointRef",
                    "type": ScheduledStopPointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartTariffZoneRef",
                    "type": TariffZoneRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    start_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "StartName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_stop_point_ref_or_end_tariff_zone_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EndStopPointRef",
                    "type": ScheduledStopPointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndTariffZoneRef",
                    "type": TariffZoneRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    end_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "EndName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
