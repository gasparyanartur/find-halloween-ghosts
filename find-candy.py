import requests
import pathlib as pl
import itertools as it

if __name__ == "__main__":
    base_url = "https://newminds.se/wp-content/uploads/2023/10/{query}.png"

    postfixes = ["", "1", "2"]
    ignore_letters = {"X"}
    letters = [
        chr(code)
        for code in range(ord("A"), ord("Z") + 1)
        if chr(code) not in ignore_letters
    ]
    file_suffix = ".png"
    base_img_path = pl.Path("./imgs")

    queries = [letter + postfix for (letter, postfix) in it.product(letters, postfixes)]
    base_img_path.mkdir(exist_ok=True)

    for query in queries:
        file_name = query + ".png"
        img_path = base_img_path / (query + ".png")
        if img_path.exists():
            continue

        response = requests.get(base_url.format(query=query))
        if response.status_code != requests.codes.ok:
            continue

        print("Found ghost:", query)
        data = response.content
        with open(img_path, "wb") as f:
            f.write(data)
