from dataclasses import dataclass

from .annotated_connection_link_structure import AnnotatedConnectionLinkStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AnnotatedConnectionLinkRef(AnnotatedConnectionLinkStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
