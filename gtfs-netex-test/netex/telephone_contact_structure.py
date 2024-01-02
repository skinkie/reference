from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TelephoneContactStructure:
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
        },
    )
    tel_country_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TelCountryCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "pattern": r"[0-9]{1,3}",
        },
    )
