from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.class_refs_rel_structure import ClassRefsRelStructure
from netex.frame_nature_enumeration import FrameNatureEnumeration
from netex.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfValidityValueStructure(TypeOfValueVersionStructure):
    """
    Type for a TYPE OF VALIDITY.

    :ivar periodicity: Periodicity of data in frames of this type.
    :ivar nature: Nature of presence of data in  Frames of this type.
    :ivar classes: Classes that should  be present  in FRAME.
    """
    class Meta:
        name = "TypeOfValidity_ValueStructure"

    periodicity: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Periodicity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    nature: Optional[FrameNatureEnumeration] = field(
        default=None,
        metadata={
            "name": "Nature",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    classes: Optional[ClassRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
