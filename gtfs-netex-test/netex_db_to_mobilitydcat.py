from owlready2 import get_ontology

# Main ontology to load
MAIN_ONTOLOGY_URL = "https://mobilitydcat-ap.github.io/mobilityDCAT-AP/releases/serialisationFiles/mobilitydcat-ap.rdf"

# Load the main ontology
onto = get_ontology(MAIN_ONTOLOGY_URL).load()

# Track external ontologies that this one relies on
extra_ontologies = set()

# Collect all properties and classes
object_properties = list(onto.object_properties())
datatype_properties = list(onto.data_properties())
all_classes = list(onto.classes())
all_properties = object_properties + datatype_properties

# Detect external ontologies by checking property ranges
for prop in all_properties:
    for cls in prop.range:
        if cls.ontology != onto:  # If the class belongs to another ontology
            extra_ontologies.add(cls.ontology.base_iri)

# Load external ontologies
for extra_iri in extra_ontologies:
    get_ontology(extra_iri).load()

# Generate Python module
with open("dcat_ontology.py", "w") as f:
    f.write("from owlready2 import *\n\n")

    # Load main and extra ontologies in the generated module
    f.write(f"onto = get_ontology(\"{MAIN_ONTOLOGY_URL}\").load()\n")
    for extra_iri in extra_ontologies:
        f.write(f"get_ontology(\"{extra_iri}\").load()\n")

    f.write("\n")

    # Generate all classes
    for cls in all_classes:
        class_name = cls.name.replace(".", "_")  # Ensure valid Python identifiers
        f.write(f"class {class_name}(Thing):\n")
        f.write(f"    ontology = onto\n")

        # Get properties that reference this class in their domain
        class_props = [prop for prop in all_properties if cls in prop.domain]

        # Include properties in the class definition
        for prop in class_props:
            f.write(f"    {prop.name} = onto.{prop.name}  # {prop.iri}\n")

        f.write("\n")

    # Write all ObjectProperties
    f.write("# Object Properties\n")
    for prop in object_properties:
        f.write(f"{prop.name} = onto.{prop.name}  # {prop.iri}\n")

    f.write("\n")

    # Write all DatatypeProperties
    f.write("# Datatype Properties\n")
    for prop in datatype_properties:
        f.write(f"{prop.name} = onto.{prop.name}  # {prop.iri}\n")

    f.write("\n")
