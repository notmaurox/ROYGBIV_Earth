import plotly
import pandas as pd

def graph(dataFile,titleIN,valueIN,fileNameOut):
    df = pd.read_csv(dataFile)
    # z field must match csv
    data = [ dict(
            type = 'choropleth',
            locations = df['CODE'],
            z = df['VALUE'],
            text = df['COUNTRY'],
            locationmode = "ISO-3",
            ## 0  = highest 
            ## 1 = lowest
            # colorscale = [[0,"rgb(255, 122, 122)"],[0.16,"rgb(255, 196, 122)"],[0.32,"rgb(255, 250, 122)"],\
            #     [0.48,"rgb(140, 255, 122)"],[0.64,"rgb(122, 142, 255)"],[0.80,"rgb(213, 122, 255)"],[1,"rgb(255, 122, 208)"]],
            colorscale = [[0,"rgb(255, 0, 0)"],[0.16,"rgb(255, 165, 0)"],[0.32,"rgb(250, 250, 0)"],\
                [0.48,"rgb(0, 128, 0)"],[0.64,"rgb(46, 108, 241)"],[0.80,"rgb(45, 19, 242)"],[1,"rgb(100, 45, 240)"]],
            autocolorscale = False,
            reversescale = True,
            marker = dict(
                line = dict (
                    color = 'rgb(180,180,180)',
                    width = 0.5
                ) ),
            colorbar = dict(
                autotick = False,
                tickprefix = '',
                title = valueIN +'<br>'),
          ) ]

    layout = dict(
        title = titleIN,
        geo = dict(
            showframe = False,
            showcoastlines = False,
            projection = dict(
                type = 'Mercator'
            )
        )
    )

    fig = dict( data=data, layout=layout )
    plotly.offline.plot( fig, validate=False, filename=fileNameOut )