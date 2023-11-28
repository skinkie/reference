from dataclasses import dataclass, field
from typing import Optional
from netex.address_ref_structure import AddressRefStructure
from netex.address_version_structure import AddressVersionStructure
from netex.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PostalAddressVersionStructure(AddressVersionStructure):
    """
    Type for a POSTAL ADDRESS.

    :ivar house_number: Number of house on street.
    :ivar building_name: Name of Building.
    :ivar address_line1: First line of Address.
    :ivar address_line2:
    :ivar street: Street on which building is found.
    :ivar town: Town, City, Village or other named settlement.
    :ivar suburb: Subarea of Town.
    :ivar post_code: Postcode or Zip code of address.
    :ivar post_code_extension: Post code extension.
    :ivar postal_region: Postal Region.
    :ivar province: Province or State of Country.
    :ivar road_address_ref: Road on which address lies.
    """
    class Meta:
        name = "PostalAddress_VersionStructure"

    house_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "HouseNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    building_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "BuildingName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    address_line1: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "AddressLine1",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    address_line2: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "AddressLine2",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    street: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Street",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    town: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Town",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    suburb: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Suburb",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    post_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    post_code_extension: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostCodeExtension",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    postal_region: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostalRegion",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    province: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Province",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    road_address_ref: Optional[AddressRefStructure] = field(
        default=None,
        metadata={
            "name": "RoadAddressRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
