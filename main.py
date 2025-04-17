# Imports --------------------------------------------------------------------------------------------------------------
from dash import Dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go

# Initialization and Data Processing -----------------------------------------------------------------------------------

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.QUARTZ, dbc.icons.FONT_AWESOME],
)

football_stats_df = pd.read_csv("data/football_stats.csv")

football_stats_df["TD"] = football_stats_df["TD"].str.replace(",", "")
football_stats_df["TD"] = football_stats_df["TD"].astype(int)
football_stats_df["TD"] = football_stats_df["TD"] / football_stats_df["GP"]

football_stats_df["FGM"] = football_stats_df["FGM"] / football_stats_df["GP"]

age_df = pd.read_csv("data/age.csv")

comparison_df = pd.read_csv("data/comparison_stats.csv")
comparison_df = comparison_df[:-2]
comparison_df[1:] = comparison_df[1:].astype(float)

# Functions ------------------------------------------------------------------------------------------------------------

def declining_figure(stat):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            mode="lines",
            x=football_stats_df["SEASON"],
            y=football_stats_df[stat],
            line=dict(color="red")
        )
    )
    fig.update_xaxes(range=[2020, 2023])
    fig.update_layout(
        xaxis_title="Year",
        xaxis=dict(tickvals=[2020, 2021, 2022, 2023])
    )
    return fig


def age_figure(year, player):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            mode="lines",
            x=age_df["YEAR"],
            y=age_df[player],
            line=dict(color="orange")
        )
    )

    fig.update_xaxes(range=[2020, 2025])

    fig.update_layout(
        title="Age of " + player,
        xaxis_title="Year",
        yaxis_title="Age",

        xaxis=dict(tickvals=[2020, 2021, 2022, 2023, 2024, 2025]),

        shapes=[
            dict(
                type="line",
                x0=year,
                x1=year,
                y0=0,
                y1=1,
                xref="x",
                yref="paper",
                line=dict(color="gray", width=2, dash="dash")
            )
        ]
    )
    return fig


def comparison_figure(data):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            mode="lines",
            x=football_stats_df["SEASON"],
            y=football_stats_df["PPG"],
            line=dict(color="red"),
            yaxis="y1"
        )
    )
    fig.add_trace(
        go.Scatter(
            mode="lines",
            x=comparison_df["YEAR"],
            y=comparison_df[data],
            line=dict(color="orange"),
            yaxis="y2"
        )
    )

    fig.update_xaxes(range=[2020, 2023])
    #fig.update_yaxes(range=[21, 25])

    fig.update_layout(
        xaxis=dict(
            title="Year",
            tickvals=[2020, 2021, 2022, 2023]
    ),
        yaxis=dict(
            title="Points Per Game",
            side="left",
        ),
        yaxis2=dict(
            title=data,
            side="right",
            overlaying="y"
        ),
        showlegend=False
    )
    return fig
