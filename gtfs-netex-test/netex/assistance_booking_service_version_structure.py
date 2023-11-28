from dataclasses import dataclass, field
from typing import Optional
from netex.all_modes_enumeration import AllModesEnumeration
from netex.assistance_availability_enumeration import AssistanceAvailabilityEnumeration
from netex.authority_ref import AuthorityRef
from netex.booking_arrangements_structure import BookingArrangementsStructure
from netex.contact_structure import ContactStructure
from netex.flexible_line_ref import FlexibleLineRef
from netex.flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from netex.line_ref import LineRef
from netex.local_service_version_structure import LocalServiceVersionStructure
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.operator_ref import OperatorRef
from netex.personal_mode_of_operation_ref import PersonalModeOfOperationRef
from netex.scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from netex.vehicle_pooling_ref import VehiclePoolingRef
from netex.vehicle_rental_ref import VehicleRentalRef
from netex.vehicle_sharing_ref import VehicleSharingRef
from netex.version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AssistanceBookingServiceVersionStructure(LocalServiceVersionStructure):
    """
    Type for ASSISTANCE BOOKING SERVICE.

    :ivar assistance_availability: Availilability of assistance.
    :ivar wheelchair_booking_required: Whether a booking is needed to
        use a wheelchair.
    :ivar booking_contact: Contact details for ASSISTANCE BOOKING
        SERVICE.
    :ivar booking_arrangements: Booking conditions for ASSISTANCE
        BOOKING SERVICE.
    :ivar vehicle_mode:
    :ivar choice:
    :ivar authority_ref_or_operator_ref:
    :ivar flexible_line_ref_or_line_ref:
    :ivar booked_object_ref: Specific object to which booking relates,
        e.g. SCHEDULED STOP POINT, STOP, VEHICLE JOURNEY, etc.
    :ivar notice_assignments: NOTICEs for ASSISTANCE BOOKING SERVICE.
    """
    class Meta:
        name = "AssistanceBookingService_VersionStructure"

    assistance_availability: Optional[AssistanceAvailabilityEnumeration] = field(
        default=None,
        metadata={
            "name": "AssistanceAvailability",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_booking_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairBookingRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_contact: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "BookingContact",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_arrangements: Optional[BookingArrangementsStructure] = field(
        default=None,
        metadata={
            "name": "BookingArrangements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonalModeOfOperationRef",
                    "type": PersonalModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingRef",
                    "type": VehiclePoolingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingRef",
                    "type": VehicleSharingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalRef",
                    "type": VehicleRentalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleModeOfOperationRef",
                    "type": FlexibleModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledModeOfOperationRef",
                    "type": ScheduledModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    authority_ref_or_operator_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    flexible_line_ref_or_line_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    booked_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "BookedObjectRef",
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
