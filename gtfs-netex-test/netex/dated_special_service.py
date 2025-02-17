from dataclasses import dataclass, field
from typing import Any

from .dated_special_service_version_structure import DatedSpecialServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DatedSpecialService(DatedSpecialServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    service_alteration_type: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
