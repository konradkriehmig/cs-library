import matplotlib.pyplot as plt

def format():
    plt.style.use("dark_background")

    fig, ax = plt.subplots()

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_position("zero")

    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.tick_params(axis="both", labelsize=5)
    ax.set_xticks(range(-10,11))
    ax.set_yticks(range(-10,11))
    ax.set_aspect("equal")

    return fig, ax
    