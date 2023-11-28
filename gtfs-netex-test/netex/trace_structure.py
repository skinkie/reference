from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from netex.delta import Delta
from netex.version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TraceStructure:
    """
    Type for a TYPE OF TRACE.

    :ivar object_ref: Identifier of ENTITY IN VERSION that has been
        created or  modiifed.
    :ivar changed_at: Timestamp of when ENTITY IN VERSION was Changed.
    :ivar changed_by: Who made change.
    :ivar description: Description of change.
    :ivar delta:
    :ivar id: Identifier of TRACE.
    :ivar created: Date TRACE was first created.
    """
    object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    changed_at: XmlDateTime = field(
        metadata={
            "name": "ChangedAt",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    changed_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChangedBy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    delta: Optional[Delta] = field(
        default=None,
        metadata={
            "name": "Delta",
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
