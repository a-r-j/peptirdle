import argparse
import itertools
import random
from typing import List

AMINO_ACIDS: List[str] = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"]


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", default=5, type=int, required=False, help="Length of peptide")
    return parser.parse_args()

def main():
    args = parse_arguments()
    words = list(itertools.product(AMINO_ACIDS, repeat=args.length-1))
    words = ["m"+"".join(w).lower() for w in words]
    print(words)
    print(len(words))

    textfile = open("validGuesses.ts", "w")
    #words = random.sample(words, 10000)
    textfile.write("export const VALIDGUESSES = [" + "\n")
    for w in words:
        textfile.write("'" + w + "',\n")
    textfile.write(
        "];" + "\n")
    textfile.close()

    textfile = open("wordlist.ts", "w")
    words = random.sample(words, 2000)
    textfile.write("export const WORDS = [" + "\n")
    for w in words:
        textfile.write("'" + w + "',\n")
    textfile.write("];" + "\n")
    textfile.close()
    
if __name__ == "__main__":
    main()
