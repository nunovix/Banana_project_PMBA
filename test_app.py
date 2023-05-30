import cv2
from ultralytics import YOLO

def main_loop(frame):
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #model_output = model(frame)[0]
    cv2.imshow("Frame Window", frame)

model = YOLO("yolov8n.pt")



capture = cv2.VideoCapture(0)
while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    main_loop(frame)
    # enable keyboard shortcut to stop capturing - press "q" to stop
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
