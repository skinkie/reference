from dataclasses import dataclass
from .fare_element_in_sequence_ref_structure import (
    FareElementInSequenceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControllableElementInSequenceRefStructure(
    FareElementInSequenceRefStructure
):
    value: RestrictedVar
