from dataclasses import dataclass
from .observed_passing_time_versioned_child_structure import (
    ObservedPassingTimeVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ObservedPassingTime(ObservedPassingTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar
