from xsdata.models.datatype import XmlTime, XmlDateTime

from anytodutch import timeZoneConversion
from netex import ServiceJourney, AvailabilityCondition, ValidityConditionsRelStructure
import pytz

from refs import getRef

original_departure_time = XmlTime(10, 0, 0)
ac = AvailabilityCondition(id="test", from_date=XmlDateTime(2023, 12, 9, 0, 0, 0), to_date=XmlDateTime(2023, 12, 9, 0, 0, 0))
sj = ServiceJourney(id="test", departure_time=original_departure_time, validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=[getRef(ac)])])
timeZoneConversion(sj, {x.id: x for x in [ac]}, pytz.timezone("UTC"), pytz.timezone("Europe/Amsterdam"))
print(str(original_departure_time) + ' -> ' + str(sj.departure_time) + ' ' + str(sj.departure_day_offset))

ac = AvailabilityCondition(id="test", from_date=XmlDateTime(2023, 10, 20, 0, 0, 0), to_date=XmlDateTime(2023, 12, 9, 0, 0, 0))
sj = ServiceJourney(id="test", departure_time=original_departure_time, validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=[getRef(ac)])])
timeZoneConversion(sj, {x.id: x for x in [ac]}, pytz.timezone("UTC"), pytz.timezone("Europe/Amsterdam"))
print(str(original_departure_time) + ' -> ' + str(sj.departure_time) + ' ' + str(sj.departure_day_offset))


# Test departure day offset
original_departure_time = XmlTime(22, 0, 0)
ac = AvailabilityCondition(id="test", from_date=XmlDateTime(2023, 9, 20, 0, 0, 0), to_date=XmlDateTime(2023, 9, 22, 0, 0, 0))
sj = ServiceJourney(id="test", departure_time=original_departure_time, validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=[getRef(ac)])])
timeZoneConversion(sj, {x.id: x for x in [ac]}, pytz.timezone("UTC"), pytz.timezone("Europe/Amsterdam"))
print(str(original_departure_time) + ' -> ' + str(sj.departure_time) + ' ' + str(sj.departure_day_offset))


ac = AvailabilityCondition(id="test", from_date=XmlDateTime(2023, 10, 29, 0, 0, 0), to_date=XmlDateTime(2023, 10, 30, 0, 0, 0))
sj = ServiceJourney(id="test", departure_time=original_departure_time, validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=[getRef(ac)])])
timeZoneConversion(sj, {x.id: x for x in [ac]}, pytz.timezone("UTC"), pytz.timezone("Europe/Amsterdam"))
print(str(original_departure_time) + ' -> ' + str(sj.departure_time) + ' ' + str(sj.departure_day_offset))
