from dataclasses import dataclass

from .formation_assignment_structure import FormationAssignmentStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DepartureFormationAssignment(FormationAssignmentStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
