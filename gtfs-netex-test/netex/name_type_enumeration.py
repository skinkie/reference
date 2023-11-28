from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class NameTypeEnumeration(Enum):
    """
    Allowed values for classification of ALTERNATIVE NAME.
    """
    ALIAS = "alias"
    TRANSLATION = "translation"
    COPY = "copy"
    LABEL = "label"
    OTHER = "other"
