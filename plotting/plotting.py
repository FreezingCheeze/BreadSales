import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# Plot given x over y
# Assumes y grouped by x
def plot(x_label, x_values, y_label, y_values, title="Graph", color='blue'):
    plt.figure(figsize=(15, 5))
    plt.plot(x_values, y_values, color=color)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


def plot_twice(x_label, x_values, y_label, ya_values, yb_values, title="Graph"):
    print('here')
    plt.figure(figsize=(15, 5))
    plt.plot(x_values, ya_values)
    plt.plot(x_values, yb_values, color='green')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

def plot_thrice(x_label, x_values, y_label, ya_values, yb_values, yc_values, title="Graph"):
    plt.figure(figsize=(15, 5))
    plt.plot(x_values, ya_values)
    plt.plot(x_values, yb_values, color='green')
    plt.plot(x_values, yc_values, color='orange')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

def scatter_and_plot(x_label, x_values, y_label, y_values, Y_pred, title="Graph"):
    plt.figure(figsize=(15, 5))
    plt.scatter(x_values, y_values)
    plt.plot(x_values, y_values, color='red')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

