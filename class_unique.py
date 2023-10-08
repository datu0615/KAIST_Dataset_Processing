import os
import shutil
import xml.etree.ElementTree as ET

def extract_classes_from_xml(directory):
    unique_classes = set()

    # Iterate over all XML files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            filepath = os.path.join(directory, filename)
            
            # Parse the XML file
            tree = ET.parse(filepath)
            root = tree.getroot()
            
            # Extract class names from the XML
            for obj in root.findall("object"):
                class_name = obj.find("name").text
                unique_classes.add(class_name)

    return sorted(list(unique_classes))

# Extract unique classes from the XML files in the /mnt/data directory
extracted_classes = extract_classes_from_xml("/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/annotations-xml-anno")

print(extracted_classes)

