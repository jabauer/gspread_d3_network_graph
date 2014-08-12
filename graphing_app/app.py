import flask
import variables
import gspread #python library for access google spreadsheets
from flask import render_template

app = flask.Flask(__name__)

@app.route('/')
#Root folder displays network graph in d3.js with some explanitory text
def network():
	return render_template('check-network.html')

#Pull data from google spreadsheet and format it for display
#as a network graph in D3.js
@app.route('/data', methods=['GET'])
def nodes_edges():
	#login to google spreadsheet
	gc = gspread.login(variables.email, variables.password)
	sh = gc.open(variables.spreadsheet)
	#sh = gc.open("Test Nodes and Edges")

	#open sheet with node data
	node_data = sh.worksheet(variables.nodes_sheet)
	#export all data in the spreadsheet as a list of lists
	#In this instance we are only interested in the 2nd and 3rd columns
	#or indexes 1,2
	all_nodes = node_data.get_all_values()
	#remove header line
	all_nodes.pop(0)

	#open sheet with edge data
	edges = sh.worksheet(variables.edges_sheet)
	#export all data as list of lists
	#The nodes we want are in Columns 2 and 3
	#at indexes 1 and 2
	all_edges = edges.get_all_values()
	#remove header line
	all_edges.pop(0)


	#Check to make sure all the nodes in a relationship are already in the
	#all_nodes list.  If not add them, or D3 will throw a hissy fit.
	for r in range(len(all_edges)):
		labels = []
		for p in range(len(all_nodes)):
			labels.append(all_nodes[p][1])
		for i in range(1,3):
			if all_edges[r][i] not in labels:
				all_nodes.append(['',all_edges[r][i],"not entered"])

	#Replace node labels in relationship with their node order number
	#which is what d3js requires for the 'source','target' links
	for p in range(len(all_nodes)):
		for r in range(len(all_edges)):
			if all_nodes[p][1] == all_edges[r][1]:
				all_edges[r][1] = p
			if all_nodes[p][1] == all_edges[r][2]:
				all_edges[r][2] = p
	#print all_nodes
	#print all_edges

	#Start to build the json structure
	data = {}
	#First make a list of dictionaries for the nodes
	#Remember it has to be a list to preserve node order
	nodes = []
	for an in all_nodes:
		d = {}
		d["label"] = an[1]
		d["attribute"] = an[2]
		nodes.append(d)
	data["nodes"] = nodes

	#Now make a list of dictionaries for the links
	links = []
	for ae in all_edges:
		d = {}
		d["source"] = ae[1]
		d["target"] = ae[2]
		links.append(d)
	data["links"] = links
	#print data

	return flask.jsonify(data)

if __name__ == '__main__':
	app.run()