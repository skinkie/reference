from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TelephoneContactStructure:
    """
    A telephone number, using GovTalk constructs.

    :ivar tel_national_number: Full telephone number including STD
        prefix.
    :ivar tel_extension_number: Any additional extension number.
    :ivar tel_country_code: Two character country prefix, e.g. 44 for
        UK.
    """
    tel_national_number: str = field(
        metadata={
            "name": "TelNationalNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
            "pattern": r"[0-9 /-]{1,20}",
        }
    )
    tel_extension_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TelExtensionNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "pattern": r"[0-9]{1,6}",
        }
    )
    tel_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TelCountryCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "pattern": r"[0-9]{1,3}",
        }
    )
