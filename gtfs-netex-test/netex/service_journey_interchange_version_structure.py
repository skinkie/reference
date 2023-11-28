from dataclasses import dataclass, field
from typing import Optional
from netex.interchange_version_structure import InterchangeVersionStructure
from netex.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.service_journey_pattern_interchange_ref import ServiceJourneyPatternInterchangeRef
from netex.vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceJourneyInterchangeVersionStructure(InterchangeVersionStructure):
    """
    Type for SERVICE JOURNEY INTERCHANGE.

    :ivar from_point_ref: SCHEDULED STOP POINT feeding INTERCHANGE.
    :ivar from_visit_number: Visit number to distinguish which visit to
        FROM SCHEDULED STOP POINT this is. Default is one. Only needed
        for circular routes with connections at the same stop on
        different visits.
    :ivar to_point_ref: SCHEDULED STOP POINT distributing from
        INTERCHANGE.
    :ivar to_visit_number: Visit number to distinguish which visit to TO
        SCHEDULED STOP POINT  this is. Default is one. Only needed for
        circular routes with connections at the same stop on different
        visits.
    :ivar from_journey_ref: VEHICLE JOURNEY that feeds the INTERCHANGE.
    :ivar to_journey_ref: VEHICLE JOURNEY that distributes from the
        INTERCHANGE.
    :ivar service_journey_pattern_interchange_ref:
    """
    class Meta:
        name = "ServiceJourneyInterchange_VersionStructure"

    from_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "FromVisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "ToVisitNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_journey_ref: VehicleJourneyRefStructure = field(
        metadata={
            "name": "FromJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_journey_ref: VehicleJourneyRefStructure = field(
        metadata={
            "name": "ToJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    service_journey_pattern_interchange_ref: Optional[ServiceJourneyPatternInterchangeRef] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyPatternInterchangeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
