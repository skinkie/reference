from dataclasses import dataclass

from .facility_delivery_structure import FacilityDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityDelivery(FacilityDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
