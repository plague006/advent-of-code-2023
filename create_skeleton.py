from pathlib import Path

# Create folders
project_folder = (Path(__file__).parent / "advent_of_code").resolve()
project_folder.mkdir(exist_ok=True)
input_folder = (Path(__file__).parent / "input").resolve()
input_folder.mkdir(exist_ok=True)

# Create helper
helper = project_folder / "helper.py"
helper.write_text(
    r"""from pathlib import Path
from typing import Literal

try:
    import codetiming

    Timer = codetiming.Timer
except ModuleNotFoundError:
    Timer = lambda: lambda x: x

INPUT_FOLDER = Path(__file__).parent.parent / "input"


def _select_input_file(folder: Path, day: str) -> Path:
    real = folder / f"{day}_real.txt"
    sample = folder / f"{day}_sample.txt"
    if real.exists() and real.read_text():
        print(f"Using {real}")
        return real
    elif sample.exists() and sample.read_text():
        print(f"Using {sample}")
        return sample
    else:
        raise ValueError(f"Neither {real} nor {sample} contain any text!")


def get_input_file_lines(
    day: str, file_selection: Literal["sample"] | Literal["real"] | None = None
) -> list[str]:
    if file_selection:
        file = INPUT_FOLDER / (f"{day}_{file_selection}.txt")
    else:
        file = _select_input_file(INPUT_FOLDER, day)

    input_text = file.read_text("UTF-8")
    lines = input_text.split("\n")
    return [line for line in lines if line]
""",
    newline="\n",
)

# Create daily files
for day_of_month in range(1, 26):
    date = f"dec_{day_of_month:02d}"

    (input_folder / f"{date}_sample.txt").touch(exist_ok=True)
    (input_folder / f"{date}_real.txt").touch(exist_ok=True)

    solution_file = project_folder / f"{date}.py"
    if solution_file.exists():
        continue

    solution_file.write_text(
        f"""from helper import get_input_file_lines, Timer


@Timer()
def main(lines: list[str]):
    ...


if __name__ == "__main__":
    main(get_input_file_lines("{date}", "sample"))
    main(get_input_file_lines("{date}"))
""",
        newline="\n",
    )
