from dataclasses import dataclass

from .frequency_of_use_version_structure import FrequencyOfUseVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FrequencyOfUse(FrequencyOfUseVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
