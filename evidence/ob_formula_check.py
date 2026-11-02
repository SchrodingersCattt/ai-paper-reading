"""Compare Table 1's -55.45 with the expression printed in footnote k.

The chemical name is on PDF page 1. The atom count below is derived from that
name, not printed as a formula in the PDF. Atomic masses are stated here.
"""

NAME = "2,4,6-triamino-5-nitropyrimidine-1,3-dioxide"
# pyrimidine-1,3-dioxide C4H4N2O2; three amino groups replace three H
# (+3N +3H); the nitro group replaces the remaining ring H (-1H +1N +2O).
ATOMS = (4, 6, 6, 4)  # C, H, N, O
TABLE = -55.45


def mw(masses):
    c, h, n, o = ATOMS
    mc, mh, mn, mo = masses
    return c * mc + h * mh + n * mn + o * mo


def ob(masses, coefficient_on_a):
    c, h, _n, o = ATOMS
    return 1600 * (o - coefficient_on_a * c - h / 2) / mw(masses)


def main():
    sets = {
        "C12 H1 N14 O16": (12, 1, 14, 16),
        "C12.011 H1.008 N14.007 O15.999": (12.011, 1.008, 14.007, 15.999),
    }
    print(NAME)
    print("atoms C H N O", ATOMS)
    for label, masses in sets.items():
        printed = ob(masses, 1)
        with_2a = ob(masses, 2)
        print(
            f"{label} Mw={mw(masses):.4f} "
            f"printed_(d-a-b/2)={printed:.4f} "
            f"with_(d-2a-b/2)={with_2a:.4f} "
            f"table={TABLE}"
        )


if __name__ == "__main__":
    main()
