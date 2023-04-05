import os
import os.path

path = r"C:\Users\admin\OneDrive - Thuyloi University\Images\dragon fruit"

lst = os.listdir(path)  # your directory path
number_files = len(lst)
os.path.isfile(path)
print(os.path.isfile(path))
for i in range(number_files):
    path_img = r"C:\Users\admin\OneDrive - Thuyloi University\Images\dragon fruit"
    path_label = (
        r"C:\Users\admin\OneDrive - Thuyloi University\Images\dragon fruit\train\labels"
    )
    hasImage = os.path.isfile(path_img + f"\dragon fruit_{i}.jpg")
    hasLabel = os.path.isfile(path_label + f"\dragon fruit_{i}.txt")
    if hasImage and hasLabel:
        print("Image and label exist")
    elif hasImage and not hasLabel:
        os.remove(path_img + f"\dragon fruit_{i}.jpg")
        print("Image exist but label not exist")
    elif not hasImage and hasLabel:
        os.remove(path_label + f"\dragon fruit_{i}.txt")
        print("Image not exist but label exist")
