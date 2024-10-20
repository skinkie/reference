import os
import gzip
import shutil

input_dir = r"D:\it"
output_dir = r"D:\it\xml"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".gz"):
        file_path = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + ".xml")

        # Open the gzip file and extract the XML content
        with gzip.open(file_path, "rb") as gz_file:
            with open(output_file, "wb") as xml_file:
                shutil.copyfileobj(gz_file, xml_file)

        print(f"Extracted XML file: {output_file}")

print("Extraction completed.")