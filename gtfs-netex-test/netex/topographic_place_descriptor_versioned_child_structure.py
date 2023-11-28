from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.multilingual_string import MultilingualString
from netex.topographic_place_ref import TopographicPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TopographicPlaceDescriptorVersionedChildStructure(VersionedChildStructure):
    """
    Type for a TOPOGRAPHIC PLACE DESCRIPTOR.

    :ivar name: Name of the TOPOGRAPHIC PLACE.
    :ivar short_name: Short name for TOPOGRAPHIC PLACE to be used when
        qualifying children.
    :ivar qualify: Qualifier to use when presenting name to distinguish
        it from other similarly named elements.
    """
    class Meta:
        name = "TopographicPlaceDescriptor_VersionedChildStructure"

    name: MultilingualString = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    qualify: Optional["TopographicPlaceDescriptorVersionedChildStructure.Qualify"] = field(
        default=None,
        metadata={
            "name": "Qualify",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass(unsafe_hash=True, kw_only=True)
    class Qualify:
        """
        :ivar qualifier_name: Qualifying name. Place name characters
            only allowed.
        :ivar topographic_place_ref:
        """
        qualifier_name: MultilingualString = field(
            metadata={
                "name": "QualifierName",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )
        topographic_place_ref: Optional[TopographicPlaceRef] = field(
            default=None,
            metadata={
                "name": "TopographicPlaceRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
