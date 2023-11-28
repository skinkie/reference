from dataclasses import dataclass, field
from typing import Optional
from netex.frequency_groups_rel_structure import FrequencyGroupsRelStructure
from netex.service_journey_version_structure import ServiceJourneyVersionStructure
from netex.template_vehicle_journey_type_enumeration import TemplateVehicleJourneyTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TemplateServiceJourneyVersionStructure(ServiceJourneyVersionStructure):
    """
    Type for TEMPLATE VEHICLE JOURNEY.

    :ivar template_vehicle_journey_type: Type of TEMPLATE VEHICLE
        JOURNEY.
    :ivar frequency_groups: frequency groups defining Template journey.
        Can only be of one type.
    """
    class Meta:
        name = "TemplateServiceJourney_VersionStructure"

    template_vehicle_journey_type: Optional[TemplateVehicleJourneyTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "TemplateVehicleJourneyType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frequency_groups: Optional[FrequencyGroupsRelStructure] = field(
        default=None,
        metadata={
            "name": "frequencyGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
