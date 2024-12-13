from netex import ServiceJourney, ValidityConditionsRelStructure, AvailabilityCondition
from transformers.references import replace_with_reference_inplace
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

sj = ServiceJourney(id="test", version="1", validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=[AvailabilityCondition(id="test2", version="1")])])

print(serializer.render(sj))

replace_with_reference_inplace(sj, "validity_conditions_or_valid_between.0.choice.0")

print(serializer.render(sj))