from dataclasses import dataclass
from .frequency_of_use_version_structure import FrequencyOfUseVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FrequencyOfUse(FrequencyOfUseVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
