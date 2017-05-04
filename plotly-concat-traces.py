import plotly
from plotly.graph_objs import Scatter, Scatter3d, Layout, Data
import numpy as np

xp = np.linspace(0,10,3)
y1 = np.linspace(0,25,3)
y2 = np.linspace(0,50,3)
x = np.concatenate([xp, [np.nan], xp])
y = np.concatenate([y1, [np.nan], y2])

traces = [
    Scatter(
                x = x,
                y = y,
                mode = 'lines')
]
data = Data(traces)
plotly.offline.iplot({
            'data': data,
            'layout': Layout(title='Figure 1')
        })
