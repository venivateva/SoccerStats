import pandas as pan
import numpy as num
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

dashapp = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# data exploration ######

# datafile=pan.read_csv("/Users/venelinavateva/PycharmProjects/Soccer/soccerstats.csv", index_col=0)
datafile=pan.read_csv("C:\PythonProjects\SoccerStats\soccerstats.csv", index_col=0)



dframe = pan.DataFrame(datafile)
print(dframe)

dcolumns = dframe.columns
# print(dcolumns)

# types=dframe["Name","Value","Age","Nationality","Wage","Body Type","Joined","Work Rate"].dtypes
# print(types)


# Data Cleanup#


dframe[["Wage","Value"]]=dframe[["Wage","Value"]].replace(to_replace=r'[€]+',value='',regex=True)

dframe.Value = (dframe.Value.replace(r'[KM]+$', '', regex=True).astype(float) * \
dframe.Value.str.extract(r'[\d\.]+([KM]+)', expand=False).fillna(1).replace(['K','M'], [10**3, 10**6]).astype(int))

dframe.Wage = (dframe.Wage.replace(r'[KM]+$', '', regex=True).astype(float) * \
dframe.Wage.str.extract(r'[\d\.]+([KM]+)', expand=False).fillna(1).replace(['K','M'], [10**3, 10**6]).astype(int))


# print(dframe[["Wage","Value"]].sort_values(by="Wage",ascending=True))

sortedframe = dframe.sort_values(by="ID",ascending=False)

sortedframe.drop_duplicates()
sortedframe.dropna()

smalldataset = sortedframe[0:100]
print(smalldataset[["Name","Value","Age","Nationality","Wage","Body Type","Joined","Work Rate"]])

colors={
        'background':'#bbd7ff',
        'text':'#000000'}

dashapp.layout = html.Div(style={'backgroundColor':colors['background']},
                          children=
    [html.H1(children='Soccer Stats',style={'textAlign':'center', 'color':colors['text']}),

    dcc.Graph(
        id='Nationality and Wage',
        figure={
            'data': [
                go.Scatter(
                    x=sortedframe[sortedframe['Nationality'] == i]['Wage'],
                    y=sortedframe[sortedframe['Nationality'] == i]['Value'],
                    text=sortedframe[sortedframe['Nationality'] == i]['Name'],
                    mode='markers',
                    opacity=0.7,
                    hoverinfo=sortedframe[sortedframe["Name"]==i]["Name"],
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in sortedframe.Nationality.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Wage'},
                yaxis={'title': 'Value'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    dashapp.run_server(debug=True)




# print(sortedframe)


