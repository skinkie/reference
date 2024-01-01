from dataclasses import dataclass
from .type_of_concession_version_structure import (
    TypeOfConcessionVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfConcession(TypeOfConcessionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
