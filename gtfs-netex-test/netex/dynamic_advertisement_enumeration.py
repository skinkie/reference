from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DynamicAdvertisementEnumeration(Enum):
    """
    Allowed values for Dynamic Advertisement.

    :cvar ALWAYS: Stop is always advertised to public.
    :cvar NEVER: Stop is not advertised to public.
    :cvar ONLY_IF_ORDERED: Stop is only advertised to public if they
        booked to go to stop.
    :cvar ONLY_IF_SIGNED_ON: Stop is only advertised to public if they
        are logged into system.
    """
    ALWAYS = "always"
    NEVER = "never"
    ONLY_IF_ORDERED = "onlyIfOrdered"
    ONLY_IF_SIGNED_ON = "onlyIfSignedOn"
