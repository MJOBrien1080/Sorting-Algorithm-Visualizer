import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Algorithms with Color Tracking
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            colors = ["blue"] * n
            colors[j] = "red"
            colors[j + 1] = "red"

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            yield arr, colors

        # mark sorted portion
        colors = ["green" if x >= n - i - 1 else "blue" for x in range(n)]
        yield arr, colors


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            colors = ["blue"] * n
            colors[i] = "green"
            colors[j] = "red"
            colors[min_idx] = "yellow"

            if arr[j] < arr[min_idx]:
                min_idx = j

            yield arr, colors

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        colors = ["green" if x <= i else "blue" for x in range(n)]
        yield arr, colors


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            colors = ["blue"] * len(arr)
            colors[j] = "red"
            colors[j + 1] = "red"

            arr[j + 1] = arr[j]
            j -= 1

            yield arr, colors

        arr[j + 1] = key

        colors = ["green" if x <= i else "blue" for x in range(len(arr))]
        yield arr, colors


# Visualization w/ graphing
def visualize_sort(data, algorithm, speed):
    generator = algorithm(data)

    fig, ax = plt.subplots()
    bars = ax.bar(range(len(data)), data, color="blue")

    ax.set_title(algorithm.__name__)

    def update(frame):
        arr, colors = frame
        for rect, val, color in zip(bars, arr, colors):
            rect.set_height(val)
            rect.set_color(color)

    ani = animation.FuncAnimation(
        fig,
        func=update,
        frames=generator,
        repeat=False,
        interval=speed
    )

    plt.show()

# Negative num failsafe
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive number greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Main
def main():
    size = get_positive_int("Enter number of elements: ")
    speed = get_positive_int("Enter speed (ms, e.g. 10-100): ")

    data = [random.randint(1, 100) for _ in range(size)]

    print("\nChoose sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")

    choice = input("Enter choice: ")

    if choice == '1':
        visualize_sort(data, bubble_sort, speed)
    elif choice == '2':
        visualize_sort(data, selection_sort, speed)
    elif choice == '3':
        visualize_sort(data, insertion_sort, speed)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
