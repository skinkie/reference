from dataclasses import dataclass, field
from netex.country_version_structure import CountryVersionStructure
from netex.iana_country_tld_enumeration import IanaCountryTldEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Country(CountryVersionStructure):
    """
    A sovereign COUNTRY.where entities may be located or domiciled.

    :ivar id: Identifier of COUNTRY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: IanaCountryTldEnumeration = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
