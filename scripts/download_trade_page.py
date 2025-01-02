from datetime import datetime
from pathlib import Path


from utils import make_request


def main():
    file_path = "tests/resources"
    file_name = f"{datetime.today().strftime("%m-%d-%Y")}_tradepage.txt"

    if Path(f"{file_path}/{file_name}").exists():
        return

    res = make_request()

    with open(f"{file_path}/{file_name}", "w") as file:
        file.write(res.text)


if __name__ == "__main__":
    main()
