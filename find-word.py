import pathlib as pl
from english_dictionary.scripts.read_pickle import get_dict
import re
import itertools as it

parse_pattern = re.compile("(?P<letter>[A-Z]+)\d*\.png")
file_suffix = ".png"
base_img_path = pl.Path("./imgs")
eng_dict = get_dict()


def get_letters():
    letters = []
    for img_path in base_img_path.iterdir():
        re_match = parse_pattern.match(img_path.name)
        if not re_match:
            continue

        letter = re_match.groupdict()["letter"]
        letters.append(letter)

    return letters


if __name__ == "__main__":
    letters = get_letters()
    for scrambled in it.permutations(letters):
        word = "".join(scrambled).lower()
        if word in eng_dict:
            print("Candidate:", word)
