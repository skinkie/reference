from dataclasses import dataclass
from .validable_element_version_structure import (
    ValidableElementVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidableElement(ValidableElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
