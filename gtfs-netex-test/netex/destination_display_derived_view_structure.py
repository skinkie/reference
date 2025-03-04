from dataclasses import dataclass, field
from typing import Optional

from .derived_view_structure import DerivedViewStructure
from .destination_display_ref import DestinationDisplayRef
from .key_list import KeyList
from .multilingual_string import MultilingualString
from .private_code import PrivateCode
from .public_code_structure import PublicCodeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DestinationDisplayDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "DestinationDisplay_DerivedViewStructure"

    key_list: Optional[KeyList] = field(
        default=None,
        metadata={
            "name": "keyList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_display_ref: Optional[DestinationDisplayRef] = field(
        default=None,
        metadata={
            "name": "DestinationDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    side_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "SideText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    front_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "FrontText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    driver_display_text: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "DriverDisplayText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: Optional[PublicCodeStructure] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
