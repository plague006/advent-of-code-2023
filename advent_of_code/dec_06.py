from helper import get_input_file_lines
import math


def main(lines: list[str]):
    times = [int(i) for i in lines[0].split()[1:]]
    distances = [int(i) for i in lines[1].split()[1:]]

    winning_ways_per_race = []
    for time, distance_to_beat in zip(times, distances):
        ways_to_win = get_ways_to_win(time, distance_to_beat)

        winning_ways_per_race.append(ways_to_win)

    print(f"p1 total:", math.prod(winning_ways_per_race))

    time = int("".join([str(i) for i in times]))
    distance_to_beat = int("".join([str(i) for i in distances]))

    print(f"p2 total:", get_ways_to_win(time, distance_to_beat))


def get_ways_to_win(time: int, distance_to_beat: int) -> int:
    ways_to_win = 0
    for i in range(time + 1):
        distance_traveled = i * (time - i)

        if distance_traveled > distance_to_beat:
            ways_to_win += 1
            continue

        if ways_to_win > 0:
            break
    return ways_to_win


if __name__ == "__main__":
    main(get_input_file_lines("dec_06", "sample"))
    main(get_input_file_lines("dec_06"))
