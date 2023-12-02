import re
from helper import get_input_file_lines


def main(lines: list[str]):
    part_1_validity_thresholds = {"red": 12, "green": 13, "blue": 14}
    part_1_total = part_2_total = 0

    for line in lines:
        game_info, hint = line.split(":")
        game_running_total = 1

        valid_game = True
        for color in part_1_validity_thresholds.keys():
            color_values = [int(num) for num in re.findall(rf"(\d+) {color}", hint)]
            color_max = max(color_values)
            game_running_total *= color_max

            if color_max > part_1_validity_thresholds[color]:
                valid_game = False

        part_2_total += game_running_total
        if valid_game:
            part_1_total += int(game_info.split(" ")[1])

    print("Part 1:", part_1_total)
    print("Part 2:", part_2_total)


if __name__ == "__main__":
    main(get_input_file_lines("dec_02"))
