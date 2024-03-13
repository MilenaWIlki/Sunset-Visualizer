import matplotlib.pyplot as plt

def draw_sunset():
    colors = ['#FF5733', '#FF8C00', '#FFD700', '#BFFF00', '#40E0D0', '#1E90FF']
    plt.figure(figsize=(8, 6))
    for i, color in enumerate(colors):
        plt.axhspan(i, i + 1, color=color)
    plt.title("Sunset Visualizer")
    plt.xlabel("Time")
    plt.ylabel("Altitude")
    plt.yticks(range(len(colors)), ["Horizon", "Clouds", "Sun", "Sky", "Upper Atmosphere", "Space"])
    plt.show()

draw_sunset()
