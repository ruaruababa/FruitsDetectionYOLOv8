from ultralytics import YOLO

src_ = r"C:\Users\admin\Pictures\fruits\tao.jepg"


def detectFruits():
    model = YOLO(
        r"C:\Users\admin\FruitsDetectionYOLOv8\models\single_train\apple\weights\best.pt"
    )

    model.overrides = {
        "project": r"C:\Users\admin\FruitsDetectionYOLOv8\results",
        "exist_ok": True,
    }

    model.predict(
        source=r"C:\Users\admin\Pictures\fruits\tao.jpg",
        save=True,
        conf=0.4,
    )
