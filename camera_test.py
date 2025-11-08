import cv2

print("🔍 Checking camera...")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected. Trying another index...")
    cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Still not opening. Check permissions or other apps.")
else:
    print("Camera opened successfully. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print(" Frame not captured!")
            break
        cv2.imshow("Live Camera Test", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
