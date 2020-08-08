
import matplotlib.pyplot as plt
import csv


def read_bat(n):
    bat_info = []
    with open("bat.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            bat_info.append(float(row[n]))

    column_x = [n+1 for n in range(len(bat_info))]
    return bat_info, column_x


def draw_bat(bat, x):
    plt.plot(x, bat, marker=".")
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    current_bat, x = read_bat(3)
    draw_bat(current_bat, x)
