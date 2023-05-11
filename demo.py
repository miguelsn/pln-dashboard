# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from getdatafromcsv import getData
from functions import createEmptyFig
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
print(data)

fig = px.line(x=weeks, y=data["Topic1"], markers=True)
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    xaxis_title="Semanas",
    yaxis_title="Probabilidad",
    font_color="#ffffff"
)

fig2 = createEmptyFig("Seleccione una semana", colors['background'])


amlo = "assets/amlo.jpg"
app.layout = html.Div(style={'backgroundColor': colors['background'], "margin-top": "0"}, children=[
    html.H1(children = ["Topic Modeling de las conferencias diarias del presidente Andres Manuel López Obrador"],
            style={
            'color': colors['text']
        },className = "text-center mt-5 mb-5"),
    html.H5(children = "Rodrigo Nevarez Escobar, Kevin David Ruiz González, Miguel Sebastian Navarro Islas, Jesús Giovanni Corral Valdez",
            className = "text-center mt-5 mb-2",
            style={
            'color': colors['text']
        }),
    #html.Div(children = [html.Div(children = [html.Img(src = amlo, style={'height':'50%', 'width':'50%'})], className = "row justify-content-center")], className = "container-fluid justify-content-center"),
    html.H3(children = ["Introducción"],
            style = {"color": colors["text"]},
            className = "ml-3"),
    html.P("""El modelado de temas es una tecnica que permite encontrar patrones y estructuras en amplias colecciones de texto. Una
        de las tecnicas mas utilizadas para esto es el LDA (Latent Dirichlet Allocation) el cual es un modelo probabilistico que encuentra
        temas en un texto basado en la frecuencia de las palabras. En este proyecto, se utiliza una implementación de LDA a un corpus 
        formado por los títulos y primer párrafo de los boletines de las conferencias mañaneras del presidente. De esta forma, obtenemos una aproximación
        de los temas más frecuentes e importantes en cierto periodo de tiempo.""",
           style={"color": colors["text"]},
           className = "ml-3"),
    html.H3(children = ["Metodología"],
            style = {"color": colors["text"]},
            className = "ml-3"),
    html.P("""pendiente jijijijiji""",
           style={"color": colors["text"]},
           className = "ml-3"),
    html.H3(children = ["Visualización de los resultados"],
            style = {"color": colors["text"]},
            className = "ml-3"),
    html.H4(children = ["Graficación por tema"],
            style = {"color": colors["text"]},
            className = "ml-3 mt-3"),
    html.Div(
    className = "p-3 row w-100",
    style = {
    "textAlign": 'left',
    'color':colors['text']},
    children = [
        html.Div(
            className = "col-sm",
            children = [
            html.P("Temas:", style={"color": colors["text"]}),
            dcc.Input(
                id="input",
                className = "form-control w-50",
                type="text",
                placeholder="Topic 1",
                debounce = True,
                style = {
                "width": "20%"}
            )
            ]
        ),
        html.Div(
            className = "col-sm",
            children = [
            dcc.Input(
                id="input2",
                className = "form-control col-sm float-right mt-5 w-50",
                type="text",
                placeholder="Topic 1",
                debounce = True,
                style = {
                "width": "20%"}
            )
            ]
        )]
    ),
      #  html.H4(children='Presencia del tema:',
      #      className = "m-3",
      #      style={
      #      'color': colors['text']
       # },),
    dcc.Graph(
        id='graph',
        figure=fig
    ),
    html.H4(children = ["Graficación por fecha"],
        style = {"color": colors["text"]},
        className = "ml-3 mt-3 mb-4"),
    dcc.Dropdown(
        weeks,
        id = "drop",
        placeholder="Selecciona una semana",
        className = "w-25 ml-3"
),
dcc.Graph(
        id='graph2',
        figure=fig2
    ),
])
@app.callback(
    Output('graph', 'figure'),
    Input('input', 'value'),
    Input("input2", "value"))
def update_graph(topic, topic2):
    new_df1 = data.get(topic, None)
    new_df2 = data.get(topic2, None)
    topics = []
    print(new_df1)
    if new_df2 is not None:
        if new_df1 is not None:
            new_df = {topic: new_df1, topic2: new_df2}
            topics = [topic, topic2]
        else:
            new_df = {topic2: new_df2}
            topics = [topic2]
    elif new_df1 is not None:
        new_df = {topic: new_df1}
        topics = [topic]
    if topics==[]:
        return createEmptyFig("Tema no encontrado", colors['background'])
    fig = go.Figure()
    for topic in topics:
        fig.add_trace(go.Scatter(x=weeks, y=new_df[topic], name=topic))
    fig.update_layout(
        transition_duration=500,
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        xaxis_title="Semanas",
        yaxis_title="Probabilidad",
        font_color="#ffffff"
    )
    return fig

@app.callback(
    Output(component_id = "graph2", component_property="figure"),
    Input(component_id = "drop", component_property="value"))
def update_graph2(week):
    if week not in weeks:
        return createEmptyFig("Seleccione un tema", colors['background'])
    index = weeks.index(week)
    probs = {"Tema": [], "Probabilidad": []}
    for x in data.keys():
        probs["Tema"].append(x)
        probs["Probabilidad"].append(data[x][index])
    fig = px.bar(probs, x="Tema", y="Probabilidad")
    fig.update_layout(
        transition_duration=500,
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        xaxis_title="Temas",
        yaxis_title="Probabilidad",
        font_color="#ffffff"
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)