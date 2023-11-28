from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ModificationSetEnumeration(Enum):
    """Classification of modification as addition, deletion, revision or delta
    only.

    Enumerated value.

    :cvar ALL: This  incldues definitions of  one ore more new entities.
    :cvar CHANGES_ONLY: This is just the modifications (addition,
        revision, deletion); entities which are unchanged are omitted.
    """
    ALL = "all"
    CHANGES_ONLY = "changesOnly"
