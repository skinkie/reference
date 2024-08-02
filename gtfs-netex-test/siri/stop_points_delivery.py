from dataclasses import dataclass

from .stop_points_delivery_structure import StopPointsDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopPointsDelivery(StopPointsDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
