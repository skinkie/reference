from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.derived_view_structure import DerivedViewStructure
from netex.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.service_link_in_journey_pattern import ServiceLinkInJourneyPattern
from netex.service_link_ref import ServiceLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnwardServiceLinkDerivedViewStructure(DerivedViewStructure):
    """
    Type for information about onwards SERVICE LINK.

    :ivar service_link_in_journey_pattern:
    :ivar service_link_ref:
    :ivar to_point_ref: Identifier of POINT at which LINK ends.
    :ivar distance: Distance for SERVICE LINK.
    :ivar run_time: RUN TIME for SERVICE LINK.
    """
    class Meta:
        name = "OnwardServiceLink_DerivedViewStructure"

    service_link_in_journey_pattern: Optional[ServiceLinkInJourneyPattern] = field(
        default=None,
        metadata={
            "name": "ServiceLinkInJourneyPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_link_ref: Optional[ServiceLinkRef] = field(
        default=None,
        metadata={
            "name": "ServiceLinkRef",
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
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    run_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "RunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
