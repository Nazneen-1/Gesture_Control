import math

class GestureRecognizer:

    def calculate_distance(self, hand_landmarks, frame_shape):
        h, w, _ = frame_shape

        thumb = hand_landmarks.landmark[4]
        index = hand_landmarks.landmark[8]

        x1, y1 = int(thumb.x * w), int(thumb.y * h)
        x2, y2 = int(index.x * w), int(index.y * h)

        distance = math.hypot(x2 - x1, y2 - y1)

        if distance < 40:
            gesture = "Closed"
        elif distance < 100:
            gesture = "Pinch"
        else:
            gesture = "Open"

        return distance, gesture, (x1, y1, x2, y2)