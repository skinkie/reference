from dataclasses import dataclass, field
from netex.frequency_of_use_version_structure import FrequencyOfUseVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FrequencyOfUse(FrequencyOfUseVersionStructure):
    """The limits of usage frequency for a FARE PRODUCT (or one of its components)
    or a SALES OFFER PACKAGE during a specific VALIDITY PERIOD.

    There may be different tariffs depending on how often the right is
    consumed during the period.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
