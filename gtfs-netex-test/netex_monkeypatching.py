from netex import VersionOfObjectRefStructure, ServiceJourneyRef, ServiceJourneyPatternRef, ServiceJourney, \
    ServiceJourneyPattern, RouteRefStructure, RouteLinkRefStructure, ScheduledStopPointRefStructure, ScheduledStopPoint, \
    RouteLink, Route, Quay, QuayRefStructure, StopPlaceRefStructure, StopPlace, TimingPoint, TimingPointRefStructure, \
    ServiceLink, ServiceLinkRefStructure, TimingLink, TimingLinkRefStructure, Locale, LocaleStructure, OperatorRef, \
    DayTypeRef, DayTypesInFrameRelStructure, DayTypeRefsRelStructure, ValidityConditionsRelStructure, \
    UicOperatingPeriodRef, OperatingPeriodRef, LineRef, QuayRef, ScheduledStopPointRef

from netexio.dbaccess import get_single

def ref_version_hash(self):
    return hash(self.ref + ';' + self.version)

VersionOfObjectRefStructure.__hash__ = ref_version_hash
ServiceJourneyRef.__hash__ = ref_version_hash
ServiceJourneyPatternRef.__hash__ = ref_version_hash
OperatorRef.__hash__ = ref_version_hash
DayTypeRef.__hash__ = ref_version_hash
OperatingPeriodRef.__hash__ = ref_version_hash
UicOperatingPeriodRef.__hash__ = ref_version_hash
LineRef.__hash__ = ref_version_hash
QuayRef.__hash__ = ref_version_hash
ScheduledStopPointRef.__hash__ = ref_version_hash

# TODO: the following hashes us version or 'any' to overcome (invalid) None situations, it would be better if we could create hashes that would capture the true NeTEx-any situation
def day_type_refs_hash(self: DayTypeRefsRelStructure):
    return hash('\n'.join([dtr.ref + ';' + (dtr.version or 'any') for dtr in self.day_type_ref]))

DayTypeRefsRelStructure.__hash__ = day_type_refs_hash

def vc_refs_hash(self: ValidityConditionsRelStructure):
    refs = []
    for vc in self.choice:
        if hasattr(vc, 'id'):
            refs.append(vc.id + ';' + (vc.version or 'any'))
        elif hasattr(vc, 'ref'):
            refs.append(vc.ref + ';' + (vc.version or 'any'))

    return hash('\n'.join(refs))

ValidityConditionsRelStructure.__hash__ = vc_refs_hash


def id_version_hash(self):
    return hash(self.id + ';' + (self.version or 'any'))

ServiceJourney.__hash__ = id_version_hash
ServiceJourneyPattern.__hash__ = id_version_hash

# First monkey patching test
def get_route(self, con) -> Route:
    return get_single(con, Route, self.ref, self.version)

RouteRefStructure.get = get_route

def get_routelink(self, con) -> RouteLink:
    return get_single(con, RouteLink, self.ref, self.version)

RouteLinkRefStructure.get = get_routelink

def get_scheduledstoppoint(self, con) -> ScheduledStopPoint:
    return get_single(con, ScheduledStopPoint, self.ref, self.version)

ScheduledStopPointRefStructure.get = get_scheduledstoppoint

def get_quay(self, con) -> Quay:
    return get_single(con, Quay, self.ref, self.version)

QuayRefStructure.get = get_quay

def get_stopplace(self, con) -> StopPlace:
    return get_single(con, StopPlace, self.ref, self.version)

StopPlaceRefStructure.get = get_stopplace


def get_timingpoint(self, con) -> TimingPoint | ScheduledStopPoint:
    if self.name_of_ref_class == 'TimingPoint':
        return get_single(con, TimingPoint, self.ref, self.version)
    elif  self.name_of_ref_class == 'ScheduledStopPoint':
        return get_single(con, ScheduledStopPoint, self.ref, self.version)
    else:
        timing_point = get_single(con, TimingPoint, self.ref, self.version)
        if timing_point is not None:
            return timing_point
        else:
            return get_single(con, ScheduledStopPoint, self.ref, self.version)

TimingPointRefStructure.get = get_timingpoint

def get_servicelink(self, con) -> ServiceLink:
    return get_single(con, ServiceLink, self.ref, self.version)

ServiceLinkRefStructure.get = get_servicelink

def get_timinglink(self, con) -> TimingLink:
    return get_single(con, TimingLink, self.ref, self.version)

TimingLinkRefStructure.get = get_timinglink

def hash_locale(self):
    return hash((self.time_zone_offset, self.time_zone, self.summer_time_zone_offset, self.summer_time_zone, self.default_language,))

Locale.__hash__ = hash_locale
LocaleStructure.__hash__ = hash_locale
