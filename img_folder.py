import os
import shutil

def copy_and_rename_images_from_folder(source_root, target_directory):
    """Copy images from the source directory structure to target directory and rename them."""
    
    # Ensure the target directory exists
    os.makedirs(target_directory, exist_ok=True)

    # List of copied files
    copied_files = []

    set_list = sorted(os.listdir(source_root))

    for set_name in set_list:
        v_list = sorted(os.listdir(os.path.join(source_root, set_name)))
        for v_name in v_list:
            file_path = os.path.join(source_root, set_name, v_name, 'visible')
            for filename in os.listdir(file_path):
                source_filepath = os.path.join(file_path, filename)
                new_filename = f"{set_name}_{v_name}_{filename}"
                target_filepath = os.path.join(target_directory, new_filename)
                shutil.copy2(source_filepath, target_filepath)
                copied_files.append(target_filepath)

    return copied_files

# Source root directory path
source_root = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/images"

# Target directory path where the images will be copied
target_directory = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/img_split/visible"

# Execute the function
copied_files = copy_and_rename_images_from_folder(source_root, target_directory)


def copy_and_rename_images_from_folder(source_root, target_directory):
    """Copy images from the source directory structure to target directory and rename them."""
    
    # Ensure the target directory exists
    os.makedirs(target_directory, exist_ok=True)

    # List of copied files
    copied_files = []

    set_list = sorted(os.listdir(source_root))

    for set_name in set_list:
        v_list = sorted(os.listdir(os.path.join(source_root, set_name)))
        for v_name in v_list:
            file_path = os.path.join(source_root, set_name, v_name, 'lwir')
            for filename in os.listdir(file_path):
                source_filepath = os.path.join(file_path, filename)
                new_filename = f"{set_name}_{v_name}_{filename}"
                target_filepath = os.path.join(target_directory, new_filename)
                shutil.copy2(source_filepath, target_filepath)
                copied_files.append(target_filepath)

    return copied_files

# Source root directory path
source_root = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/images"

# Target directory path where the images will be copied
target_directory = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/img_split/infrared"

# Execute the function
copied_files = copy_and_rename_images_from_folder(source_root, target_directory)