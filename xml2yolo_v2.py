import os
import shutil
import xml.etree.ElementTree as ET

def convert_xml_to_txt_updated_corrected(xml_filepath, output_directory):
    # Class to ID mapping
    class_to_id = {
        "cyclist": "0",
        "people": "1",
        "person": "2"
    }
    
    # Parse the XML file
    tree = ET.parse(xml_filepath)
    root = tree.getroot()

    # Extract image dimensions
    image_size = root.find("size")
    image_width = int(image_size.find("width").text)
    image_height = int(image_size.find("height").text)

    # Extract bounding box details
    objects = root.findall("object")

    txt_content = []

    for obj in objects:
        # Extract class name and map to class ID
        class_name = obj.find("name").text
        class_id = class_to_id.get(class_name, "0")  # Default to 0 if class name is not recognized
        
        bbox = obj.find("bndbox")
        x = float(bbox.find("x").text)
        y = float(bbox.find("y").text)
        w = float(bbox.find("w").text)
        h = float(bbox.find("h").text)

        # Convert to x_min, y_min, x_max, y_max format
        x_min = x
        y_min = y
        x_max = x + w
        y_max = y + h

        # Calculate x_center, y_center, width, and height (normalized)
        x_center = (x_min + x_max) / (2 * image_width)
        y_center = (y_min + y_max) / (2 * image_height)
        width = (x_max - x_min) / image_width
        height = (y_max - y_min) / image_height

        # Append to txt_content
        txt_content.append(f"{class_id} {x_center} {y_center} {width} {height}")

    # Save to a txt file with the same name
    output_filepath = os.path.join(output_directory, os.path.basename(xml_filepath).replace(".xml", ".txt"))
    with open(output_filepath, "w") as txt_file:
        txt_file.write("\n".join(txt_content))

    return output_filepath


def convert_all_xml_in_folder(source_directory, output_directory):
    """Convert all XML files in the specified directory to TXT format."""
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # List of converted txt files
    converted_files = []

    # Iterate over all XML files in the source directory
    for filename in os.listdir(source_directory):
        if filename.endswith(".xml"):
            xml_filepath = os.path.join(source_directory, filename)
            converted_txt_filepath = convert_xml_to_txt_updated_corrected(xml_filepath, output_directory)
            converted_files.append(converted_txt_filepath)

    return converted_files

# Source directory containing the XML files
source_directory = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/annotations-xml-anno"

# Output directory where the converted txt files will be saved
output_directory = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/annotations-txt-anno"

# Convert all XML files in the source directory
converted_files = convert_all_xml_in_folder(source_directory, output_directory)

# Print the list of converted txt files
print(converted_files)