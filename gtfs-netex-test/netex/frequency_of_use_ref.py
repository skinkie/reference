from dataclasses import dataclass
from netex.frequency_of_use_ref_structure import FrequencyOfUseRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FrequencyOfUseRef(FrequencyOfUseRefStructure):
    """
    Reference to a FREQUENCY OF USE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
