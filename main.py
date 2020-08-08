import matplotlib.pyplot as plt
import csv


def read_bat(n):
    bat_info = []
    with open("bat.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            bat_info.append(float(row[n]))

    return bat_info


def draw_bat(bat, x):
    plt.plot(x, bat, marker=".")
    plt.grid(True)
    plt.show()


def draw_bats(*args, x=None):
    n = 0
    color = ["blue", "green", "red"]
    label = ["current", "max", "design"]
    plt.grid(True)
    for y in args:
        plt.plot(x, y, color=color[n], label=label[n])
        n += 1

    plt.legend(loc=0)
    plt.show()


if __name__ == '__main__':
    current_bat = read_bat(0)
    max_bat = read_bat(1)
    design_bat = read_bat(2)
    rate_bat = read_bat(3)
    draw_bats(current_bat, max_bat, design_bat, x=[n + 1 for n in range(len(current_bat))])
