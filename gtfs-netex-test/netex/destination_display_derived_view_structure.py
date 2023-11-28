from dataclasses import dataclass, field
from typing import Optional
from netex.derived_view_structure import DerivedViewStructure
from netex.destination_display_ref import DestinationDisplayRef
from netex.key_list import KeyList
from netex.multilingual_string import MultilingualString
from netex.private_code import PrivateCode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DestinationDisplayDerivedViewStructure(DerivedViewStructure):
    """
    Type for Simplified DESTINATION DISPLAY.

    :ivar key_list: A list of alternative Key values for an element.
    :ivar destination_display_ref:
    :ivar name: Name of destination on DESTINATION DISPLAY.
    :ivar short_name: Short Name on DESTINATION DISPLAY.
    :ivar side_text: Name of destination to show on side of VEHICLE.
    :ivar front_text: Name of destination to show on front of VEHICLE.
    :ivar driver_display_text: Text to show to Driver or Staff for the
        DESTINATION DISPLAY.
    :ivar short_code: Short code associated with Destination display
        used vehicle display controller which describes the format of
        the destination text in the front and side display in the
        vehicle. (VDV).
    :ivar public_code: Public code to show for Destination.
    :ivar private_code:
    """
    class Meta:
        name = "DestinationDisplay_DerivedViewStructure"

    key_list: Optional[KeyList] = field(
        default=None,
        metadata={
            "name": "keyList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination_display_ref: Optional[DestinationDisplayRef] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    side_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "SideText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    front_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "FrontText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_display_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "DriverDisplayText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
