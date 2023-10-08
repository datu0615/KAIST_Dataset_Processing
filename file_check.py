import os

txt_train = len(os.listdir('/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/annotations-txt-anno/train'))
txt_test = len(os.listdir('/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/annotations-txt-anno/test'))
infrared_train = len(os.listdir('/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/img_split/infrared/train'))
infrared_test = len(os.listdir('/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/img_split/infrared/test'))
visible_train = len(os.listdir('/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/img_split/visible/train'))
visible_test = len(os.listdir('/home/jb/Desktop/cv/multispectral-object-detection/datasets/rgbt-ped-detection/datasets/kaist-cvpr15/img_split/visible/test'))

print(f'txt train file count : {txt_train}')
print(f'txt test file count : {txt_test}')
print(f'infrared train file count : {infrared_train}')
print(f'infrared test file count : {infrared_test}')
print(f'visible train file count : {visible_train}')
print(f'visible test file count : {visible_test}')