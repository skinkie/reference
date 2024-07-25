import duckdb as sqlite3
from typing import Iterable, Dict, Generator, Set

from netexio.dbaccess import write_objects, load_generator, update_generator, load_local
from netex import ServiceJourneyPattern, Direction, MultilingualString, ResponsibilitySet, ResponsibilityRoleAssignment, \
    StakeholderRoleTypeEnumeration, Line, Operator, OperatorRef, ServiceJourney, TemplateServiceJourney, LineRef
from refs import getId, getRef, getIndex

from utils import project

import netex_monkeypatching


def infer_operator_from_responsibilityset_and_apply(read_database, write_database, generator_defaults: dict):
    line_ref_to_operator_ref: Dict[str, OperatorRef] = {}
    mapping: Dict[str, OperatorRef] = {}

    def process_line(object: Line|ServiceJourney|TemplateServiceJourney):
        if object.operator_ref is None:
            if object.responsibility_set_ref_attribute is not None and object.responsibility_set_ref_attribute in mapping:
                object.operator_ref = mapping[object.responsibility_set_ref_attribute]
                return object
            elif object.id in line_ref_to_operator_ref:
                object.operator_ref = line_ref_to_operator_ref[object.id]
                return object

    def process_journey(object: ServiceJourney|TemplateServiceJourney):
        changed = False
        if object.operator_ref_or_operator_view is None and object.responsibility_set_ref_attribute is not None and object.responsibility_set_ref_attribute in mapping:
            object.operator_ref_or_operator_view = mapping[object.responsibility_set_ref_attribute]
            changed = True

        if object.operator_ref_or_operator_view is not None and object.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view is not None and hasattr(object.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view, 'ref'):
            line_ref_to_operator_ref[object.flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view.ref] = mapping[object.responsibility_set_ref_attribute]

        if changed:
            return object

    def query1(read_con) -> Generator:
        _load_generator = load_generator(read_con, Line)
        for line in _load_generator:
            new_line = process_line(line)
            if new_line is not None:
                yield new_line

    def query2(read_con) -> Generator:
        _load_generator = load_generator(read_con, ServiceJourney)
        for service_journey in _load_generator:
            new_service_journey = process_journey(service_journey)
            if new_service_journey is not None:
                yield new_service_journey

    def query3(read_con) -> Generator:
        _load_generator = load_generator(read_con, TemplateServiceJourney)
        for template_service_journey in _load_generator:
            new_template_service_journey = process_journey(template_service_journey)
            if new_template_service_journey is not None:
                yield new_template_service_journey


    # TODO: Make the database access pattern generic.
    with sqlite3.connect(write_database) as write_con:
        if write_database == read_database:
            read_con = write_con
        else:
            read_con = sqlite3.connect(read_database, read_only=True)

        _mapping: Dict[str, Set] = {}
        # operators = getIndex(load_local(read_con, Operator))
        for responsibility_set in load_local(read_con, ResponsibilitySet):
            _mapping[responsibility_set.id] = set([])
            for role_assignment in responsibility_set.roles.responsibility_role_assignment:
                if StakeholderRoleTypeEnumeration.OPERATION in role_assignment.stakeholder_role_type or StakeholderRoleTypeEnumeration.OPERATION_1 in role_assignment.stakeholder_role_type:
                    _mapping[responsibility_set.id].add(project(role_assignment.responsible_organisation_ref, OperatorRef))

        mapping = {x: y.pop() for x, y in _mapping.items() if len(y) == 1}
        # Maybe Authority too?

        update_generator(write_con, ServiceJourney, query2(read_con))
        update_generator(write_con, TemplateServiceJourney, query3(read_con))
        update_generator(write_con, Line, query1(read_con))

