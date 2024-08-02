from dataclasses import dataclass, field

from .iana_country_tld_enumeration import IanaCountryTldEnumeration

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class CountryRefStructure:
    value: IanaCountryTldEnumeration = field(
        metadata={
            "required": True,
        }
    )
