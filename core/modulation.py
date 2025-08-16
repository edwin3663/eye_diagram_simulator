# Filename: prbs_generator.py
# Project: eye_diagram_simulator
# Author: Peter Saffold
# License: MIT (see LICENSE file for details)
# Description: Generates NRZ or PAM4 modulation for a bitstream
from collections.abc import Iterable

import numpy as np


class NRZModulator:
    """Simulates an NRZ signal"""

    def __init__(self, samples: int = 32, v_high: int = 1, v_low: int = -1):
        self.samples = samples
        self.v_high = v_high
        self.v_low = v_low


    def encode(self, bits: Iterable[int]) -> np.ndarray:
        # 0 -> v_low, 1 -> v_high
        return np.where(bits == 1, self.v_high, self.v_low)