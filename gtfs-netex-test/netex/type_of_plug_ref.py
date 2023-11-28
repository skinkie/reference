from dataclasses import dataclass
from netex.type_of_plug_ref_structure import TypeOfPlugRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfPlugRef(TypeOfPlugRefStructure):
    """Reference to a TYPE OF PLUG.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
