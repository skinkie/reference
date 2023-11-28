from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.multilingual_string import MultilingualString
from netex.rounding_method_enumeration import RoundingMethodEnumeration
from netex.rounding_steps_rel_structure import RoundingStepsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoundingVersionedStructure(DataManagedObjectStructure):
    """
    Type for ROUNDING.

    :ivar name: Name of ROUNDING parameter set.
    :ivar rounding_method: Rounding method to use.  If "down", "up" or
        "split".  use modulus. If "step table" use ROUNDING STEPs.
    :ivar rounding_modulus: Rounding modulus to use if method is "down",
        "up" or  "split".
    :ivar rounding_steps: PRICE amount. in specified currency.
    """
    class Meta:
        name = "Rounding_VersionedStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rounding_method: Optional[RoundingMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "RoundingMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rounding_modulus: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RoundingModulus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rounding_steps: Optional[RoundingStepsRelStructure] = field(
        default=None,
        metadata={
            "name": "roundingSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
