from dataclasses import dataclass
from .validity_parameter_assignment_ref_structure import (
    ValidityParameterAssignmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GenericParameterAssignmentRefStructure(
    ValidityParameterAssignmentRefStructure
):
    value: RestrictedVar
