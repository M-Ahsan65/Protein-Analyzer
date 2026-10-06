# Protein Sequence Analyzer
# Bioinformatics Mini Project

AMINO_ACID_WEIGHTS = {
    "A": 89.09,
    "R": 174.20,
    "N": 132.12,
    "D": 133.10,
    "C": 121.15,
    "E": 147.13,
    "Q": 146.15,
    "G": 75.07,
    "H": 155.16,
    "I": 131.17,
    "L": 131.17,
    "K": 146.19,
    "M": 149.21,
    "F": 165.19,
    "P": 115.13,
    "S": 105.09,
    "T": 119.12,
    "W": 204.23,
    "Y": 181.19,
    "V": 117.15
}

HYDROPHOBIC = "AILMFWV"
CHARGED = "DEKR"

VALID_AMINO_ACIDS = set(AMINO_ACID_WEIGHTS.keys())


def validate_sequence(sequence):
    return all(aa in VALID_AMINO_ACIDS for aa in sequence)


def amino_acid_count(sequence):
    counts = {}

    for aa in sequence:
        counts[aa] = counts.get(aa, 0) + 1

    return counts


def molecular_weight(sequence):
    weight = 0

    for aa in sequence:
        weight += AMINO_ACID_WEIGHTS[aa]

    return weight


def percentage(sequence, group):
    count = sum(aa in group for aa in sequence)
    return (count / len(sequence)) * 100


# -----------------------------
# Main Program
# -----------------------------

protein = input("Enter protein sequence: ").upper().replace(" ", "")

if not protein:
    print("❌ Please enter a protein sequence.")

elif not validate_sequence(protein):
    print("❌ Invalid protein sequence!")
    print("Use standard one-letter amino acid codes.")

else:
    counts = amino_acid_count(protein)

    print("\n========== PROTEIN ANALYSIS ==========")

    print("Protein Sequence:", protein)

    print("Protein Length:", len(protein))

    print(f"\nApprox. Molecular Weight: "
          f"{molecular_weight(protein):.2f} Da")

    print(f"Hydrophobic Amino Acids: "
          f"{percentage(protein, HYDROPHOBIC):.2f}%")

    print(f"Charged Amino Acids: "
          f"{percentage(protein, CHARGED):.2f}%")

    print("\nAmino Acid Frequency:")

    for aa, count in sorted(counts.items()):
        print(f"{aa}: {count}")

    most_common = max(counts, key=counts.get)

    print("\nMost Common Amino Acid:")
    print(f"{most_common} ({counts[most_common]} times)")

    print("\n======================================")