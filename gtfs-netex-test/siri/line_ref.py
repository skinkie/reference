from dataclasses import dataclass

from .line_ref_structure import LineRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class LineRef(LineRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
