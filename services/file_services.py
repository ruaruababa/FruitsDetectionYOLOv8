import os.path
import shutil

# path = r"C:\Users\yang\OneDrive - Thuyloi University\Images\apple\test\labels"


def moveFile(currentPath, newPath):
    for i in range(622, 1000):
        if os.path.isfile(r"currentPath\apple_" + str(i) + ".txt"):
            shutil.move(
                r"currentPath\apple_" + str(i) + ".txt",
                r"newPath",
            )
            print(f"Moving apple_{i}.txt")


def rewrite_class(path_, new_class):
    for i in range(0, 1000):
        hasFile = os.path.isfile(f"{path_}" + str(i) + ".txt")
        if hasFile:
            file_ = open(
                f"{path_}" + str(i) + ".txt",
                "r",
            )
            labels_ = file_.read().splitlines()
            for label in labels_:
                lb = label.split(" ")
                lb = [float(val) if val != f"{lb[0]}" else new_class for val in lb]
                my_list = [str(lb[i]) for i in range(len(lb))]
                my_list = " ".join(my_list)
                rf = open(
                    f"{path_}" + str(i) + ".txt",
                    "a",
                )
                rf.truncate(0)
                wf = open(
                    f"{path_}" + str(i) + ".txt",
                    "a",
                )
                wf.write(my_list + "\n")


def remove_img_no_labels(path_):
    for i in range(0, 1000):
        hasImg = os.path.isfile(r"path_\apple_" + str(i) + ".jpg")
        hasLabel = os.path.isfile(r"path_\apple_" + str(i) + ".txt")
        if hasImg and hasLabel:
            print("TRUE")
        elif hasImg and not hasLabel:
            os.remove(r"path_\apple_" + str(i) + ".jpg")
            print(f"Removing apple_{i}.jpg")
        elif not hasImg and hasLabel:
            os.remove(r"path_\apple_" + str(i) + ".txt")
            print(f"Removing apple_{i}.txt")


def main():
    path_ = (
        r"C:\Users\admin\OneDrive - Thuyloi University\Images\watermelon\watermelon_"
    )
    rewrite_class(path_, 3)


if __name__ == "__main__":
    main()
