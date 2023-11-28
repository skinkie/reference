from dataclasses import dataclass, field
from typing import Optional
from netex.iana_country_tld_enumeration import IanaCountryTldEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CountryRefStructure:
    """
    Type for a reference to a Country Identifier.

    :ivar value:
    :ivar ref: Iso 3166-1 Two Character country code.
    :ivar ref_principality: Iso3166-3 Three character country code
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    ref: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ref_principality: Optional[str] = field(
        default=None,
        metadata={
            "name": "refPrincipality",
            "type": "Attribute",
        }
    )
