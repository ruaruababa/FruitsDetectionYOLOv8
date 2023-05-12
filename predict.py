from ultralytics import YOLO

src_ = r"C:\Users\admin\Pictures\fruits\tao.jepg"


model = YOLO(
    r"C:\Users\admin\FruitsDetectionYOLOv8\models\single_train\apple\weights\best.pt"
)

model.overrides = {
    "project": r"C:\Users\admin\FruitsDetectionYOLOv8\results",
    "exist_ok": True,
}


def detectFruits(fileName):
    results = model.predict(
        source=f"{fileName}",
        save=True,
        conf=0.4,
        show=True,
    )

    for r in results:
        print("r.boxes.cls", r.boxes.cls)
        print("r.boxes.conf", r.boxes)
        print("r.boxes.xyxy", r.boxes.data)
        for c in r.boxes.cls:
            if c:
                print("class", c)
                print("Class", int(c))
                print("Class", model.names[int(c)])
            else:
                print("no class")
