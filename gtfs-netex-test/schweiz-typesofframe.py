from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from netex import TypeOfFrame, MultilingualString, ClassRefStructure, ClassesInRepositoryRelStructure, ClassInFrame, \
    MandatoryEnumeration, ClassRefTypeEnumeration, ValueSet, TypesOfValueStructure, GeneralFrame, \
    GeneralFrameMembersRelStructure, PublicationDelivery, ParticipantRef, DataObjectsRelStructure

types_of_frame = ValueSet(version="1.10", id="ch:ValueSet:TypesOfSpecificFrame",
         class_of_values="TypeOfFrame", name=MultilingualString(value="Types of Schweiz Frames"),
         values=TypesOfValueStructure(type_of_value_or_type_of_entity=[
             TypeOfFrame(id='ch:TypeOfFrame:COMMON', version='1.10',
                         name=MultilingualString(value="Schweiz Common"),
                         frame_class_ref=ClassRefStructure(name_of_class="CompositeFrame"),
                         classes=ClassesInRepositoryRelStructure(class_in_frame_ref_or_class_in_frame=[
                             ClassInFrame(name_of_class="TimetableFrame",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.ALL,
                                          type_of_frame_ref="ch:TypeOfFrame:COMMONFRAME"
                                          )
                         ])),

             TypeOfFrame(id='ch:TypeOfFrame:COMMONFRAME', version='1.10',
                         name=MultilingualString(value="Schweiz Common TimetableFrame"),
                         frame_class_ref=ClassRefStructure(name_of_class="TimetableFrame"),
                         classes=ClassesInRepositoryRelStructure(class_in_frame_ref_or_class_in_frame=[
                             ClassInFrame(name_of_class="ServiceFacilitySet",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                          ),
                             ClassInFrame(name_of_class="TypeOfService",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                          ),
                             ClassInFrame(name_of_class="JourneyMeeting",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                          ),
                             ClassInFrame(name_of_class="InterchangeRule",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                          )
                         ])),

             TypeOfFrame(id='ch:TypeOfFrame:RESOURCE', version='1.10',
                         name=MultilingualString(value="Schweiz Resource"),
                         frame_class_ref=ClassRefStructure(name_of_class="CompositeFrame"),
                         classes=ClassesInRepositoryRelStructure(class_in_frame_ref_or_class_in_frame=[
                             ClassInFrame(name_of_class="ResourceFrame",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.ALL,
                                          type_of_frame_ref="ch:TypeOfFrame:RESOURCEFRAME"
                                          )
                         ])),

             TypeOfFrame(id='ch:TypeOfFrame:RESOURCEFRAME', version='1.10',
                         name=MultilingualString(value="Schweiz ResourceFrame"),
                         frame_class_ref=ClassRefStructure(name_of_class="ServiceFrame"),
                         classes=ClassesInRepositoryRelStructure(class_in_frame_ref_or_class_in_frame=[
                             ClassInFrame(name_of_class="ResponsibilitySet",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                          ),
                             ClassInFrame(name_of_class="TypeOfProductCategory",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                          ),
                             ClassInFrame(name_of_class="Operator",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                          ),
                             ClassInFrame(name_of_class="VehicleType",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                          )
                         ])),

             TypeOfFrame(id='ch:TypeOfFrame:SERVICE', version='1.10',
                        name=MultilingualString(value="Schweiz Service"),
                        frame_class_ref=ClassRefStructure(name_of_class="CompositeFrame"),
                        classes=ClassesInRepositoryRelStructure(class_in_frame_ref_or_class_in_frame=[
                            ClassInFrame(name_of_class="ServiceFrame",
                                         mandatory=MandatoryEnumeration.REQUIRED,
                                         class_ref_type=ClassRefTypeEnumeration.ALL,
                                         type_of_frame_ref="ch:TypeOfFrame:SERVICEFRAME"
                                         )
                        ])),

            TypeOfFrame(id='ch:TypeOfFrame:SERVICEFRAME', version='1.10',
                      name=MultilingualString(value="Schweiz ServiceFrame"),
                      frame_class_ref=ClassRefStructure(name_of_class="ServiceFrame"),
                      classes=ClassesInRepositoryRelStructure(class_in_frame_ref_or_class_in_frame=[
                          ClassInFrame(name_of_class="Direction",
                                       mandatory=MandatoryEnumeration.REQUIRED,
                                       class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                       ),
                          ClassInFrame(name_of_class="Line",
                                       mandatory=MandatoryEnumeration.REQUIRED,
                                       class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                       ),
                          ClassInFrame(name_of_class="DestinationDisplay",
                                       mandatory=MandatoryEnumeration.REQUIRED,
                                       class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                       ),
                          ClassInFrame(name_of_class="ScheduledStopPoint",
                                       mandatory=MandatoryEnumeration.REQUIRED,
                                       class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                       ),
                          ClassInFrame(name_of_class="DefaultConnection",
                                       mandatory=MandatoryEnumeration.REQUIRED,
                                       class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                       ),
                          ClassInFrame(name_of_class="SiteConnection",
                                       mandatory=MandatoryEnumeration.REQUIRED,
                                       class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                       ),
                          ClassInFrame(name_of_class="PassengerStopAssignment",
                                       mandatory=MandatoryEnumeration.REQUIRED,
                                       class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                       ),
                          ClassInFrame(name_of_class="Notice",
                                       mandatory=MandatoryEnumeration.REQUIRED,
                                       class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                       )
                      ])),

             TypeOfFrame(id='ch:TypeOfFrame:SERVICECALENDAR', version='1.10',
                         name=MultilingualString(value="Schweiz ServiceCalendar"),
                         frame_class_ref=ClassRefStructure(name_of_class="CompositeFrame"),
                         classes=ClassesInRepositoryRelStructure(class_in_frame_ref_or_class_in_frame=[
                             ClassInFrame(name_of_class="ServiceCalendarFrame",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.ALL,
                                          type_of_frame_ref="ch:TypeOfFrame:SERVICECALENDARFRAME"
                                          )
                         ])),

             TypeOfFrame(id='ch:TypeOfFrame:SERVICECALENDARFRAME', version='1.10',
                         name=MultilingualString(value="Schweiz ServiceCalendarFrame"),
                         frame_class_ref=ClassRefStructure(name_of_class="ServiceCalenderFrame"),
                         classes=ClassesInRepositoryRelStructure(class_in_frame_ref_or_class_in_frame=[
                             ClassInFrame(name_of_class="AvailabilityConditions",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                          ),
                             ClassInFrame(name_of_class="ServiceCalendar",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                          ),
                             ClassInFrame(name_of_class="DayType",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                          ),
                             ClassInFrame(name_of_class="Timeband",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                          ),
                         ])),

             TypeOfFrame(id='ch:TypeOfFrame:SITE', version='1.10',
                         name=MultilingualString(value="Schweiz Site"),
                         frame_class_ref=ClassRefStructure(name_of_class="CompositeFrame"),
                         classes=ClassesInRepositoryRelStructure(class_in_frame_ref_or_class_in_frame=[
                             ClassInFrame(name_of_class="ServiceCalendarFrame",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.ALL,
                                          type_of_frame_ref="ch:TypeOfFrame:SITEFRAME"
                                          )
                         ])),

             TypeOfFrame(id='ch:TypeOfFrame:SITEFRAME', version='1.10',
                         name=MultilingualString(value="Schweiz SiteFrame"),
                         frame_class_ref=ClassRefStructure(name_of_class="SiteFrame"),
                         classes=ClassesInRepositoryRelStructure(class_in_frame_ref_or_class_in_frame=[
                             ClassInFrame(name_of_class="TopographicPlace",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                          ),
                             ClassInFrame(name_of_class="StopPlace",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                          ),
                         ])),

             TypeOfFrame(id='ch:TypeOfFrame:TIMETABLE', version='1.10',
                         name=MultilingualString(value="Schweiz Timetable"),
                         frame_class_ref=ClassRefStructure(name_of_class="CompositeFrame"),
                         classes=ClassesInRepositoryRelStructure(class_in_frame_ref_or_class_in_frame=[
                             ClassInFrame(name_of_class="TimetableFrame",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.ALL,
                                          type_of_frame_ref="ch:TypeOfFrame:TIMETABLEFRAME"
                                          )
                         ])),

             TypeOfFrame(id='ch:TypeOfFrame:TIMETABLEFRAME', version='1.10',
                         name=MultilingualString(value="Schweiz TimetableFrame"),
                         frame_class_ref=ClassRefStructure(name_of_class="TimetableFrame"),
                         classes=ClassesInRepositoryRelStructure(class_in_frame_ref_or_class_in_frame=[
                             ClassInFrame(name_of_class="ServiceJourney",
                                          mandatory=MandatoryEnumeration.REQUIRED,
                                          class_ref_type=ClassRefTypeEnumeration.MEMBERS,
                                          ),
                         ])),
         ])
         )

general_frame = GeneralFrame(id="ch:GeneralFrame:TypeOfFrame", version="1.10",
                             members=GeneralFrameMembersRelStructure(choice=types_of_frame.values.type_of_value_or_type_of_entity))

publication_delivery = PublicationDelivery(
            publication_timestamp=XmlDateTime.now(),
            participant_ref=ParticipantRef(value="NDOV"),
            description=MultilingualString(value="Schweiz TypeOfFrame"),
            data_objects=DataObjectsRelStructure(choice=[general_frame]),
            version="ntx:1.1",
        )

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

ns_map={'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

with open('netex-output/schweiz-typesofframe.xml', 'w') as out:
    serializer.write(out, publication_delivery, ns_map)

type_of_frames = {x.id: x for x in types_of_frame.values.type_of_value_or_type_of_entity}