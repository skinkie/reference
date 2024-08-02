from dataclasses import dataclass, field

from .capability_access_control_structure import CapabilityAccessControlStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessageCapabilityAccessControlStructure(CapabilityAccessControlStructure):
    check_info_channel_ref: bool = field(
        default=True,
        metadata={
            "name": "CheckInfoChannelRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
