from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class DirektrufType:
    telefonnummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "Telefonnummer",
            "type": "Element",
            "namespace": "",
        },
    )
    ipadresse: Optional[str] = field(
        default=None,
        metadata={
            "name": "IPAdresse",
            "type": "Element",
            "namespace": "",
        },
    )
