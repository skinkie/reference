from dataclasses import dataclass, field
from typing import Optional
from netex.access_zone_ref import AccessZoneRef
from netex.administrative_zone_ref import AdministrativeZoneRef
from netex.derived_view_structure import DerivedViewStructure
from netex.fare_zone_ref import FareZoneRef
from netex.mobility_service_constraint_zone_ref import MobilityServiceConstraintZoneRef
from netex.multilingual_string import MultilingualString
from netex.stop_area_ref import StopAreaRef
from netex.tariff_zone_ref import TariffZoneRef
from netex.transport_administrative_zone_ref import TransportAdministrativeZoneRef
from netex.type_of_zone_ref import TypeOfZoneRef
from netex.zone_ref import ZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ZoneDerivedViewStructure(DerivedViewStructure):
    """
    Type for SCHEDULED STOP POINT VIEW.

    :ivar choice:
    :ivar name: Name of Stop Point.
    :ivar type_of_zone_ref:
    """
    class Meta:
        name = "Zone_DerivedViewStructure"

    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MobilityServiceConstraintZoneRef",
                    "type": MobilityServiceConstraintZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopAreaRef",
                    "type": StopAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportAdministrativeZoneRef",
                    "type": TransportAdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessZoneRef",
                    "type": AccessZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZoneRef",
                    "type": AdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareZoneRef",
                    "type": FareZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffZoneRef",
                    "type": TariffZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ZoneRef",
                    "type": ZoneRef,
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
    type_of_zone_ref: Optional[TypeOfZoneRef] = field(
        default=None,
        metadata={
            "name": "TypeOfZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
