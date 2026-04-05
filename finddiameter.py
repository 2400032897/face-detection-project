import cv2
import numpy as np

# ---------- CALIBRATION SETTINGS ----------
KNOWN_DIAMETER_CM = 2.5  # real diameter of reference object (cm)

# Reference object pixel diameter at 15 cm distance
PIXEL_AT_REFERENCE = 120  

# Distance range in pixels (15-25 cm)
PIXEL_MAX = 120  # closest (15 cm)
PIXEL_MIN = 70   # farthest (25 cm)

# Minimum & maximum radius to ignore noise
MIN_RADIUS = 20
MAX_RADIUS = 200

# ---------- CAMERA SETUP ----------
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (9, 9), 2)

    # Detect circles
    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=100,
        param1=50,
        param2=30,
        minRadius=MIN_RADIUS,
        maxRadius=MAX_RADIUS
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))

        # Filter circles within radius range (ignore noise)
        valid_circles = [c for c in circles[0, :] if MIN_RADIUS <= c[2] <= MAX_RADIUS]

        if valid_circles:
            # Pick largest valid circle
            x, y, r = max(valid_circles, key=lambda c: c[2])
            diameter_pixel = 2 * r

            # Distance check
            if PIXEL_MIN <= diameter_pixel <= PIXEL_MAX:
                diameter_cm = (diameter_pixel / PIXEL_AT_REFERENCE) * KNOWN_DIAMETER_CM
                text = f"Diameter: {diameter_cm:.2f} cm"
                color = (0, 255, 0)  # Green
            elif diameter_pixel < PIXEL_MIN:
                text = "Move closer!"
                color = (0, 0, 255)  # Red
            else:
                text = "Move farther!"
                color = (0, 0, 255)  # Red

            # Draw circle & label
            cv2.circle(frame, (x, y), r, color, 2)
            cv2.putText(frame, text, (x - 60, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Display live frame
    cv2.imshow("Single Circle Diameter Detector", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()