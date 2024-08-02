from dataclasses import dataclass, field
from typing import Optional

from .administrative_area_ref_structure import AdministrativeAreaRefStructure
from .info_links_structure import InfoLinksStructure
from .versioned_object_structure import VersionedObjectStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class DataManagedObjectStructure(VersionedObjectStructure):
    managed_by_area_ref: Optional[AdministrativeAreaRefStructure] = field(
        default=None,
        metadata={
            "name": "ManagedByAreaRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    info_links: Optional[InfoLinksStructure] = field(
        default=None,
        metadata={
            "name": "InfoLinks",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
