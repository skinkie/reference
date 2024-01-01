from dataclasses import dataclass, field
from .code_type import CodeType


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class CodeWithAuthorityType(CodeType):
    code_space: str = field(
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
            "required": True,
        }
    )
    value: RestrictedVar
