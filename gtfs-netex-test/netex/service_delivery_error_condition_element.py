from dataclasses import dataclass
from netex.service_delivery_error_condition_structure import ServiceDeliveryErrorConditionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceDeliveryErrorConditionElement(ServiceDeliveryErrorConditionStructure):
    """
    Element fror an erroc condition for use in WSDL.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
