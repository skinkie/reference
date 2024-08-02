from dataclasses import dataclass

from .info_channel_delivery_structure import InfoChannelDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class InfoChannelDelivery(InfoChannelDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
