import matplotlib.pyplot as plt

class Grapher:
    def __init__(self):
        self.results = {}

    def add_result(self, interval, process_count, avg_time):
        if interval not in self.results:
            self.results[interval] = []
        # Store as LIST instead of tuple
        self.results[interval].append([process_count, avg_time])

    def plot(self, title="Average Time vs Number of Processes"):
        for interval in self.results:
            # Sort by process count (first element of each list)
            self.results[interval].sort(key=lambda item: item[0])
            x = []
            y = []
            for item in self.results[interval]:
                x.append(item[0])  # process_count
                y.append(item[1])  # avg_time

            plt.plot(x, y, marker='o', label=f"Interval {interval}")
        plt.title(title)
        plt.xlabel("Number of Processes")
        plt.ylabel("Average Time in System")
        plt.legend()
        plt.grid(True)
        plt.show()