from dataclasses import dataclass

from .type_of_concession_ref_structure import TypeOfConcessionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfConcessionRef(TypeOfConcessionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
