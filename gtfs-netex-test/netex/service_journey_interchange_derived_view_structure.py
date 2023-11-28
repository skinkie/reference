from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.connecting_journey_view import ConnectingJourneyView
from netex.connection_certainty_enumeration import ConnectionCertaintyEnumeration
from netex.derived_view_structure import DerivedViewStructure
from netex.line_derived_view_structure import LineDerivedViewStructure
from netex.multilingual_string import MultilingualString
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.service_journey_interchange_ref import ServiceJourneyInterchangeRef
from netex.vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceJourneyInterchangeDerivedViewStructure(DerivedViewStructure):
    """
    Type for SERVICE JOURNEY INTERCHANGE VIEW.

    :ivar service_journey_interchange_ref:
    :ivar description: Description of SCHEDULED STOP POINT feeding
        INTERCHANGE.
    :ivar stay_seated: Whether the passenger can remain in vehicle (i.e.
        block linking). Default is false: the passenger must change
        vehicles for this INTERCHANGE. Default is false.
    :ivar cross_border: Whether INTERCHANGE  involves crossing an
        international border. Default is false.
    :ivar planned: Whether INTERCHANGE is planned in a timetable.
        Default is true.
    :ivar guaranteed: Whether INTERCHANGE is guaranteed. Default is
        false.
    :ivar advertised: Whether INTERCHANGE is advertised as an
        interchange. Default is true.
    :ivar controlled: Whether INTERCHANGE  is controlled in real-time.
        Default is true.
    :ivar connection_certainty: Nature of gurantee to  conenction.
    :ivar notice_assignments: NOTICEs of an interchange.
    :ivar connecting_journey_ref_or_connecting_journey_view:
    :ivar connecting_line_view: Simplified view of connecting LINE.
    :ivar standard_wait_time: Standard wait time for INTERCHANGE.
    :ivar maximum_wait_time: Maximum wait time for INTERCHANGE.
    :ivar maximum_automatic_wait_time: Maximum automatic wait time for
        INTERCHANGE.
    :ivar standard_transfer_time: Standard transfer  duration for
        INTERCHANGE.
    :ivar minimum_transfer_time: Maximum transfer duration for
        INTERCHANGE.
    :ivar maximum_transfer_time: Maximum transfer duration for
        INTERCHANGE.
    :ivar control_centre_notify_threshold: Interval before CONTROL
        CENTRE should be notified associated with  SERVICE JOURNEY
        INTERCHANGE.
    """
    class Meta:
        name = "ServiceJourneyInterchange_DerivedViewStructure"

    service_journey_interchange_ref: Optional[ServiceJourneyInterchangeRef] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyInterchangeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    stay_seated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StaySeated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cross_border: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CrossBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    planned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Planned",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    guaranteed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Guaranteed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    advertised: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Advertised",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controlled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Controlled",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    connection_certainty: Optional[ConnectionCertaintyEnumeration] = field(
        default=None,
        metadata={
            "name": "ConnectionCertainty",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    connecting_journey_ref_or_connecting_journey_view: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ConnectingJourneyRef",
                    "type": VehicleJourneyRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ConnectingJourneyView",
                    "type": ConnectingJourneyView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    connecting_line_view: Optional[LineDerivedViewStructure] = field(
        default=None,
        metadata={
            "name": "ConnectingLineView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    standard_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_automatic_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumAutomaticWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    standard_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardTransferTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumTransferTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumTransferTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    control_centre_notify_threshold: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ControlCentreNotifyThreshold",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
