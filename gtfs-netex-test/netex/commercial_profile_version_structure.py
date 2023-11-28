from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.general_group_of_entities_ref import GeneralGroupOfEntitiesRef
from netex.type_of_concession_ref import TypeOfConcessionRef
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CommercialProfileVersionStructure(UsageParameterVersionStructure):
    """
    Type for COMMERCIAL PROFILE.

    :ivar type_of_concession_ref:
    :ivar consumption_amount: Financial Factor.
    :ivar consumption_units: Consumption Factor.
    :ivar general_group_of_entities_ref:
    """
    class Meta:
        name = "CommercialProfile_VersionStructure"

    type_of_concession_ref: Optional[TypeOfConcessionRef] = field(
        default=None,
        metadata={
            "name": "TypeOfConcessionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    consumption_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ConsumptionAmount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    consumption_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ConsumptionUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_group_of_entities_ref: Optional[GeneralGroupOfEntitiesRef] = field(
        default=None,
        metadata={
            "name": "GeneralGroupOfEntitiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
