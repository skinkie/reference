from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.info_links_rel_structure import InfoLinksRelStructure
from netex.multilingual_string import MultilingualString
from netex.private_code import PrivateCode
from netex.private_code_structure import PrivateCodeStructure
from netex.type_of_equipment_ref import TypeOfEquipmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EquipmentVersionStructure(DataManagedObjectStructure):
    """
    Type for EQUIPMENT.

    :ivar name: Name of EQUIPMENT.
    :ivar private_code:
    :ivar public_code: A Public code which may be displayed on equipment
        to identify it.
    :ivar image: Default image for EQUIPMENT.
    :ivar type_of_equipment_ref:
    :ivar description: Further description or other comment for
        EQUIPMENT.
    :ivar note: Further description or other comment for internal use by
        OPERATOR.
    :ivar info_links: INFO LINKs associated with EQUIPMENT +v1.1
    :ivar out_of_service: Whether the EQUIPMENT is out of service for
        protracted time. A separate Real time services should be used
        for short term outages. e.g. SIRI FM.
    """
    class Meta:
        name = "Equipment_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    image: Optional[str] = field(
        default=None,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_equipment_ref: Optional[TypeOfEquipmentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    note: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    info_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "infoLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    out_of_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OutOfService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
