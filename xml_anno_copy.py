import os
import shutil
import xml.etree.ElementTree as ET

def copy_xml_files_with_object_modified(directory, target_directory, set_name="", v_name=""):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    files_copied = []

    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            filepath = os.path.join(directory, filename)
            
            # Parse the XML file
            tree = ET.parse(filepath)
            root = tree.getroot()
            
            # Check for the presence of 'object' tags
            object_tags = root.findall(".//object")
            
            # If 'object' tags are found, copy the file to the target directory
            if object_tags:
                # Modify the filename to the desired format
                new_filename = f"{set_name}_{v_name}_{filename}"
                target_path = os.path.join(target_directory, new_filename)
                
                shutil.copy2(filepath, target_path)
                files_copied.append(new_filename)

    return files_copied

path = '/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/annotations-xml-new-sanitized/'
set_list = sorted(os.listdir(path))
all_copied_files = []

for set_name in set_list:
    v_list = sorted(os.listdir(path + set_name + '/'))
    for v_name in v_list:
        file_path = path + set_name + '/' + v_name + '/'
        copied_files = copy_xml_files_with_object_modified(file_path, "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/annotations-xml-anno", set_name, v_name)
        all_copied_files.extend(copied_files)

