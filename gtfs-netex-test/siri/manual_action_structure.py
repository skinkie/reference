from dataclasses import dataclass

from .parameterised_action_structure import ParameterisedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ManualActionStructure(ParameterisedActionStructure):
    pass
