from dataclasses import dataclass, field
from netex.train_number_version_structure import TrainNumberVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TrainNumber(TrainNumberVersionStructure):
    """
    Specification of codes assigned to particular VEHICLE JOURNEYs when operated by
    TRAINs of COMPOUND TRAINs according to a functional purpose (passenger
    information, operation follow-up, etc).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
