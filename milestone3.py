import numpy as np
from pycaw.pycaw import AudioUtilities

class VolumeController:

    def __init__(self, min_dist=20, max_dist=200):
        self.min_dist = min_dist
        self.max_dist = max_dist
        self.history = []

        self.device = AudioUtilities.GetSpeakers()
        self.endpoint = self.device.EndpointVolume

        self.min_vol, self.max_vol = self.endpoint.GetVolumeRange()[:2]

    def map_distance_to_volume(self, distance):
        distance = np.clip(distance, self.min_dist, self.max_dist)
        normalized = (distance - self.min_dist) / (self.max_dist - self.min_dist)
        return normalized

    def set_volume(self, normalized_value):
        normalized_value = np.clip(normalized_value, 0, 1)

        target_volume = (
            normalized_value * (self.max_vol - self.min_vol)
            + self.min_vol
        )

        self.endpoint.SetMasterVolumeLevel(target_volume, None)

        volume_percent = int(normalized_value * 100)

        # Store last 20 values
        self.history.append(volume_percent)
        if len(self.history) > 20:
            self.history.pop(0)

        return volume_percent