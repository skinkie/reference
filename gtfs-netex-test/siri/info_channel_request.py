from dataclasses import dataclass

from .info_channel_discovery_request_structure import InfoChannelDiscoveryRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class InfoChannelRequest(InfoChannelDiscoveryRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
