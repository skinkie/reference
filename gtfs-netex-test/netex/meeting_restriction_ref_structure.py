from dataclasses import dataclass
from .infrastructure_link_restriction_ref_structure import (
    InfrastructureLinkRestrictionRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MeetingRestrictionRefStructure(
    InfrastructureLinkRestrictionRefStructure
):
    value: RestrictedVar
