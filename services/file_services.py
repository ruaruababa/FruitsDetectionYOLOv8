import os.path
import shutil

path = r"C:\Users\yang\OneDrive - Thuyloi University\Images\apple\test\labels"
# os.path.isfile(
#     r"C:\\Users\\yang\\OneDrive - Thuyloi University\\Images\\apple\apple_3.jpg"
# )
# print(
#     os.path.isfile(
#         r"C:\\Users\\yang\\OneDrive - Thuyloi University\\Images\\apple\apple_3.jpg"
#     )
# )

# for i in range(622, 1000):
#     if os.path.isfile(
#         r"C:\\Users\\yang\\OneDrive - Thuyloi University\\Images\\apple\\valid\\images\apple_"
#         + str(i)
#         + ".txt"
#     ):
#         shutil.move(
#             r"C:\\Users\\yang\\OneDrive - Thuyloi University\\Images\\apple\\valid\\images\apple_"
#             + str(i)
#             + ".txt",
#             r"C:\\Users\\yang\\OneDrive - Thuyloi University\\Images\\apple\\valid\\labels",
#         )
#         print(f"Moving apple_{i}.txt")
lst = os.listdir(path)  # your directory path
number_files = len(lst)
for i in range(0, 1000):
    hasFile = os.path.isfile(
        r"C:\\Users\\yang\\OneDrive - Thuyloi University\\Images\\apple\\test\\labels\apple_"
        + str(i)
        + ".txt"
    )
    if hasFile:
        file_ = open(
            r"C:\\Users\\yang\\OneDrive - Thuyloi University\\Images\\apple\\test\\labels\apple_"
            + str(i)
            + ".txt",
            "r",
        )

        labels_ = file_.read().splitlines()
        # labels_i = labels_[i].split(" ")
        for lebel in labels_:
            lb = lebel.split(" ")
            lb = [float(val) if val != "15" else 0 for val in lb]
            my_list = [str(lb[i]) for i in range(len(lb))]
            my_list = " ".join(my_list)
            print(my_list)
            rf = open(
                r"C:\\Users\\yang\\OneDrive - Thuyloi University\\Images\\apple\\test\\labels\apple_"
                + str(i)
                + ".txt",
                "a",
            )
            rf.truncate(0)
            wf = open(
                r"C:\\Users\\yang\\OneDrive - Thuyloi University\\Images\\apple\\test\\labels\apple_"
                + str(i)
                + ".txt",
                "a",
            )
            wf.write(my_list + "\n")
        # print(labels_i)

# for i in range(1, 1000):
#     if os.path.isfile(
#         r"C:\\Users\\yang\\OneDrive - Thuyloi University\\Images\\apple\\test\\images\apple_"
#         + str(i)
#         + ".jpg"
#     ) and os.path.isfile(
#         r"C:\\Users\\yang\\OneDrive - Thuyloi University\\Images\\apple\\test\\labels\apple_"
#         + str(i)
#         + ".txt"
#     ):
#         print("1")
#     else:
#         if os.path.isfile(
#             r"C:\\Users\\yang\\OneDrive - Thuyloi University\\Images\\apple\\test\\images\apple_"
#             + str(i)
#             + ".jpg"
#         ):
#             os.remove(
#                 r"C:\\Users\\yang\\OneDrive - Thuyloi University\\Images\\apple\\test\\images\apple_"
#                 + str(i)
#                 + ".jpg"
#             )
#             if os.path.isfile(
#                 r"C:\\Users\\yang\\OneDrive - Thuyloi University\\Images\\apple\\test\\labels\apple_"
#                 + str(i)
#                 + ".txt"
#             ):
#                 os.remove(
#                     r"C:\\Users\\yang\\OneDrive - Thuyloi University\\Images\\apple\\test\\labels\apple_"
#                     + str(i)
#                     + ".txt"
#                 )

#             print(f"Removing apple_{i}.jpg and apple_{i}.txt")
