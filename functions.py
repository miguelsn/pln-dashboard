import plotly.graph_objects as go
def createEmptyFig(msg, bg):
    fig2 = go.Figure()
    fig2.update_layout(
        transition_duration=500,
        xaxis = {
            "visible": False,
        },
        yaxis = {
            "visible": False
        },
        plot_bgcolor=bg,
        paper_bgcolor=bg,
        )
    fig2.add_annotation(
            text = msg,
            xref = "paper",
            yref = "paper",
            font=dict(
                color="#ffffff",
                size = 28
            ),
            showarrow = False,
        )
    return fig2