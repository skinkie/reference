from dataclasses import dataclass

from .manual_action_structure import ManualActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ManualAction(ManualActionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
