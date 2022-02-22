import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import csv
df = pd.read_csv("data.csv")
studentD = df.loc[df["student_id"] == "TRL_987"]
fig = go.Figure(go.Bar(x = studentD.groupby("level")["attempt"].mean(),y = ["level1","level2","level3","level4"],orientation = 'h'))
fig.show()