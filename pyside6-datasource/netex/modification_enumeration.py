from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ModificationEnumeration(Enum):
    """Classification of modification as addition, deletion or revision.

    Enumerated value.

    :cvar NEW: This is a definition of a new entity.
    :cvar REVISE: This is a revision to an existing entity. All values
        are replaced.
    :cvar DELETE: This is a deletion of an existing entity.
    :cvar UNCHANGED: This is a repeat of the values to an entity that
        has not change since the previous version. All values are
        replaced.
    :cvar DELTA: This is just the changes to a previous version of an
        entity. Optional values are only provided if they have changed.
    """
    NEW = "new"
    REVISE = "revise"
    DELETE = "delete"
    UNCHANGED = "unchanged"
    DELTA = "delta"
