from pathlib import Path

INPUT_FOLDER = Path(__file__).parent.parent / "input"


def get_input_file_lines(filename: str) -> list[str]:
    input_text = (INPUT_FOLDER / filename).read_text("UTF-8")
    lines = input_text.split("\n")
    return [line for line in lines if line]
