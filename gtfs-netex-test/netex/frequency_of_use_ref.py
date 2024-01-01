from dataclasses import dataclass
from .frequency_of_use_ref_structure import FrequencyOfUseRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FrequencyOfUseRef(FrequencyOfUseRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
