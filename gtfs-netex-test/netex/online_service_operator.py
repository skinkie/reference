from dataclasses import dataclass
from .online_service_operator_version_structure import (
    OnlineServiceOperatorVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnlineServiceOperator(OnlineServiceOperatorVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
