from dataclasses import dataclass

from .annotated_line_structure import AnnotatedLineStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AnnotatedLineRef(AnnotatedLineStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
