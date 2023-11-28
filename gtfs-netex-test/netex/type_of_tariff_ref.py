from dataclasses import dataclass
from netex.type_of_tariff_ref_structure import TypeOfTariffRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfTariffRef(TypeOfTariffRefStructure):
    """Reference to a TYPE OF TARIFF.

    (TAP TSI)
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
