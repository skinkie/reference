from dataclasses import dataclass, field
from typing import Optional
from netex.driver_ref import DriverRef
from netex.operating_day_ref import OperatingDayRef
from netex.service_journey_version_structure import ServiceJourneyVersionStructure
from netex.uic_operating_period import UicOperatingPeriod

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DatedServiceJourneyVersionStructure(ServiceJourneyVersionStructure):
    """
    Data type for Planned VEHICLE JOURNEY (Production Timetable Service).
    """
    class Meta:
        name = "DatedServiceJourney_VersionStructure"

    operating_day_ref_or_uic_operating_period: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OperatingDayRef",
                    "type": OperatingDayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UicOperatingPeriod",
                    "type": UicOperatingPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    driver_ref: Optional[DriverRef] = field(
        default=None,
        metadata={
            "name": "DriverRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
