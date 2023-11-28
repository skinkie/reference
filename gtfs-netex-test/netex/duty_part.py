from dataclasses import dataclass, field
from netex.duty_part_version_structure import DutyPartVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DutyPart(DutyPartVersionStructure):
    """A continuous part of a driver DUTY during which (s)he is under the
    management of the company.

    A DUTY PART may include BREAKs. .
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
