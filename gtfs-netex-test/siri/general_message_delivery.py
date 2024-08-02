from dataclasses import dataclass

from .general_message_delivery_structure import GeneralMessageDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessageDelivery(GeneralMessageDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
