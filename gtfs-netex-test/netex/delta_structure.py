from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from netex.delta_values_rel_structure import DeltaValuesRelStructure
from netex.modification_enumeration import ModificationEnumeration
from netex.simple_object_ref import SimpleObjectRef
from netex.simple_object_ref_structure import SimpleObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeltaStructure:
    """
    Type for a DELTA.

    :ivar simple_object_ref:
    :ivar from_version_ref: Base version against which DELTA is made.
    :ivar to_version_ref: Version being compared against baseline by
        DELTA.
    :ivar modification: Nature of change.
    :ivar delta_values: Values for changes to ENTITY.
    :ivar id: Identifier of DELTA.
    :ivar created: Date reference was first created.
    """
    simple_object_ref: Optional[SimpleObjectRef] = field(
        default=None,
        metadata={
            "name": "SimpleObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_version_ref: Optional[SimpleObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "FromVersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_version_ref: SimpleObjectRefStructure = field(
        metadata={
            "name": "ToVersionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
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
    delta_values: Optional[DeltaValuesRelStructure] = field(
        default=None,
        metadata={
            "name": "deltaValues",
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
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
