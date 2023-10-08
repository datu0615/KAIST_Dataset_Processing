import os

def remove_images_without_annotations(img_directory, annotation_directory):
    """Remove images in the img_directory that do not have corresponding annotations in the annotation_directory."""
    
    # Get a list of all annotation filenames without extensions
    annotation_files = [filename.split('.')[0] for filename in os.listdir(annotation_directory) if filename.endswith('.txt')]
    
    # Iterate through images in the img_directory
    removed_files = []
    for filename in os.listdir(img_directory):
        if filename.split('.')[0] not in annotation_files:  # We check for the filename without extension
            filepath_to_remove = os.path.join(img_directory, filename)
            os.remove(filepath_to_remove)
            removed_files.append(filepath_to_remove)

    return removed_files

# Paths
img_directory = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/img_split/visible/train"
annotations_directory = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/annotations-txt-anno/train"

# Execute the function
removed_files = remove_images_without_annotations(img_directory, annotations_directory)


# Paths
img_directory = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/img_split/visible/test"
annotations_directory = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/annotations-txt-anno/test"

# Execute the function
removed_files = remove_images_without_annotations(img_directory, annotations_directory)


# Paths
img_directory = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/img_split/infrared/train"
annotations_directory = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/annotations-txt-anno/train"

# Execute the function
removed_files = remove_images_without_annotations(img_directory, annotations_directory)


# Paths
img_directory = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/img_split/infrared/test"
annotations_directory = "/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/annotations-txt-anno/test"

# Execute the function
removed_files = remove_images_without_annotations(img_directory, annotations_directory)
