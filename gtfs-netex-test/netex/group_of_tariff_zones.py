from dataclasses import dataclass

from .group_of_tariff_zones_version_structure import GroupOfTariffZonesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfTariffZones(GroupOfTariffZonesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
