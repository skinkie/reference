from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.car_pooling_service_ref import CarPoolingServiceRef
from netex.chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from netex.online_service_ref import OnlineServiceRef
from netex.taxi_service_ref import TaxiServiceRef
from netex.transport_zone_use_enumeration import TransportZoneUseEnumeration
from netex.vehicle_rental_service_ref import VehicleRentalServiceRef
from netex.vehicle_sharing_service_ref import VehicleSharingServiceRef
from netex.vehicle_type_zone_restrictions_rel_structure import VehicleTypeZoneRestrictionsRelStructure
from netex.zone_rule_applicability_enumeration import ZoneRuleApplicabilityEnumeration
from netex.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityServiceConstraintZoneVersionStructure(ZoneVersionStructure):
    """
    Type for MOBILITY SERVICE CONSTRAINT ZONE restricts id.

    :ivar rule_applicability: Applicability of rule inside (defaut) or
        outside of zone
    :ivar zone_use: How ZONE may be used.
    :ivar maximum_speed: Maximum speed  in  ZONE.
    :ivar choice:
    :ivar vehicle_restrictions: Vehclie restrictions in Zone
    """
    class Meta:
        name = "MobilityServiceConstraintZone_VersionStructure"

    rule_applicability: Optional[ZoneRuleApplicabilityEnumeration] = field(
        default=None,
        metadata={
            "name": "RuleApplicability",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    zone_use: Optional[TransportZoneUseEnumeration] = field(
        default=None,
        metadata={
            "name": "ZoneUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_speed: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumSpeed",
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
                    "name": "OnlineServiceRef",
                    "type": OnlineServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalServiceRef",
                    "type": VehicleRentalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingServiceRef",
                    "type": VehicleSharingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleServiceRef",
                    "type": ChauffeuredVehicleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServiceRef",
                    "type": TaxiServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingServiceRef",
                    "type": CarPoolingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    vehicle_restrictions: Optional[VehicleTypeZoneRestrictionsRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleRestrictions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
