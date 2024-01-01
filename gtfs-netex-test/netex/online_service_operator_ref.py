from dataclasses import dataclass
from .online_service_operator_ref_structure import (
    OnlineServiceOperatorRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnlineServiceOperatorRef(OnlineServiceOperatorRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
