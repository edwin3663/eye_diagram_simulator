# Filename: prbs_generator.py
# Project: eye_diagram_simulator
# Author: Peter Saffold
# License: MIT (see LICENSE file for details)
# Description: Generates PRBS7/9/11/15/23/31 bitstreams using LFSRs for use in waveform simulation

from enum import Enum

class PRBSOrder(Enum):
    """
    Enumeration of supported PRBS orders.

    This enum is used to define the order of the PRBS (Pseudorandom Binary Sequence) generator.
    Each member corresponds to a standard PRBS polynomial order that determines the length of the
    linear feedback shift register (LFSR) used in sequence generation.

    Attributes:
        PRBS7:  PRBS of order 7 (x^7 + x^6 + 1)
        PRBS9:  PRBS of order 9 (x^9 + x^5 + 1)
        PRBS11: PRBS of order 11 (x^11 + x^9 + 1)
        PRBS15: PRBS of order 15 (x^15 + x^14 + 1)
        PRBS23: PRBS of order 23 (x^23 + x^18 + 1)
        PRBS31: PRBS of order 31 (x^31 + x^28 + 1)
    """
    PRBS7 = 7
    PRBS9 = 9
    PRBS11 = 11
    PRBS15 = 15
    PRBS23 = 23
    PRBS31 = 31

class PRBSGenerator:
    """Generates PRBS sequences for PRBS7, PRBS9, PRBS11, PRBS15, PRBS23, PRBS31."""

    # Predefined tap positions for PRBS polynomials
    _prbs_taps = {
        PRBSOrder.PRBS7: (7,6),
        PRBSOrder.PRBS9: (9,5),
        PRBSOrder.PRBS11: (11, 9),
        PRBSOrder.PRBS15: (15, 14),
        PRBSOrder.PRBS23: (23, 18),
        PRBSOrder.PRBS31: (31, 28),
    }

    def __init__(self, order: PRBSOrder = PRBSOrder.PRBS7, seed: int = None):
        self.order = order
        self.taps = self._prbs_taps[order]
        max_state = (1 << order.value) - 1

        if seed is None:
            self.state = max_state # default: all ones
        else:
            if not isinstance(seed, int):
                raise TypeError("Seed must be an integer.")
            if seed <= 0:
                raise ValueError("Seed must be a positive non-zero integer.")
            if seed > max_state:
                raise ValueError(f"Seed must not be less than 2^{order.value} ({max_state}).")
            self.state = seed

    def next_bit(self) -> int:
        """Generate the next PRBS bit."""
        tap1 = (self.state >> (self.taps[0] - 1)) & 1
        tap2 = (self.state >> (self.taps[1] - 1)) & 1
        new_bit = tap1 ^ tap2
        self.state = ((self.state << 1) | new_bit) & ((1 << self.order.value) - 1)
        return new_bit

    def generate_bits(self, count) -> [int]:
        """Generate a list of PRBS bits."""
        return [self.next_bit() for _ in range(count)]


