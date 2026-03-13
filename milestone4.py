import time


class PerformanceMetrics:

    def __init__(self):
        self.accuracy = 100
        self.response_time = 0
        self.prev_time = time.time()

    def update(self):
        """
        Calculate response time between frames
        """
        current = time.time()
        self.response_time = int((current - self.prev_time) * 1000)
        self.prev_time = current

        return self.response_time

    def evaluate_gesture_quality(self, distance):

        if distance > 120:
            return "Good"
        elif distance > 60:
            return "Moderate"
        else:
            return "Poor"