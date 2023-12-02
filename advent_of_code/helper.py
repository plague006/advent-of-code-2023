from pathlib import Path
from typing import Literal

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
