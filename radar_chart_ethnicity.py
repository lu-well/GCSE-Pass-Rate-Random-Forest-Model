import numpy as np
import matplotlib.pyplot as plt


# create function which produces a radar chart for multiple groups and normalises the scales for all variables 
def radar_chart_multi(categories, group_values, ranges, group_labels=None, title="Selected Ethnic Backgrounds and"
                                                                                 " their Interactions with Influential"
                                                                                 " Variables"):
    N = len(categories)
    if not all(len(vals) == N for vals in group_values):
        raise ValueError("Each group's values must match the number of categories")
    if len(ranges) != N:
        raise ValueError("ranges must match the number of categories")
    if group_labels and len(group_labels) != len(group_values):
        raise ValueError("group_labels must match the number of groups")

    # specify axis angles
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

    # create axes for variables
    plt.xticks(angles[:-1], categories)
    ax.set_rlabel_position(0)
    plt.yticks([0.25, 0.5, 0.75], ["", "", ""], color="grey", size=7)
    plt.ylim(0, 1)

    # plot groups
    for idx, values in enumerate(group_values):
        # normalisation of values
        normalized = [
            (v - r[0]) / (r[1] - r[0]) if r[1] != r[0] else 0.5
            for v, r in zip(values, ranges)
        ]
        normalized += normalized[:1]  # close polygon

        label = group_labels[idx] if group_labels else f"Group {idx+1}"
        ax.plot(angles, normalized, linewidth=2, linestyle='solid', label=label)
        ax.fill(angles, normalized, alpha=0.15)

    plt.title(title, size=14, y=1.1)
    plt.legend(loc='upper left', bbox_to_anchor=(1.2, 1.1))
    plt.show()


# create data to be used and display in radar chart
categories = ["FSM Eligibility", "Absence Rate", "Number of Pupils in the School", "Religious", "Selective",
              "Ofsted Average Score"]
ranges = [(0, 50), (0, 15), (300, 1500), (0, 15), (0, 35), (1, 4)]

group_values = [
    [38, 14, 539, 8, 0, 2.4],  # Group 1
    [13, 6, 1305, 12, 13, 1.6],  # Group 2
    [9, 5, 1180, 8, 31, 1.4]   # Group 3
]

group_labels = ["traveller of Irish heritage", "white and Asian", "Chinese"]

radar_chart_multi(categories, group_values, ranges, group_labels)
