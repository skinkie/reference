from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from netex.access_mode_enumeration import AccessModeEnumeration
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.connection_certainty_enumeration import ConnectionCertaintyEnumeration
from netex.connection_ref_structure import ConnectionRefStructure
from netex.external_object_ref_structure import ExternalObjectRefStructure
from netex.multilingual_string import MultilingualString
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.private_code import PrivateCode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InterchangeVersionStructure(DataManagedObjectStructure):
    """
    Type for INTERCHANGE.

    :ivar name: Name of INTERCHANGE RULE.
    :ivar description: Description of SCHEDULED STOP POINT feeding
        INTERCHANGE.
    :ivar private_code:
    :ivar external_interchange_ref: An alternative  code that uniquely
        identifies the INTERCHANGE. Specifically for use in AVMS
        systems. For VDV compatibility.
    :ivar connection_ref: Reference to a CONNECTION Link over which the
        INTERCHANEG takes place.
    :ivar priority: Priority to assign to this INTERCHANGE.
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
    :ivar transfer_modes: ACCESS MODES by which the transfer can be
        made.
    :ivar notice_assignments: NOTICEs of an interchange.
    """
    class Meta:
        name = "Interchange_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    external_interchange_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalInterchangeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    connection_ref: Optional[ConnectionRefStructure] = field(
        default=None,
        metadata={
            "name": "ConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "Priority",
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
    transfer_modes: List[AccessModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "transferModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
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
