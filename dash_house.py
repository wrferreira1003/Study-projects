from email.mime import application
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import numpy as np
import dash

from re import template
from tempfile import tempdir
import plotly.graph_objects as go

df   = pd.read_csv('kc_house_data.csv')
data = pd.read_csv('dataset_mapa.csv')

mean_lat = df.lat.mean()
mean_long = df.long.mean()

#---------------------------------------------------------------------------------------------------------------
#Insights

#Imóveis que possuem vista para água, são 30% mais caros, na media..
h1= df[['waterfront', 'price']].groupby(['waterfront']).mean().reset_index()
figl = px.bar(h1, x='waterfront', y='price')
figl.update_layout(template='plotly_dark', paper_bgcolor="rgba(0, 0, 0, 0)")

#Imóveis que sofreram reformas são 43.37% mais caros em media
#Coluna discriminando se o imovel foi ou nao renovado
df.loc[df['yr_renovated'] == 0, 'renovated'] = 'no'
df.loc[df['yr_renovated'] > 0, 'renovated'] = 'yes'
h6 = df[['renovated', 'price']].groupby('renovated').mean().reset_index()
figl1 = px.bar(h6, x='renovated', y='price')
figl1.update_layout(template='plotly_dark', paper_bgcolor="rgba(0, 0, 0, 0)")


# Coluna contendo apenas o mês da publicacao do imovel para a venda
df['month'] = pd.to_datetime(df['date']).dt.month

#No verão os imoveis vendem -2.91% em relaçao a primavera (maior estação de venda)
df.loc[(df['month'] >= 6) & (df['month'] <= 8), 'season'] = 'summer'
df.loc[(df['month'] >= 9) & (df['month'] <= 11), 'season'] = 'Autumn'
df.loc[(df['month'] == 12) | (df['month'] <= 2), 'season'] = 'Winter'
df.loc[(df['month'] >= 3) & (df['month'] <= 5), 'season'] = 'Spring'

h7 = df[['season', 'price']].groupby(['season']).count().sort_values(by='price', ascending=False).reset_index()
h7.rename(columns= {'season':'Season', 'price': 'Count'}, inplace=True)
h7_perc = (h7.loc[1, 'Count'] / h7.loc[0, 'Count'] -1) *100
igl2 = px.bar(h7, x='Season', y='Count')
igl2.update_layout(template='plotly_dark', paper_bgcolor="rgba(0, 0, 0, 0)")

#-----------------------------------------Data do mapa-------------------------------------------------------

data.loc[data['price'] > 2000000, 'price'] = 2000000
data.loc[data['price'] < 100000, 'price'] = 100000

#------------------------------------------------------------------------------------------------------------------
#Mapas interativos

#px.set_mapbox_access_token('pk.eyJ1Ijoid3JmZXJyZWlyYSIsImEiOiJjbDJxcml1YngwMGduM2NwZXkyeGx2bXR6In0.Smk9XrVHXr-I7qdmmkpFtg')
fig = go.Figure()
fig.update_layout(template='plotly_dark', paper_bgcolor="rgba(0, 0, 0, 0)")


#------------------------------Layout----------------------------------------------------------------------------



app = dash.Dash(__name__ , external_stylesheets= [dbc.themes.DARKLY],
                                                meta_tags=[{'name': 'viewport',
                                                            'content':'width=device-width, initial-scale=1.0'}])
application= app.server

