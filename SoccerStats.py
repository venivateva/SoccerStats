import pandas as pan
import numpy as num
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

dashapp = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#### data exploration ######

dframe=pan.read_csv("/Users/venelinavateva/PycharmProjects/Soccer/soccerstats.csv",index_col=0,)


#dframe=pan.DataFrame(datafile)
print(dframe)

dcolumns=dframe.columns
print(dcolumns)

types=dframe["Name","Value","Age","Nationality","Wage","Body Type","Joined","Work Rate"].dtypes
print(types)
#dframe.Wage=dframe.Wage.astype(str)
#print(types)


#Data Cleanup#

# replacebadnum = {
#     'K' : 1000,
#     'M' : 1000000}
#
#
# def good_number(s):
#     multiply = 1.0
#     while s[-1] in good_number:
#         multiply *= good_number[s[-1]]
#         s = s[:-1]
#     return float(s) * multiply

dframe["Wage","Value"]=dframe["Wage","Value"].replace(to_replace=r'[€]+',value='',regex=True)
dframe["Wage","Value"].replace({'K': '*1e3', 'M': '*1e6'}, regex=True)
dframe["Wage","Value"].pan.eval.astype(int)


print(dframe[["Wage","Value"]])





sortedframe=dframe.sort_values(by="ID",ascending=False)

sortedframe.drop_duplicates()
sortedframe.dropna()

#smalldataset=sortedframe[0:1000]
#print(smalldataset[["Name","Value","Age","Nationality","Wage","Body Type","Joined","Work Rate"]])

#
# dashapp.layout = html.Div([
#     dcc.Graph(
#         id='Nationality and Wage',
#         figure={
#             'data': [
#                 go.Scatter(
#                     x=sortedframe[sortedframe['Nationality'] == i]['Wage'],
#                     y=sortedframe[sortedframe['Nationality'] == i]['Value'],
#                     text=sortedframe[sortedframe['Nationality'] == i]['Nationality'],
#                     mode='markers',
#                     opacity=0.7,
#                     marker={
#                         'size': 15,
#                         'line': {'width': 0.5, 'color': 'white'}
#                     },
#                     name=i
#                 ) for i in sortedframe.Nationality.unique()
#             ],
#             'layout': go.Layout(
#                 xaxis={'type': 'log', 'title': 'Wage'},
#                 yaxis={'title': 'Value'},
#                 margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
#                 legend={'x': 0, 'y': 1},
#                 hovermode='closest'
#             )
#         }
#     )
# ])
#
# if __name__ == '__main__':
#     dashapp.run_server(debug=True)




#print(sortedframe)

