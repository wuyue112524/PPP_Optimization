import pandas as pd
import plotly as py
import plotly.graph_objects as go

#Visualization moduel
class DataframePlot():

	def __init__(self,dataframe):
		self.df = dataframe

	def layout(self,graph_title = "",y_title = "", x_title = ""):
		#default no title
		layout = go.Layout(
        title = graph_title,
        yaxis = dict(title=y_title),
        xaxis = dict(title = x_title))
		return layout


	def single_scatter_trace(self,x_colname,y_colname, legend=""):
		trace = go.Scatter(x = self.df[x_colname], y=self.df[y_colname], mode='lines',
				name =legend)
		return trace

	def multiple_scatter_trace(self,x_colname,y_colname_list,legend_list=[""]):
		storage = []
		#create multiple trace 
		for item in y_colname_list:
			y_colname = item  
			
			#let the legend name be the y colname if legend list is empty
			if legend_list == [""]:
				legend_list = y_colname_list
				legend_index = y_colname_list.index(item)
				legend = legend_list[legend_index]
			
			#find the legend if there is one, make sure the length of lengend list and y colname list are the same  
			else:
				assert len(legend_list)== len(y_colname_list)
				legend_index = y_colname_list.index(item)
				legend = legend_list[legend_index]

			obj = DataframePlot(self.df)
			trace = obj.single_scatter_trace(x_colname = x_colname, y_colname = y_colname, legend=legend)
			storage.append(trace)
		return storage

    #need to specify layout first
	def scatter_plot(self,x_colname,y_colname_list,legend_list=[""],graph_title = "",y_title = "", x_title = ""):
		obj = DataframePlot(self.df)
		layout = obj.layout(graph_title= graph_title,y_title = y_title,x_title = x_title)
		data = obj.multiple_scatter_trace(x_colname,y_colname_list,legend_list=legend_list)
		fig = go.Figure(data=data,layout =layout)
		#py.offline.plot(fig)
		fig.show()