app.layout = dbc.Container([

                dbc.Row([
                    
                    dbc.Col([
                    
                        html.H1('Dashboard House Rocket',
                            className= 'text-center text primary, display-2 shadow')
                            ],width=12),
                
                ]),
#------------------------------------------------------------------------------------------------------------------
                dbc.Row([
                    
                    dbc.Col( html.H4('Principais Insights!',
                                    className= 'text-left',),
                                    width=12),
                ]),
#------------------------------------------------------------------------------------------------------------------
                
                dbc.Row([

                    dbc.Col([ #coluna1
                    
                        dcc.Graph(id= 'bar-fig', figure= figl),
                        html.P('Imóveis no litoral com visão para o mar são na média 212.64% mais caros que os demais.',
                            className= 'display-20 shadow'),

                    ],sm=12, md=4),

                    dbc.Col([ #coluna2
                    
                        dcc.Graph(id= 'bar-fig1', figure= figl1),
                        html.P('Imóveis que sofreram reformas são 43.37% mais caros em media.',
                            className= 'display-20 shadow'),

                    ],sm=12, md=4),

                    dbc.Col([ #Coluna3
                    
                        dcc.Graph(id= 'bar-fig2', figure= igl2),
                        html.P('No verão os imoveis vendem -2.91% em relaçao a primavera (maior estação de venda).',
                            className= 'display-20 shadow'),

                    ],sm=12, md=4)

                ]),
                        
                dbc.Row([       
                        dbc.Col([

                            html.H4("Filtrar Pelo Distrito", style={"margin-top": "50px", "margin-bottom": "25px"}),

                            dcc.Dropdown(
                                id="location_dropdown",
                                options=[{"label": x, "value": x} for x in data.zipcode.unique() ],
                                value= 0,
                                placeholder= "Selecione um Distrito"
                            ),
                        ],sm=12, md=6),

                        dbc.Col([

                            html.H4("Filtrar Imoveis apto ou não para compra", style={"margin-top": "50px", "margin-bottom": "25px"}),
                            
                            dcc.Dropdown(
                                id="status_dropdown",
                                options=[{"label": x, "value": x} for x in data.status.unique() ],
                                value= 0,
                                placeholder= "buy or not buy"
                                
                            ),
                        ],sm=12, md=6),


                ]),

                dbc.Row([
                        dcc.Graph(id= 'map-graph', figure=fig)
                        ], style={"height": "80vh"})
                


])

@app.callback(
     Output('map-graph', 'figure' ),
    [Input('location_dropdown', 'value'),
     Input('status_dropdown', 'value')]
)

def update_graph(color_map, status_map):

    px.set_mapbox_access_token('pk.eyJ1Ijoid3JmZXJyZWlyYSIsImEiOiJjbDJxcml1YngwMGduM2NwZXkyeGx2bXR6In0.Smk9XrVHXr-I7qdmmkpFtg')
    
    if (color_map is None) & (status_map is None):
        df_aux = data.copy()

    elif (color_map == 0) & (status_map == 0):
        df_aux = data.copy()
    
    elif(color_map != 0) & ((status_map is None) or (status_map ==0) ): 
        df_aux = data[(data['zipcode'] == color_map)] 
    
    elif((color_map is None) or (color_map ==0)) & (status_map != 0 ):
        df_aux = data[(data['status'] == status_map)]

    else:
        df_aux = data[(data['zipcode'] == color_map) & (data['status'] == status_map) ]

    status_map = 'price' #Variavel de teste 
    color_rgb = px.colors.sequential.GnBu

    df_quantiles= data[status_map].quantile(np.linspace(0, 1, len(color_rgb))).to_frame()
    df_quantiles=(df_quantiles - df_quantiles.min()) / (df_quantiles.max() - df_quantiles.min())
    df_quantiles['colors'] = color_rgb

    df_quantiles.set_index(status_map, inplace=True)
    color_scale = [[i, j] for i , j in df_quantiles['colors'].iteritems()]


    map_fig = px.scatter_mapbox(df_aux, lat="lat", lon="long", color='price',
                size='price', size_max=15, zoom=10, opacity=0.4)

    map_fig.update_coloraxes(colorscale = color_scale)
    
    map_fig.update_layout(mapbox= dict(center=go.layout.mapbox.Center(lat=mean_lat, lon=mean_long)),
                                template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)",
                                margin=go.layout.Margin(l=10, r=10, t=10, b=10),)

    return map_fig


if __name__ == '__main__':
    app.run_server(debug=False, port=8080)