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
    model.predict(
        source=f"{fileName}",
        save=True,
        conf=0.4,
    )
