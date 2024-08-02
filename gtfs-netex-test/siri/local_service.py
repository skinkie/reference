from dataclasses import dataclass

from .local_service_structure import LocalServiceStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class LocalService(LocalServiceStructure):
    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
