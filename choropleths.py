import pandas as pd
import plotly.express as px
from uk_geojson_data import uk_geojson

# retrieve geojson file information
district_ids = [feature["properties"]["LAD22NM"] for feature in uk_geojson["features"]]

# read data from csv
df = pd.read_csv(r"district specific.csv", index_col=False) # modify file path for raw data input

# create choropleth showing number of pupis in each district
fig = px.choropleth(
    df,
    geojson=uk_geojson,
    locations="District",
    featureidkey="properties.LAD22NM",
    color="Number of Pupils",
    color_continuous_scale="Viridis_r",
    range_color=(2000, 30000),
    title="Number of Pupils per District"
)

fig.update_traces(
    marker_line_color='white',
    marker_line_width=1
)

fig.update_geos(fitbounds="locations", visible=False)

fig.show()

# create choropleth showing absence rate in each district
fig = px.choropleth(
    df,
    geojson=uk_geojson,
    locations="District",
    featureidkey="properties.LAD22NM",
    color="% Absence Rate",
    color_continuous_scale="Viridis_r",
    range_color=(5, 12),
    title="Absence Rate per District"
)

fig.update_traces(
    marker_line_color='white',
    marker_line_width=1
)

fig.update_geos(fitbounds="locations", visible=False)

fig.show()

# create choropleth showing FSM eligibility in each district
fig = px.choropleth(
    df,
    geojson=uk_geojson,
    locations="District",
    featureidkey="properties.LAD22NM",
    color="% FSM",
    color_continuous_scale="Viridis_r",
    range_color=(10, 35),
    title="FSM Eligibility % per District"
)

fig.update_traces(
    marker_line_color='white',
    marker_line_width=1
)

fig.update_geos(fitbounds="locations", visible=False)

fig.show()

# create choropleth showing absence rate and FSM eligibility interaction in each district
fig = px.choropleth(
    df,
    geojson=uk_geojson,
    locations="District",
    featureidkey="properties.LAD22NM",
    color="FSM Absence Interaction",
    color_continuous_scale="Viridis_r",
    range_color=(60, 250),
    title="FSM and Absence Interaction"
)

fig.update_traces(
    marker_line_color='white',
    marker_line_width=1
)

fig.update_geos(fitbounds="locations", visible=False)

fig.show()
