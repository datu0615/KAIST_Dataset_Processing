import os
import shutil
import xml.etree.ElementTree as ET

def remove_objects_with_class_and_delete_empty_files(directory, target_class):
    modified_files = []
    deleted_files = []

    # Iterate over all XML files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            filepath = os.path.join(directory, filename)
            
            # Parse the XML file
            tree = ET.parse(filepath)
            root = tree.getroot()
            
            # Check for objects with the target class and remove them
            objects_to_remove = []
            for obj in root.findall("object"):
                class_name = obj.find("name").text
                if class_name == target_class:
                    objects_to_remove.append(obj)

            # If any objects are removed, modify the XML and save it
            if objects_to_remove:
                for obj in objects_to_remove:
                    root.remove(obj)
                # If no 'object' tags are left, delete the file
                if not root.findall("object"):
                    os.remove(filepath)
                    deleted_files.append(filename)
                else:
                    tree.write(filepath)
                    modified_files.append(filename)

    return modified_files, deleted_files

# Remove objects with the class "person?" in the XML files in the /mnt/data directory
# and delete files if they have no 'object' tags left
modified_xml_files, deleted_xml_files = remove_objects_with_class_and_delete_empty_files("/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/annotations-xml-anno", "person?")

modified_xml_files, deleted_xml_files
