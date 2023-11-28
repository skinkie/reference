from dataclasses import dataclass, field
from netex.type_of_tariff_value_structure import TypeOfTariffValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfTariff(TypeOfTariffValueStructure):
    """
    A classification of TARIFFs according to their functional purpose.

    :ivar id:
    :ivar name_of_classified_entity_class: Name of Class of the ENTITY.
        Allows reflection. Fixed for each ENTITY type.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    name_of_classified_entity_class: str = field(
        init=False,
        default="Tariff",
        metadata={
            "name": "nameOfClassifiedEntityClass",
            "type": "Attribute",
        }
    )
