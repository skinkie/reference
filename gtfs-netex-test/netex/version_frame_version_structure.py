from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import (
    DataManagedObjectStructure,
    ValidityConditionsRelStructure,
)
from netex.codespaces_rel_structure import CodespacesRelStructure
from netex.layer_refs_rel_structure import LayerRefsRelStructure
from netex.multilingual_string import MultilingualString
from netex.traces_rel_structure import TracesRelStructure
from netex.type_of_frame_ref import TypeOfFrameRef
from netex.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.version_frame_refs_rel_structure import VersionFrameRefsRelStructure
from netex.version_ref_structure import VersionRefStructure
from netex.versions_rel_structure import VersionsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VersionFrameVersionStructure(DataManagedObjectStructure):
    """
    Type for a VERSION FRAME.

    :ivar name: Name of VERSION FRAME.
    :ivar description: Description of VERSION FRAME.
    :ivar type_of_frame_ref: Reference to a TYPE OF VERSION FRAME.
    :ivar baseline_version_frame_ref: Prerequisite Baseline VERSION
        FRAME  that all objects in this VERSION require.
    :ivar codespaces: CODE SPACES used in this frame. Normally there
        will be at least one.  A default may be specified in the Frame
        defaults.
    :ivar frame_defaults: Default values to use on elements in the frame
        that do not explicitly state a value.
    :ivar versions: Formal definitions of VERSIONs included in frame.
    :ivar prerequisites: Prerequisite VERSION FRAMEs containing elements
        that this frame depends on.  +v1.1
    :ivar traces: TRACEs recording changes to ENTITIES in FRAME.
    :ivar content_validity_conditions: Common VALIDITY CONDITIONs used
        by elements in frame.
    :ivar layers: layers included in frame
    """
    class Meta:
        name = "VersionFrame_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_frame_ref: Optional[TypeOfFrameRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    baseline_version_frame_ref: Optional[VersionRefStructure] = field(
        default=None,
        metadata={
            "name": "BaselineVersionFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    codespaces: Optional[CodespacesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frame_defaults: Optional[VersionFrameDefaultsStructure] = field(
        default=None,
        metadata={
            "name": "FrameDefaults",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    versions: Optional[VersionsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prerequisites: Optional[VersionFrameRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    traces: Optional[TracesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    content_validity_conditions: Optional[ValidityConditionsRelStructure] = field(
        default=None,
        metadata={
            "name": "contentValidityConditions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    layers: Optional[LayerRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
