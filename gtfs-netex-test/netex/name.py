from dataclasses import dataclass
from .code_type import CodeType


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class Name(CodeType):
    class Meta:
        name = "name"
        namespace = "http://www.opengis.net/gml/3.2"
