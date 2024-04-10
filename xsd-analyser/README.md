# Generate the XML Schema
xsdata -p xsd --kw-only -ss clusters --compound-fields XMLSchema.xsd

# Generate the NeTEx Schema
xsdata -p netex --kw-only -ss clusters --compound-fields /home/skinkie/Sources/NeTEx/xsd/NeTEx_publication.xsd

# Start the analyser

The analyser grabs all xpath selectors.
Using MRO it grabs all the generated NeTEx Python classes, and makes sure the correct name is found.
By subtracting the netexclasses, from the xpath selectors we can find which xpath selectors are not part of the schema.
