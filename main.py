
import csv


def read_bat(n):
    bat_info = []
    with open("bat.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            bat_info.append(row[n])

    return bat_info


if __name__ == '__main__':
    current_bat = read_bat(0)
    print(current_bat)