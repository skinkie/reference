from dataclasses import dataclass, field
from typing import Optional
from netex.modification_enumeration import ModificationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeltaValueStructure:
    """
    Type for a DELTA VALUE.

    :ivar delta_ref: Identifier of DELTA of which this is part.
    :ivar modification: Nature of change made by DELTA.
    :ivar value_name: Name of VALUE altered by DELTA.
    :ivar old_value: Previous value for attribute.
    :ivar new_value: New value for attribute set by DELTA.
    :ivar id: Identifier of DELTA.
    """
    delta_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeltaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    modification: Optional[ModificationEnumeration] = field(
        default=None,
        metadata={
            "name": "Modification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    value_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValueName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    old_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "OldValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    new_value: Optional[object] = field(
        default=None,
        metadata={
            "name": "NewValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
