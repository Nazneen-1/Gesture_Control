import cv2
import mediapipe as mp
import math
import time
import tkinter as tk
from PIL import Image, ImageTk

# ==========================
# MediaPipe Wrapper
# ==========================
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

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.hands.process(rgb)

# ==========================
# Main App
# ==========================
class GestureApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Gesture Recognition Interface")
        self.root.state("zoomed")  # FULL SCREEN
        self.root.configure(bg="#121212")

        self.cap = cv2.VideoCapture(0)
        self.camera_running = False
        self.pTime = 0

        # Default parameters
        self.detection_conf = 0.7
        self.tracking_conf = 0.7
        self.max_hands = 1

        self.detector = HandDetector(
            self.detection_conf,
            self.tracking_conf,
            self.max_hands
        )

        self.build_ui()

    # ==========================
    # UI
    # ==========================
    def build_ui(self):

        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        # LEFT - CAMERA
        self.video_label = tk.Label(self.root, bg="black")
        self.video_label.grid(row=0, column=0, sticky="nsew")

        # RIGHT PANEL
        self.panel = tk.Frame(self.root, bg="#1e1e1e")
        self.panel.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.panel.columnconfigure(0, weight=1)

        # Detection Section
        self.create_section("Detection Status")
        self.status_label = self.create_label("Inactive", "#ff4444")
        self.hands_label = self.create_label("Hands Detected: 0")
        self.fps_label = self.create_label("FPS: 0")

        # Model Info
        self.model_label = self.create_label(f"Model Status: Loaded")
        self.landmarks_label = self.create_label("Landmarks: 21")
        self.connections_label = self.create_label(
            f"Connections: {len(self.detector.mp_hands.HAND_CONNECTIONS)}"
        )

        # Sliders Section
        self.create_section("Detection Parameters")

        self.create_slider("Detection Confidence", 0, 1,
                           self.detection_conf,
                           self.update_detection_conf)

        self.create_slider("Tracking Confidence", 0, 1,
                           self.tracking_conf,
                           self.update_tracking_conf)

        self.create_slider("Max Hands", 1, 4,
                           self.max_hands,
                           self.update_max_hands,
                           is_int=True)

        # Distance Section
        self.create_section("Distance Measurement")
        self.distance_label = self.create_label("0 px", "#00ffcc", 22)

        # Gesture Section
        self.create_section("Gesture States")
        self.open_label = self.create_label("Open (>100 px)")
        self.pinch_label = self.create_label("Pinch (40-100 px)")
        self.closed_label = self.create_label("Closed (<40 px)")

        # Buttons
        btn_frame = tk.Frame(self.panel, bg="#1e1e1e")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="Start Camera",
                  bg="#00bfff", width=15,
                  command=self.start_camera).grid(row=0, column=0, padx=5)

        tk.Button(btn_frame, text="Stop Camera",
                  bg="#ff4444", width=15,
                  command=self.stop_camera).grid(row=0, column=1, padx=5)

        tk.Button(btn_frame, text="Capture",
                  bg="#00ffcc", width=15,
                  command=self.capture_image).grid(row=0, column=2, padx=5)

    # ==========================
    # UI Helpers
    # ==========================
    def create_section(self, title):
        tk.Label(self.panel, text=title,
                 bg="#1e1e1e", fg="#00bfff",
                 font=("Segoe UI", 12, "bold")
                 ).pack(anchor="w", pady=(15, 5))

    def create_label(self, text, color="white", size=11):
        label = tk.Label(self.panel,
                         text=text,
                         bg="#1e1e1e",
                         fg=color,
                         font=("Segoe UI", size))
        label.pack(anchor="w")
        return label

    def create_slider(self, text, min_val, max_val,
                      default, command, is_int=False):

        tk.Label(self.panel, text=text,
                 bg="#1e1e1e", fg="white").pack(anchor="w")

        slider = tk.Scale(self.panel,
                          from_=min_val,
                          to=max_val,
                          resolution=0.1 if not is_int else 1,
                          orient="horizontal",
                          bg="#1e1e1e",
                          fg="white",
                          troughcolor="#333333",
                          highlightthickness=0,
                          command=command)
        slider.set(default)
        slider.pack(fill="x")

    # ==========================
    # Slider Updates
    # ==========================
    def update_detection_conf(self, val):
        self.detection_conf = float(val)
        self.reinitialize_model()

    def update_tracking_conf(self, val):
        self.tracking_conf = float(val)
        self.reinitialize_model()

    def update_max_hands(self, val):
        self.max_hands = int(float(val))
        self.reinitialize_model()

    def reinitialize_model(self):
        # Properly close old model
        self.detector.hands.close()

        # Reinitialize with new parameters
        self.detector.init_model(
            self.detection_conf,
            self.tracking_conf,
            self.max_hands
        )

        self.model_label.config(text="Model Status: Reloaded")

    # ==========================
    # Camera
    # ==========================
    def start_camera(self):
        self.camera_running = True
        self.update_frame()

    def stop_camera(self):
        self.camera_running = False
        self.status_label.config(text="Inactive", fg="#ff4444")

    def capture_image(self):
        if hasattr(self, "current_frame"):
            cv2.imwrite("captured_frame.jpg", self.current_frame)

    def update_frame(self):
        if not self.camera_running:
            return

        success, frame = self.cap.read()
        if not success:
            return

        frame = cv2.flip(frame, 1)

        results = self.detector.process(frame)

        distance = 0
        gesture = None
        hands_detected = 0

        if results.multi_hand_landmarks:
            hands_detected = len(results.multi_hand_landmarks)
            self.status_label.config(text="Active", fg="#00ff00")

            for handLms in results.multi_hand_landmarks:
                self.detector.mp_draw.draw_landmarks(
                    frame, handLms,
                    self.detector.mp_hands.HAND_CONNECTIONS
                )

                h, w, _ = frame.shape
                thumb = handLms.landmark[4]
                index = handLms.landmark[8]

                x1, y1 = int(thumb.x * w), int(thumb.y * h)
                x2, y2 = int(index.x * w), int(index.y * h)

                distance = math.hypot(x2 - x1, y2 - y1)

                if distance < 40:
                    gesture = "Closed"
                elif distance < 100:
                    gesture = "Pinch"
                else:
                    gesture = "Open"

                cv2.circle(frame, (x1, y1), 10, (255, 0, 0), -1)
                cv2.circle(frame, (x2, y2), 10, (255, 0, 0), -1)
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        # FPS
        cTime = time.time()
        fps = 1 / (cTime - self.pTime) if (cTime - self.pTime) != 0 else 0
        self.pTime = cTime

        self.hands_label.config(text=f"Hands Detected: {hands_detected}")
        self.fps_label.config(text=f"FPS: {int(fps)}")
        self.distance_label.config(text=f"{int(distance)} px")

        # Reset gesture colors
        for label in [self.open_label, self.pinch_label, self.closed_label]:
            label.config(fg="gray")

        if gesture == "Open":
            self.open_label.config(fg="#00ff00")
        elif gesture == "Pinch":
            self.pinch_label.config(fg="#00ff00")
        elif gesture == "Closed":
            self.closed_label.config(fg="#00ff00")

        self.current_frame = frame
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        imgtk = ImageTk.PhotoImage(image=img)
        self.video_label.imgtk = imgtk
        self.video_label.configure(image=imgtk)

        self.root.after(10, self.update_frame)


root = tk.Tk()
app = GestureApp(root)
root.mainloop()