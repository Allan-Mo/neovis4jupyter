import json
import os
import uuid

from IPython.display import HTML, Javascript, display
from py2neo import Graph as Py2NeoGraph


def vis_network(nodes, edges):
    """
    Creates the HTML page with all the parameters
    :param nodes: The nodes to be represented an their information.
    :param edges: The edges represented an their information.
    :param physics: The options for the physics of vis.js.
    :return: IPython.display.HTML
    """
    base = open(os.path.join(os.path.dirname(__file__), 'assets/index2.html')).read()
    nodes = [{"identity": x.identity, "labels": list(x._labels), "properties": {i: x.get(i) for i in x.keys()}} for x in nodes]
    edges = [{"identity": x.identity, "type":x.__class__.__name__, "start": x.nodes[0].identity,"end":x.nodes[-1].identity, "properties":{i:x.get(i) for i in x.keys()}} for x in edges]

    html = base.format(uuid=uuid.uuid4().hex,nodes=json.dumps(nodes), edges=json.dumps(edges))

    return HTML(html)

class Graph(object):
    """
    g = Graph()
    g.init_notebook_mode()
    g.draw("match (n) return n limit 10")
    """
    def __init__(self,uri=None,auth=None):
        uri = uri if uri else "neo4j://localhost:7687"
        auth = auth if auth else ("neo4j","psbc6885")
        self.graph = Py2NeoGraph(uri,auth=auth)
    def run(self,*args,**kwargs):
        return self.graph.run(*args,**kwargs)
    def draw(self,*args,**kwargs):
        cursor = self.graph.run(*args, **kwargs)
        subgraph = cursor.to_subgraph()
        nodes = subgraph.nodes
        edges = subgraph.relationships
        return vis_network(nodes,edges)
    @classmethod
    def init_notebook_mode(cls,labels={},relationships={},arrows=False,debug=True):
        dir = os.path.dirname(__file__)
        js_vis_file = os.path.join(dir, 'assets/myz_neovis.js')
        css_file = os.path.join(dir, 'assets/vis.css')
        # display(
        #     Javascript(data=open(js_vis_file).read(),
        #                css=f'{css_file}')
        # )
        html = []
        html.append(f"<script> {open(js_vis_file).read()} </script>")
        html.append(f"<style> {open(css_file).read()} </style>")

        js_jquery_file = os.path.join(dir, 'assets/jquery-3.2.1.min.js')
        # display(
        #     Javascript(data=open(js_jquery_file).read())
        # )
        html.append(f"<script> {open(js_jquery_file).read()} </script>")
        js_raw = """
            var myzvis_config = {{
                labels: {labels},
                relationships: {relationships},
                arrows: {arrows},
                console_debug: {debug}
                }};
            myzvis = new NeoVis.default(myzvis_config);
            window['myzvis'] = myzvis;
            """.format(labels=json.dumps(labels),
                       relationships=json.dumps(relationships),
                       arrows="true" if arrows else "false",
                       debug="true" if debug else "false")
        # display(
        #     Javascript(data=js_raw)
        # )
        html.append(f"<script> {js_raw} </script>")
        return HTML('\n'.join(html))