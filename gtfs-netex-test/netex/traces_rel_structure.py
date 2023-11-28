from dataclasses import dataclass, field
from typing import List
from netex.trace import Trace

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TracesRelStructure:
    """
    A collection of one or more TRACEs.

    :ivar trace: A way to record the context of the changes occurred in
        a given ENTITY instance, as regards the authors, the causes of
        the changes, etc., possibly accompanied by a descriptive text.he
        next one.  A TRACE contains pairs of attributes' old values -
        new values.
    """
    class Meta:
        name = "traces_RelStructure"

    trace: List[Trace] = field(
        default_factory=list,
        metadata={
            "name": "Trace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
