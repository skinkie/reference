from dataclasses import dataclass

from .info_link_structure_1 import InfoLinkStructure1

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class InfoLink(InfoLinkStructure1):
    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
