from dataclasses import dataclass
from .code_with_authority_type import CodeWithAuthorityType


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class Identifier(CodeWithAuthorityType):
    class Meta:
        name = "identifier"
        namespace = "http://www.opengis.net/gml/3.2"
