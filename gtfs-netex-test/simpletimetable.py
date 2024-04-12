from typing import List

from xsdata.models.datatype import XmlTime, XmlDuration

from GtfsNeTEx import date_to_xmldatetime, gtfs_date
from netex import AvailabilityCondition, Codespace, ServiceJourney, ValidityConditionsRelStructure, Version, \
    PrivateCode, TimeDemandTypeRef, TimeDemandType, ServiceJourneyPatternRef, ServiceJourneyPattern, \
    JourneyRunTimesRelStructure, JourneyRunTime, VehicleTypeRef, VehicleType, TimingLinkRef, TimingLink
from refs import getBitString2, getId, getRef


class SimpleTimetable:
    codespace: Codespace
    version: Version

    def __init__(self, codespace, version):
        self.codespace = codespace
        self.version = version

    # Handle trips with the same arrival station, and same arrival time
    def simple_timetable2(self, filename) -> (List[ServiceJourney], List[AvailabilityCondition], List[TimeDemandType]):
        simple_timetable = {}
        import csv
        with open(filename, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                orig_from = line['from']

                if line['from'] == 'H' or line['from'] == 'T':
                    line['from'] += line['to']

                if line['to'] == 'H' or line['to'] == 'T':
                    line['to'] += orig_from

                operating_date, departure = line['departure'].split('T')
                departure = departure.split('+')[0]

                key = '_'.join([line['from'], line['to'], departure, line['duration'], line['vessel']])
                operating_dates = simple_timetable.get(key, [])
                operating_dates.append(gtfs_date(operating_date.replace('-', '')))
                simple_timetable[key] = operating_dates

        availability_conditions = {}
        tdts = {}
        sjs = []

        for key, operating_dates in simple_timetable.items():
            from_ssp, to_ssp, time, duration, vessel = key.split('_')
            ac_hash = hash(tuple(operating_dates)) # TODO replace with hashlib.sha256
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


            tdt_key = '-'.join([from_ssp, to_ssp, duration])
            duration_secs = int(duration) * 60

            tdt = TimeDemandType(id=getId(TimeDemandType, self.codespace, tdt_key), version=self.version.version,
                           run_times=JourneyRunTimesRelStructure(
                               journey_run_time=[JourneyRunTime(id=getId(JourneyRunTime, self.codespace, '-'.join([from_ssp, to_ssp, duration])),
                                                                version=self.version.version,
                                                                timing_link_ref=TimingLinkRef(ref=getId(TimingLink, self.codespace, '-'.join([from_ssp, to_ssp])), version=self.version.version),
                                                                run_time=XmlDuration(f"PT{duration_secs}S"))]))
            tdts[tdt_key] = tdt


            sj = ServiceJourney(id=getId(ServiceJourney, self.codespace, key), version=self.version.version,
                                private_code=PrivateCode(type_value="JourneyNumber", value="{:04d}".format(int(time.replace(':', '')))),
                                time_demand_type_ref=getRef(tdt),
                                journey_pattern_ref=ServiceJourneyPatternRef(ref=getId(ServiceJourneyPattern, self.codespace, '-'.join([from_ssp, to_ssp])), version=self.version.version),
                                departure_time=XmlTime(hour=int(time[0:2]), minute=int(time[3:5]), second=0),
                                vehicle_type_ref=VehicleTypeRef(ref=getId(VehicleType, self.codespace, vessel), version=self.version.version),
                           validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=getRef(ac))])

            sjs.append(sj)



        return (sjs, list(availability_conditions.values()), list(tdts.values()))



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
                                journey_pattern_ref=ServiceJourneyPatternRef(ref=getId(ServiceJourneyPattern, self.codespace, '-'.join([from_ssp, to_ssp])), version=self.version.version),
                                departure_time=XmlTime(hour=int(time[0:2]), minute=int(time[3:5]), second=0),
                           validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=getRef(ac))])

            sjs.append(sj)

        return (sjs, list(availability_conditions.values()))


# stt = SimpleTimetable(Codespace(id="test", xmlns="test"), Version(id="1", version="1"))
# stt.simple_timetable('../teso/scrape-output/teso-20231129.csv')