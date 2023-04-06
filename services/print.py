import logging

# logging.basicConfig(
#     filename="start_folder.bat", level=logging.INFO, format="%(message)s"
# )
start_folder = logging.getLogger("start_folder.bat")
start_folder.setLevel(logging.INFO)
start_folder.addHandler(logging.FileHandler("start_folder.bat", "w"))
close_folder = logging.getLogger("close_folder.bat")
close_folder.setLevel(logging.INFO)
close_folder.addHandler(logging.FileHandler("close_folder.bat", "w"))
fruits = [
    "apple",
    "orange",
    "kiwi",
    "strawberry",
    "blueberry",
    "mango",
    "pineapple",
    "watermelon",
    "grape",
    "pear",
    "peach",
    "mango",
    "cherry",
    "lemon",
    "lime",
    "grapefruit",
    "avocado",
    "melon",
]
fruits = fruits.sort()
path = r"C:\Users\admin\Desktop\Images"
logging.info(f"@echo off")
for i in range(len(fruits)):
    start_folder.info(f"start {path}\{fruits[i]}")
    command = f'TASKKILL /F /FI "WINDOWTITLE eq {path}\{fruits[i]}" /IM explorer.exe'
    close_folder.info(command)
