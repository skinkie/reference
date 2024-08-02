from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class JourneyRelationTypeEnumeration(Enum):
    CONTINUATION_OF_JOURNEY = "ContinuationOfJourney"
    CONTINUED_BY_JOURNEY = "ContinuedByJourney"
    SPLITS_INTO_JOURNEYS = "SplitsIntoJourneys"
    CONTINUATION_OF_SPLIT_JOURNEY = "ContinuationOfSplitJourney"
    JOINING_OF_JOURNEYS = "JoiningOfJourneys"
    CONTINUED_BY_JOINED_JOURNEY = "ContinuedByJoinedJourney"
    REPLACEMENT_OF_JOURNEY = "ReplacementOfJourney"
    REPLACED_BY_JOURNEY = "ReplacedByJourney"
    SUPPORT_OF_JOURNEY = "SupportOfJourney"
    SUPPORTED_BY_JOURNEY = "SupportedByJourney"
