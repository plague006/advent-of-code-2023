from pathlib import Path

# Create folders
project_folder = (Path(__file__).parent / "advent_of_code").resolve()
project_folder.mkdir(exist_ok=True)
input_folder = (Path(__file__).parent / "input").resolve()
input_folder.mkdir(exist_ok=True)

# Create helper
helper = project_folder / "aoc_helper.py"
helper.write_text(
    r"""from pathlib import Path

INPUT_FOLDER = Path(__file__).parent.parent / "input"


def get_input_file_lines(filename: str) -> list[str]:
    input_text = (INPUT_FOLDER / filename).read_text("UTF-8")
    lines = input_text.split("\n")
    return [line for line in lines if line]
"""
)

# Create daily files
for day_of_month in range(1, 26):
    date = f"dec_{day_of_month:02d}"

    (input_folder / f"{date}_sample.txt").touch(exist_ok=True)
    (input_folder / f"{date}_real.txt").touch(exist_ok=True)

    solution_file = project_folder / f"{date}.py"
    solution_file.write_text(
f"""from helper import get_input_file_lines


def main(lines: list[str]):
    ...


if __name__ == "__main__":
    main(get_input_file_lines("{date}_sample.txt"))
"""
    )
