from dataclasses import dataclass
from netex.type_of_concession_ref_structure import TypeOfConcessionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfConcessionRef(TypeOfConcessionRefStructure):
    """
    Reference to a TYPE OF CONCESSION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
