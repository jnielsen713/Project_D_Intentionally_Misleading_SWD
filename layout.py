# Imports --------------------------------------------------------------------------------------------------------------
from dash import dcc, html
import dash_bootstrap_components as dbc

# Components -----------------------------------------------------------------------------------------------------------

# Sections -------------------------------------------------------------------------------------------------------------

header = dbc.Row(
    [
        dbc.Col(
            [
                html.Div(
                    [
                        html.H1("Football Players are getting WORSE at the Game"),
                        html.H4("Joshua Nielsen - CS-150 - Prof. Mike Ryu")
                    ],
                    id="title_box"
                )
            ],
            width=12
        )
    ],
    class_name="grass",
)

body = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Card(
                    [
                        html.H2("Declining Statistics"),
                        dcc.RadioItems(
                            options={
                                "PPG": "Points Per Game",
                                "TD": "Touchdowns Per Game",
                                "FGM": "Field Goals Per Game",
                            },
                            value="PPG",
                            id="declining_checklist",
                            # inline=True
                        ),
                        dcc.Graph(id="declining_chart")
                    ]
                )
            ],
            width=6
        ),
        dbc.Col(
            [
                dbc.Card(
                    [
                        html.H2("Old Age"),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.P("Player"),
                                        dcc.Dropdown(
                                            id="player_selector",
                                            options=[
                                                "Aaron Rodgers",
                                                "Joe Flacco",
                                                "Tom Brady",
                                                "Travis Kelce",
                                                "Trent Williams"
                                            ],
                                            value="Aaron Rodgers"
                                        ),
                                        dcc.Graph(id="age_chart", style={"margin": "10px"}),
                                        html.P("Year"),
                                        dcc.Slider(
                                            id="age_slider",
                                            min=2020,
                                            max=2025,
                                            value=2023,
                                            marks={
                                                2020: '\'20',
                                                2021: '\'21',
                                                2022: '\'22',
                                                2023: '\'23',
                                                2024: '\'24',
                                                2025: '\'25',
                                            },
                                            step=1
                                        )
                                    ],
                                    width=8
                                ),
                                dbc.Col(
                                    [
                                        html.H5("Visual Representation"),
                                        html.Img(id="age_image")
                                    ],
                                    width=4
                                )
                            ]
                        )
                    ]
                )
            ],
            width=6
        )
    ]
)

body2 = dbc.Row(
    [
        dbc.Col(
            [
                dbc.Card(
                    [
                        html.H2("Center Graphic"),
                        html.P("Comparison value:"),
                        dcc.Dropdown(
                            options={
                                "GAS": "Average gas price in the United States (Dollars per Gallon)",
                                "CROCS": "Annual revenue of Crocs (Millions of Dollars)",
                                "EGGS": "Average price of a dozen eggs in the US (Dollars)",
                                "GOOGLE": "Number of google queries for \"How to play football\"",
                                "BEER": "Quantity of beer consumed per capita (Gallons)"
                            },
                            value="GAS",
                            id="comparison_dropdown"),
                        html.Br(),
                        dcc.Graph(id="comparison_chart")
                    ]
                )
            ]
        )
    ],
    style={"background-color": "lightblue"}
)

footer = dbc.Row(
    [
        dbc.Col(
            [
                html.A(
                    [
                        html.P("Learn more!")
                    ],
                    href="https://docs.google.com/document/d/1Bt9OuVD1Gn0TYPKlI4Fig6TBDdvXIZmCtA8wLLeSrX8"
                )
            ]
        )
    ],
    class_name="grass"
)


# Main Layout ----------------------------------------------------------------------------------------------------------

def create_layout():
    return dbc.Container(
        [
            header,
            body,
            body2,
            footer
        ],
        className="row",
        fluid=True,
        style={"background-color": "lightblue"}
    )
