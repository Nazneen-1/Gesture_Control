import mediapipe as mp
import cv2

class HandDetector:

    def __init__(self, detection_conf, tracking_conf, max_hands):
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.init_model(detection_conf, tracking_conf, max_hands)

    def init_model(self, detection_conf, tracking_conf, max_hands):
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=detection_conf,
            min_tracking_confidence=tracking_conf,
            max_num_hands=int(max_hands)
        )

    def detect(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.hands.process(rgb)

    def draw(self, frame, hand_landmarks):
        self.mp_draw.draw_landmarks(
            frame,
            hand_landmarks,
            self.mp_hands.HAND_CONNECTIONS
        )