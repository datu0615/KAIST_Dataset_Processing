import os
import shutil

def read_txt_file(txt_filepath):
    """Read the txt file and return the list of image filenames."""
    with open(txt_filepath, 'r') as file:
        image_filenames = [line.strip() for line in file.readlines()]
    return image_filenames

def move_annotations_based_on_txt(txt_filepaths, annotation_directory):
    """Move annotation txt files based on the provided image txt files to train or test subdirectories."""
    
    # Read image filenames from txt files
    listed_train_images = read_txt_file(txt_filepaths[0])  # Assuming the first txt is for training
    listed_test_images = read_txt_file(txt_filepaths[1])   # Assuming the second txt is for testing
    
    # Ensure the train and test subdirectories exist
    train_subdir = os.path.join(annotation_directory, 'train')
    test_subdir = os.path.join(annotation_directory, 'test')
    os.makedirs(train_subdir, exist_ok=True)
    os.makedirs(test_subdir, exist_ok=True)

    # Iterate through annotations in the annotation_directory
    moved_files = []
    for filename in os.listdir(annotation_directory):
        if filename.split('.')[0] in listed_train_images:  # We check for the filename without extension
            source_filepath = os.path.join(annotation_directory, filename)
            target_filepath = os.path.join(train_subdir, filename)
            shutil.move(source_filepath, target_filepath)
            moved_files.append(target_filepath)
        elif filename.split('.')[0] in listed_test_images:
            source_filepath = os.path.join(annotation_directory, filename)
            target_filepath = os.path.join(test_subdir, filename)
            shutil.move(source_filepath, target_filepath)
            moved_files.append(target_filepath)

    return moved_files

# Paths
train_txt_path = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/imageSets/train.txt"
test_txt_path = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/imageSets/test.txt"
annotations_directory = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/annotations-txt-anno"

# Execute the function
moved_files = move_annotations_based_on_txt([train_txt_path, test_txt_path], annotations_directory)