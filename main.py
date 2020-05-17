import pandas as pd
import plotly
import plotly.graph_objects as go
from plotly import offline
from plotly.subplots import make_subplots

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

df = pd.read_csv('Metro Bank-20200516-184807.csv')


def plotbar(x):
    fig = make_subplots(specs=[[{'secondary_y': False}]])
    fig.add_trace(
        go.Bar(
            x=df.Category,
            y=df.Expense,
            marker=dict(color='cornflowerblue', line=dict(color='cornflowerblue', width=1), opacity=1),
            name='pounds'),
        secondary_y=False)
    fig.update_layout(title='test',
                      titlefont=dict(size=26),
                      bargap=x,
                      barmode='stack',
                      legend_orientation='h',
                      legend=dict(font=dict(size=16)),
                      plot_bgcolor='rgb(255,255,255)')
    fig.update_yaxes(title_text="Cum. Cashflow & Repayment Amount",
                     secondary_y=False,
                     showline=True,
                     mirror=True,
                     linecolor='black',
                     titlefont=dict(size=20),
                     tickfont=dict(size=16))
    # fig.update_yaxes(title_text='', secondary_y=True, showline=True, linecolor='black',
    #                  titlefont=dict(size=20), tickfont=dict(size=16))
    fig.update_xaxes(showline=True, linecolor='black', mirror=True, tickfont=dict(size=16))
    return fig




# fig.show()



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-bar'),
    dcc.Slider(
        id='slider',
        min=0,
        max=1,
        value=0,
        marks={str(i): i for i in [0, 0.25, 0.5, 0.75, 1]},
        step=None
    )
])

@app.callback(
    Output('graph-bar', 'figure'),
    [Input('slider', 'value')])
def update_fig(x):
    return plotbar(x)


app.run_server(debug=False)
