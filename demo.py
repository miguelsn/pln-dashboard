# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

stylesheet = ["https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css"]
app = Dash(__name__, external_stylesheets=stylesheet)

colors = {
    'background': '#2D2727',
    'text': '#191919'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background'], "width": "100vw", "height": "100vh", "margin-top": "0"}, children=[
    html.Nav(
        children=[
    html.H4(children='LDA Mañaneras',
            style={
                "position" : "relative",
                "left": "45%"
            })
        ],
        style={
            'textAlign': 'center',
            'color': colors['text'],
        },
        className = "navbar navbar-dark bg-dark p-3 text-light"
    ),

    html.Div(
    className = "p-3",
    style = {
    "textAlign": 'left',
    'color':colors['text']},
    children = [
        dcc.Input(
            id="input_text",
            className = "form-control",
            type="text",
            placeholder="topic",
            style = {
            "width": "20%"}
        )
    ]
    ),
    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)