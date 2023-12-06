from typing import List

from xsdata.models.datatype import XmlTime

from GtfsNeTEx import date_to_xmldatetime, gtfs_date
from netex import AvailabilityCondition, Codespace, ServiceJourney, ValidityConditionsRelStructure, Version, \
    PrivateCode, TimeDemandTypeRef, TimeDemandType, ServiceJourneyPatternRef, ServiceJourneyPattern
from refs import getBitString2, getId, getRef


class SimpleTimetable:
    codespace: Codespace
    version: Version

    def __init__(self, codespace, version):
        self.codespace = codespace
        self.version = version


    def simple_timetable(self, filename) -> (List[ServiceJourney], List[AvailabilityCondition]):
        simple_timetable = {}
        import csv
        with open(filename, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                if line['from'] == 'Texel':
                    line['from'] = 'TX'
                elif line['from'] == 'Den Helder':
                    line['from'] = 'DH'
                if line['to'] == 'Texel':
                    line['to'] = 'TX'
                elif line['to'] == 'Den Helder':
                    line['to'] = 'DH'

                key = '_'.join([line['from'], line['to'], line['time']])
                operating_dates = simple_timetable.get(key, [])
                operating_dates.append(gtfs_date(line['date'].replace('-', '')))
                simple_timetable[key] = operating_dates


        availability_conditions = {}
        sjs = []

        for key, operating_dates in simple_timetable.items():
            from_ssp, to_ssp, time = key.split('_')
            ac_hash = hash(tuple(operating_dates))
            ac_hash = ("%0.2X" % (ac_hash**2))[0:8]
            ac = availability_conditions.get(ac_hash, None)
            if ac is None:
                od = sorted(operating_dates)
                ac = AvailabilityCondition(
                    id=getId(AvailabilityCondition, self.codespace, str(ac_hash)),
                    version=self.version.version, is_available=True,
                    from_date=date_to_xmldatetime(od[0]),
                    to_date=date_to_xmldatetime(od[-1]),
                    valid_day_bits=getBitString2(od))
                availability_conditions[str(ac_hash)] = ac

            sj = ServiceJourney(id=getId(ServiceJourney, self.codespace, key), version=self.version.version,
                                private_code=PrivateCode(type_value="JourneyNumber", value="{:04d}".format(int(time.replace(':', '')))),
                                time_demand_type_ref=TimeDemandTypeRef(ref=getId(TimeDemandType, self.codespace, '-'.join([from_ssp, to_ssp])), version=self.version.version),
                                choice=ServiceJourneyPatternRef(ref=getId(ServiceJourneyPattern, self.codespace, '-'.join([from_ssp, to_ssp])), version=self.version.version),
                                departure_time=XmlTime(hour=int(time[0:2]), minute=int(time[3:5]), second=0),
                           validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=getRef(ac))])

            sjs.append(sj)

        return (sjs, list(availability_conditions.values()))


# stt = SimpleTimetable(Codespace(id="test", xmlns="test"), Version(id="1", version="1"))
# stt.simple_timetable('../teso/scrape-output/teso-20231129.csv')