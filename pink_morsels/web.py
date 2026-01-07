from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


def create_app():
    # Load processed sales data
    df = pd.read_csv("data.csv")

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Sort by date
    df = df.sort_values("date")

    # Create line chart
    fig = px.line(
        df,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={
            "date": "Date",
            "sales": "Total Sales"
        }
    )

    # Create Dash app
    app = Dash(__name__)

    # Define layout
    app.layout = html.Div([
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={"textAlign": "center"}
        ),

        html.P(
            "Sales before and after the Pink Morsel price increase on January 15, 2021.",
            style={"textAlign": "center"}
        ),

        dcc.Graph(figure=fig)
    ])

    return app
