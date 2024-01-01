from dataclasses import dataclass
from .rental_option_version_structure import RentalOptionVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RentalOption(RentalOptionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
