from Bio.Seq import Seq
from Bio import SeqIO



# Check if the sequence is valid
def check_valid_sequence(sequence):
    valid_chars = set("ATGC")
    return all(char in valid_chars for char in sequence)


def check_dna_sequence(sequence):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    # Check for the validity of the INPUT sequence
    if not check_valid_sequence(sequence):
        print("The sequence contains invalid characters. Use only the letters A, T, G and C.")
        return False

    # Find the start codon in the sequence
    start_index = sequence.find(start_codon)
    if start_index == -1:
        # If start codon not found, try in reverse complement
        reversed_sequence = Seq(sequence).reverse_complement()
        start_index = reversed_sequence.find(start_codon)

        if start_index == -1:
            print("Start codon not found")
            return False
        else:
            # If start codon found in reverse complement, update the sequence to reversed_sequence
            sequence = reversed_sequence
            print("The start codon found in reversed sequence")

    # Found start codon
    print("Start codon found.")

    # Check if start codon is followed by stop codon
    if check_stop_codon_after_start(sequence, start_index, stop_codons):
        print("Stop codon found.")
        return True

    print("Stop codon not found.")
    return False


def check_stop_codon_after_start(sequence, start_index, stop_codons):
    current_position = start_index + len("ATG")
    while current_position < len(sequence):
        codon = sequence[current_position:current_position + 3]

        if codon in stop_codons:
            return True

        current_position += 3

    return False


def main():
    # Receiving input from the user
    sequence = input("Enter the nucleotide sequence: ").upper()

    # Print of result
    if check_dna_sequence(sequence):
        print("The sequence contains a prokaryotic coding sequence.")
    else:
        print("The sequence DOES NOT contain a prokaryotic coding sequence.")


if __name__ == "__main__":
    main()
