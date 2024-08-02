from dataclasses import dataclass

from .interchange_ref_structure import InterchangeRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class InterchangeRef(InterchangeRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
