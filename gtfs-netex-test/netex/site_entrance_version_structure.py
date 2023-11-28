from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.entrance_enumeration import EntranceEnumeration
from netex.multilingual_string import MultilingualString
from netex.site_component_version_structure import SiteComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteEntranceVersionStructure(SiteComponentVersionStructure):
    """
    Type for SITE ENTRANCe.

    :ivar public_code: Alternative identifier of ENTRANCE shown to
        Public.
    :ivar label: Label of ENTRANCE.
    :ivar entrance_type: Classification of ENTRANCE. Use EQUIPMENT
        element to describe in further detail.
    :ivar is_external: Whether ENTRANCE is external to STOP PLACE.
        Default is true.
    :ivar is_entry: Whether ENTRANCE can be used for entry. Default is
        true.
    :ivar is_exit: Whether ENTRANCE can be used for exit. Default is
        true.
    :ivar width: Width of ENTRANCE in metres.
    :ivar height: Height of ENTRANCE In metres.
    :ivar dropped_kerb_outside: Whether nearest crossing to ENTRANCE has
        dropped kerb.
    :ivar drop_off_point_close: Whether there is a drop off point close
        by to ENTRANCE.
    """
    class Meta:
        name = "SiteEntrance_VersionStructure"

    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance_type: Optional[EntranceEnumeration] = field(
        default=None,
        metadata={
            "name": "EntranceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_external: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsExternal",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_entry: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_exit: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsExit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dropped_kerb_outside: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DroppedKerbOutside",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    drop_off_point_close: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DropOffPointClose",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
