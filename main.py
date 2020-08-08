
import csv


def read_bat(n):
    bat_info = []
    with open("bat.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            bat_info.append(float(row[n]))

    column_x = [n+1 for n in range(len(bat_info))]
    return bat_info, column_x

    return bat_info


if __name__ == '__main__':
    current_bat = read_bat(0)
    print(current_bat)