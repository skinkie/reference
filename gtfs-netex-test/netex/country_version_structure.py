from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.place_version_structure import PlaceVersionStructure
from netex.private_code_structure import PrivateCodeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CountryVersionStructure(PlaceVersionStructure):
    """
    Type for a  COUNTRY.

    :ivar uic_code: Code given to COUNTRY by UIC.
    :ivar alternative_names: Alternative names for COUNTRY.
    :ivar principality: ISO Country Subdivision code type, eg GB-WLS,
        GB-SCT, GB-NIR, GB-ENG.  +v1.1.
    """
    class Meta:
        name = "Country_VersionStructure"

    uic_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "UicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    principality: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
