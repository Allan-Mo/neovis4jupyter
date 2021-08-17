# neovis4jupyter

A tool to visualize graph database queries from Neo4j in the Jupyter Notebook, when you ***CANNOT*** access databases by javascript-driver, but ***CAN*** access from jupyter server.

Notebook query --> Jupyter server(using py2neo) --> Neo4j --> Jupyter server --> Notebook --> Graph render

## Refer
[neovis.js](https://github.com/neo4j-contrib/neovis.js)

[neo4jupyter](https://github.com/merqurio/neo4jupyter)

## Requirement
[py2neo](https://github.com/py2neo-org/py2neo)

## Install
`pip install neovis4jupyter-0.1-py3-none-any.whl`

## Docs

### Load all the javascript.

```python
from neovis4jupyter import Graph
Graph.init_notebook_mode()
```
***or*** with vis configuration
```python
from neovis4jupyter import Graph
Graph.init_notebook_mode(labels={},relationships={},arrows=False,debug=True)
```

See [config object from neovis.js](https://github.com/neo4j-contrib/neovis.js).

### Connect to database.
All arguments will be passed to py2neo.Graph(). see [details](https://py2neo.org/2021.1/workflow.html#py2neo.Graph)

```python
graph = Graph('bolt://localhost:7687',auth=('neo4j', 'password'))
```
You can provide ***name*** argument to select database, which default value is ***None***.

### Draw the graph

```python
graph.draw('match (n) return n limit 10')
```

