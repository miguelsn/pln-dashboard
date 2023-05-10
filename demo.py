# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from getdatafromcsv import getData
stylesheet = ["https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css"]
app = Dash(__name__, external_stylesheets=stylesheet)

colors = {
    'background': '#2D2727',
    'text': '#ffffff'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
data, weeks = getData()
print(weeks)
print(data["Topic1"])

fig = px.line(x=weeks, y=data["Topic1"], markers=True)

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    xaxis_title="Semanas",
    yaxis_title="Probabilidad",
    font_color="#ffffff"
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
            id="input",
            className = "form-control",
            type="text",
            placeholder="topic",
            debounce = True,
            style = {
            "width": "20%"}
        )
    ]
    ),
        html.H4(children='Presencia del tema:',
            className = "m-3",
            style={
            'color': colors['text']
        },),
    dcc.Graph(
        id='graph',
        figure=fig
    )
])
@app.callback(
    Output('graph', 'figure'),
    Input('input', 'value'))
def update_graph(topic):
    new_df = data.get(topic, None)
    
    if new_df is None:
        fig = go.Figure()
        fig.update_layout(
          transition_duration=500,
          xaxis = {
            "visible": False,
          },
          yaxis = {
            "visible": False
          },
          plot_bgcolor=colors['background'],
          paper_bgcolor=colors['background'],
        )
        fig.add_annotation(
            text = "Tema no encontrado",
            xref = "paper",
            yref = "paper",
            font=dict(
                color="#ffffff",
                size = 28
            ),
            showarrow = False,
        )
        return fig
        return {
        "layout": {
            "tranition_duration": 500,
            "xaxis": {
                "visible": False
            },
            "yaxis": {
                "visible": False
            },
            "plot_bgcolor": colors["background"],
            "paper_bgcolor": colors["background"],
            "annotations": [
                {
                    "text": "Tema no encontrado",
                    "xref": "paper",
                    "yref": "paper",
                    "font_color": "#ffffff",
                    "showarrow": False,
                    "font": {
                        "size": 28
                    }
                }
            ]
        }
}
    fig = px.line(x=weeks, y=new_df, markers=True)
    fig.update_layout(
        transition_duration=500,
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        xaxis_title="Semanas",
        yaxis_title="Probabilidad",
        font_color="#ffffff"
    )
    return fig
if __name__ == '__main__':
    app.run_server(debug=True)