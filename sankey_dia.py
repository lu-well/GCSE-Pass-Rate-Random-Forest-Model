import plotly.graph_objects as go

# specify colours to be used in diagram
colors = [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22"
]

# create and plot Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
      pad=15,
      thickness=20,
      line=dict(color="black", width=0.5),
      label=["Academies", "Local authority maintained schools", "Free Schools", "Special schools",
             "Independent schools", "Religious", "Non-religious", "Selective", "Non-Selective"],
      color=colors
    ),
    link=dict(
      source=[7, 7, 8, 8, 8, 8, 8, 0, 1, 2, 0, 1, 2, 3, 4],
      target=[0, 1, 0, 1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 6, 6],
      value=[140, 20, 1818, 503, 109, 91, 3, 295, 158, 17, 1663, 365, 92, 91, 3]
    ))])

fig.update_layout(title_text="Selective and Religious Admissions per Establishment Type", font_size=30)
fig.show()
