from dataclasses import dataclass

from .value_set_structure import ValueSetStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ValueSet(ValueSetStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
