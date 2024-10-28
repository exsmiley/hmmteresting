from ultralytics import YOLO
import cv2


def predict(chosen_model, img, conf=0.5):
    classes = ["people"]
    classes = []
    # if len(classes) == 0:
    results = chosen_model.predict(img, conf=conf)
    # else:
    # results = chosen_model.predict(img, conf=conf, classes=classes)
    return results

def predict_and_detect(model, img):
    results = predict(model, img, conf=0.2)

    for result in results:
        for box in result.boxes:
            cv2.rectangle(img, (int(box.xyxy[0][0]), int(box.xyxy[0][1])), (int(box.xyxy[0][2]), int(box.xyxy[0][3])), (255, 0, 0), 2)

            cv2.putText(img, f"{result.names[int(box.cls[0])]}", (int(box.xyxy[0][0]), int(box.xyxy[0][1])-10), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)

if __name__ == "__main__":
    yolo_model = YOLO("yolo11n.pt")
    img_filename = "lobbywithppl.jpg"
    img = cv2.imread(img_filename)
    predict_and_detect(yolo_model, img)
    cv2.imshow("image", img)
    cv2.imwrite(img_filename.replace(".jpg", "2.jpg"), img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()