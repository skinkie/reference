from dataclasses import dataclass, field
from typing import Optional
from netex.check_constraints_rel_structure import CheckConstraintsRelStructure
from netex.class_of_use_ref import ClassOfUseRef
from netex.equipment_places_rel_structure import EquipmentPlacesRelStructure
from netex.level_ref import LevelRef
from netex.local_services_rel_structure import LocalServicesRelStructure
from netex.place_equipments_rel_structure import PlaceEquipmentsRelStructure
from netex.site_element_version_structure import SiteElementVersionStructure
from netex.site_ref_structure import SiteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteComponentVersionStructure(SiteElementVersionStructure):
    """
    A component of a SITE COMPONENT.

    :ivar site_ref: Reference to parent of SITE, if any.
    :ivar level_ref:
    :ivar class_of_use_ref:
    :ivar check_constraints: Impediments to navigation from processes or
        barriers. For example security, check in etc.
    :ivar equipment_places: EQUIPMENT PLACEs within SITE COMPONENT.
    :ivar place_equipments: Items of fixed EQUIPMENT that may be located
        in places within the SITE  ELEMENT.
    :ivar local_services: LOCAL SERVICEs that may be located in PLACEs
        within the SITE ELEMENT.
    """
    class Meta:
        name = "SiteComponent_VersionStructure"

    site_ref: Optional[SiteRefStructure] = field(
        default=None,
        metadata={
            "name": "SiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    level_ref: Optional[LevelRef] = field(
        default=None,
        metadata={
            "name": "LevelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    class_of_use_ref: Optional[ClassOfUseRef] = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    check_constraints: Optional[CheckConstraintsRelStructure] = field(
        default=None,
        metadata={
            "name": "checkConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipment_places: Optional[EquipmentPlacesRelStructure] = field(
        default=None,
        metadata={
            "name": "equipmentPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_equipments: Optional[PlaceEquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "placeEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    local_services: Optional[LocalServicesRelStructure] = field(
        default=None,
        metadata={
            "name": "localServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
