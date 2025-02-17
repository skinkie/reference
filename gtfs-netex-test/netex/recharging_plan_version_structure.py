from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .block_refs_rel_structure import BlockRefsRelStructure
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .recharging_process_enumeration import RechargingProcessEnumeration
from .recharging_steps_rel_structure import RechargingStepsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RechargingPlanVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "RechargingPlan_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    recharging_process_type: Optional[RechargingProcessEnumeration] = field(
        default=None,
        metadata={
            "name": "RechargingProcessType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    total_charge_energy: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TotalChargeEnergy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    charging_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ChargingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    recharging_steps: Optional[RechargingStepsRelStructure] = field(
        default=None,
        metadata={
            "name": "rechargingSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    block_refs: Optional[BlockRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "blockRefs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
