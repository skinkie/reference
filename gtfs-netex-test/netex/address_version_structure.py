from dataclasses import dataclass, field
from typing import Optional
from netex.country_ref import CountryRef
from netex.multilingual_string import MultilingualString
from netex.place_version_structure import PlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AddressVersionStructure(PlaceVersionStructure):
    """
    Type for an ADDRESS.

    :ivar country_ref:
    :ivar country_name: Name of Counntry, derivedable from Country Ref.
    """
    class Meta:
        name = "Address_VersionStructure"

    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    country_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "CountryName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
