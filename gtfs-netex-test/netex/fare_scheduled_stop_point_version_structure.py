from dataclasses import dataclass, field
from typing import Optional
from netex.border_point_ref import BorderPointRef
from netex.fare_scheduled_stop_point_ref_structure import FareScheduledStopPointRefStructure
from netex.multilingual_string import MultilingualString
from netex.scheduled_stop_point_version_structure import ScheduledStopPointVersionStructure
from netex.site_facility_set import SiteFacilitySet
from netex.site_facility_set_ref import SiteFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareScheduledStopPointVersionStructure(ScheduledStopPointVersionStructure):
    """
    Type for FARE SCHEDULED STOP POINT restricts id.

    :ivar site_facility_set_ref_or_site_facility_set:
    :ivar name_on_routing: Name to use to indicate station on routings
        and itineraries.
    :ivar accounting_stop_point_ref: Station to use for accounting (TAP
        TSi B1)
    :ivar border_point_ref:
    """
    class Meta:
        name = "FareScheduledStopPoint_VersionStructure"

    site_facility_set_ref_or_site_facility_set: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SiteFacilitySetRef",
                    "type": SiteFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFacilitySet",
                    "type": SiteFacilitySet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    name_on_routing: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "NameOnRouting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accounting_stop_point_ref: Optional[FareScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "AccountingStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    border_point_ref: Optional[BorderPointRef] = field(
        default=None,
        metadata={
            "name": "BorderPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
