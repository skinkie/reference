from dataclasses import dataclass, field
from typing import Optional
from netex.country_ref import CountryRef
from netex.online_service_refs_rel_structure import OnlineServiceRefsRelStructure
from netex.organisation_version_structure import OrganisationVersionStructure
from netex.postal_address import PostalAddress
from netex.postal_address_version_structure import PostalAddressVersionStructure
from netex.road_address import RoadAddress

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnlineServiceOperatorVersionStructure(OrganisationVersionStructure):
    """
    Type for an ONLINE SERVICE OPERATOR.

    :ivar country_ref:
    :ivar postal_address_or_road_address_or_address:
    :ivar services: ONLIEN SERVICES managed by ONLIEN OPERATOR,
    """
    class Meta:
        name = "OnlineServiceOperator_VersionStructure"

    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    postal_address_or_road_address_or_address: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PostalAddress",
                    "type": PostalAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadAddress",
                    "type": RoadAddress,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Address",
                    "type": PostalAddressVersionStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    services: Optional[OnlineServiceRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
