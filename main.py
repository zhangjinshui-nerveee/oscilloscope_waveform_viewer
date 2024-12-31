import numpy as np
import pandas as pd
import plotly.express as px
import pathlib
wavedata_path = pathlib.Path('data')
# create pandas instance
wavedata_no = 4843
wavedata = pd.read_csv(wavedata_path/"tek{}.csv".format(wavedata_no), 
                       low_memory=False, # dtype=float, 
                       on_bad_lines="skip", 
                       skiprows=20)
# use plotly to plot all traces out
print(wavedata.keys())
# Create a bar plot
fig = px.bar(wavedata, x='TIME', y='CH1', title='Sample Bar Plot')

# Show the plot
fig.show()
# show plot in browser
