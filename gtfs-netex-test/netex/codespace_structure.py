from dataclasses import dataclass, field
from typing import Optional
from netex.entity_structure import EntityStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CodespaceStructure(EntityStructure):
    """
    Type for CODESPACE.

    :ivar xmlns: Prefix used to identify CODESPACE, e.g. 'napt', 'oda',
        'ratp' etc.
    :ivar xmlns_url: CODESPACE path. The URL associated which with the
        CODESPACE defines a unique system for identifying objects within
        the CODESPACE.
    :ivar description: Description of CODESPACE.
    :ivar data_source_ref: Data Source of ENTITY.
    """
    xmlns: str = field(
        metadata={
            "name": "Xmlns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    xmlns_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "XmlnsUrl",
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
    data_source_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataSourceRef",
            "type": "Attribute",
        }
    )
