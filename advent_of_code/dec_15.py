from helper import get_input_file_lines, Timer


@Timer()
def main(lines: list[str]):
    total = 0
    for chars in lines[0].split(","):
        value = 0
        for char in chars:
            value = ((value + ord(char)) * 17) % 256

        total += value

    print(total)


if __name__ == "__main__":
    main(get_input_file_lines("dec_15", "sample"))
    main(get_input_file_lines("dec_15"))
