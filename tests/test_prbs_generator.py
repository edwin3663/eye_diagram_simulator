# Filename: test_prbs_generaator.py
# Project: eye_diagram_simulator
# Author: Peter Saffold
# License: MIT (see LICENSE file for details)
# Description: Tests the PRBSGenerator class
from core.prbs_generator import PRBSGenerator, PRBSOrder


def test_prbs_initialization():
    # seed can be none defaults to all ones
    PRBSGenerator(PRBSOrder.PRBS7, None)

    # TypeError when seed is not integer
    PRBSGenerator(PRBSOrder.PRBS7, )

    # ValueError when seed is zero

    # ValueError when seed exceeds PRBS length


    pass


def test_prbs_bit_stream(order: PRBSOrder = PRBSOrder.PRBS7, seed: int = None):
    generator = PRBSGenerator(order = PRBSOrder.PRBS7)
    sequence = generator.generate_bits(2**7 - 1)

    counts: [int] = [2**7 -1, 200]
    for num in counts:
        sequence = generator.generate_bits(num)
        print(f"A {num} bit length RBS7 sequence.")
        print(f"sequence: {sequence}")

test_prbs_bit_stream()