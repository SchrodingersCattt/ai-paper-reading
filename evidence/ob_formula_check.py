"""Compare Table 1's -55.45 with the expression printed in footnote k.

Page 10 prints the elemental-analysis formula C4H6N6O4 (202.0451).
The atom counts below are those printed counts. Atomic masses used for the
integer check are stated in this file.
"""

NAME = "2,4,6-triamino-5-nitropyrimidine-1,3-dioxide"
# Methods page prints: calcd (%) for C4H6N6O4 (202.0451).
ATOMS = (4, 6, 6, 4)  # C, H, N, O
PRINTED_MW = 202.0451
TABLE = -55.45


def mw(masses):
    c, h, n, o = ATOMS
    mc, mh, mn, mo = masses
    return c * mc + h * mh + n * mn + o * mo


def ob(masses, coefficient_on_a):
    c, h, _n, o = ATOMS
    return 1600 * (o - coefficient_on_a * c - h / 2) / mw(masses)


def main():
    c, h, _n, o = ATOMS
    printed = 1600 * (o - c - h / 2) / PRINTED_MW
    with_2a = 1600 * (o - 2 * c - h / 2) / PRINTED_MW
    print(NAME)
    print("atoms C H N O", ATOMS)
    print(
        f"printed_Mw={PRINTED_MW} "
        f"printed_(d-a-b/2)={printed:.4f} "
        f"with_(d-2a-b/2)={with_2a:.4f} "
        f"table={TABLE}"
    )
    sets = {
        "C12 H1 N14 O16": (12, 1, 14, 16),
        "C12.011 H1.008 N14.007 O15.999": (12.011, 1.008, 14.007, 15.999),
    }
    for label, masses in sets.items():
        print(
            f"{label} Mw={mw(masses):.4f} "
            f"printed_(d-a-b/2)={ob(masses, 1):.4f} "
            f"with_(d-2a-b/2)={ob(masses, 2):.4f}"
        )


if __name__ == "__main__":
    main()
