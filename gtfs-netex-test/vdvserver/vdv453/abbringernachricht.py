from dataclasses import dataclass
from .abbringernachricht_type import AbbringernachrichtType


@dataclass(kw_only=True)
class Abbringernachricht(AbbringernachrichtType):
    pass
