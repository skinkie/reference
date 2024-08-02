from dataclasses import dataclass

from .access_link_ref_structure import AccessLinkRefStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class AccessLinkRef(AccessLinkRefStructure):
    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
