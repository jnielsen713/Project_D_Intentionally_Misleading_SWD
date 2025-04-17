# Imports --------------------------------------------------------------------------------------------------------------
from dash import Input, Output, State
import plotly.graph_objects as go

from main import app, declining_figure, age_figure, comparison_figure


# Callbacks ------------------------------------------------------------------------------------------------------------
def register_callbacks(app):
    @app.callback(Output("declining_chart", "figure"),
                  Input("declining_checklist", "value"))
    def update_declining(stat):
        fig = declining_figure(stat)
        return fig

    @app.callback(Output("age_chart", "figure"),
                  Output("age_image", "src"),
                  Input("age_slider", "value"),
                  Input("player_selector", "value"))
    def update_age(year, player):
        src = "assets/age_" + str(year - 2020) + ".png"
        fig = age_figure(year, player)
        return fig, src

    @app.callback(Output("comparison_chart", "figure"),
                  Input("comparison_dropdown", "value"))
    def update_comparison(data):
        fig = comparison_figure(data)
        return fig
