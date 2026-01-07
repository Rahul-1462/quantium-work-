from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd


def create_app():
    # Load data
    df = pd.read_csv("data.csv")
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    # Create Dash app
    app = Dash(__name__)

    # Layout
    app.layout = html.Div(
        style={
            "fontFamily": "Arial",
            "maxWidth": "1200px",
            "margin": "auto",
            "padding": "20px"
        },
        children=[

            # Header
            html.H1(
                "Pink Morsel Sales Visualiser",
                style={
                    "textAlign": "center",
                    "color": "#E91E63"
                }
            ),

            html.P(
                "Explore Pink Morsel sales over time. Use the radio buttons to filter by region.",
                style={
                    "textAlign": "center",
                    "fontSize": "18px"
                }
            ),

            # Radio buttons
            dcc.RadioItems(
                id="region-filter",
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                ],
                value="all",
                inline=True,
                style={
                    "textAlign": "center",
                    "marginBottom": "20px",
                    "fontSize": "16px"
                }
            ),

            # Graph
            dcc.Graph(id="sales-line-chart")
        ]
    )

    # Callback to update chart
    @app.callback(
        Output("sales-line-chart", "figure"),
        Input("region-filter", "value")
    )
    def update_chart(selected_region):
        if selected_region == "all":
            filtered_df = df
        else:
            filtered_df = df[df["region"].str.lower() == selected_region]

        fig = px.line(
            filtered_df,
            x="date",
            y="sales",
            title="Pink Morsel Sales Over Time",
            labels={
                "date": "Date",
                "sales": "Total Sales"
            }
        )

        fig.update_layout(
            plot_bgcolor="#F9F9F9",
            paper_bgcolor="#F9F9F9"
        )

        return fig

    return app
