from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime
from netex.day_type_ref import DayTypeRef
from netex.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from netex.derived_view_structure import DerivedViewStructure
from netex.destination_display_view import DestinationDisplayView
from netex.fare_day_type_ref import FareDayTypeRef
from netex.frequency_structure import FrequencyStructure
from netex.journey_pattern_ref import JourneyPatternRef
from netex.multilingual_string import MultilingualString
from netex.service_journey_pattern_ref import ServiceJourneyPatternRef
from netex.service_journey_ref_structure import ServiceJourneyRefStructure
from netex.service_pattern_ref import ServicePatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ConnectingJourneyDerivedViewStructure(DerivedViewStructure):
    """
    Type for CONNECTING JOURNEY VIEW.

    :ivar service_journey_ref: Service Journey to which srevice
        connects.
    :ivar departure_time_or_frequency:
    :ivar name: Name of journey.
    :ivar destination_display_view:
    :ivar fare_day_type_ref_or_day_type_ref:
    :ivar choice:
    :ivar connecting_order: Order of Point within Connecting journey as
        an absolute number.
    :ivar connecting_visit_number: Order of Point within Connecting as
        number of visits to the same stop.  Default is 1.
    """
    class Meta:
        name = "ConnectingJourney_DerivedViewStructure"

    service_journey_ref: ServiceJourneyRefStructure = field(
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    departure_time_or_frequency: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DepartureTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Frequency",
                    "type": FrequencyStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_view: Optional[DestinationDisplayView] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_day_type_ref_or_day_type_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    connecting_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "ConnectingOrder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    connecting_visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "ConnectingVisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
