import itertools
from helper import get_input_file_lines, Timer
import math


def main(lines: list[str]):
    directions = [c == "R" for c in lines[0]]

    lookup = {
        line.split()[0]: (line[7:15].split(", ")[0], line[7:15].split(", ")[1])
        for line in lines[1:]
    }

    p1_answer = part_1(directions, lookup)
    print(f"P1 answer:", p1_answer)

    p2_answer = part_2(directions, lookup)
    print(f"P2 answer:", p2_answer)


@Timer()
def part_1(directions: list[bool], lookup: dict[str, tuple[str, str]]) -> int:
    current_node = "AAA"

    step_count = 0
    for dir in itertools.cycle(directions):
        step_count += 1
        current_node = lookup[current_node][dir]

        if current_node == "ZZZ":
            break

    return step_count


@Timer()
def part_2(directions: list[bool], lookup: dict[str, tuple[str, str]]) -> int:
    starter_nodes = [node for node in lookup.keys() if node[2] == "A"]

    factors: list[int] = []
    for node in starter_nodes:
        current_node = node
        step_count = 0
        for dir in itertools.cycle(directions):
            step_count += 1
            current_node = lookup[current_node][dir]

            if current_node[2] == "Z":
                break

        factors.append(step_count)

    return math.lcm(*factors)


if __name__ == "__main__":
    main(get_input_file_lines("dec_08", "sample"))
    main(get_input_file_lines("dec_08"))
