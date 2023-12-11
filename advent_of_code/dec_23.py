from helper import get_input_file_lines, Timer


@Timer()
def main(lines: list[str]):
    ...


if __name__ == "__main__":
    main(get_input_file_lines("dec_23", "sample"))
    main(get_input_file_lines("dec_23"))
