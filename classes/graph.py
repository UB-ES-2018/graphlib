__author__ = """\n""".join(['Sergio Montoya de Paco <sergio.mp1710@gmail.com>'])
"""
Clase Graph, que representa un grafo (conjunto de vértices y aristas). La clase representa un grafo no dirigido, por lo tanto, 
las aristas que unen dos vértices son bidireccionales.
Métodos:
    -def __init__(self): Constructor de la clase, donde se crea el conjunto vacío de nodos y aristas.
    -def node(self)(@property): Atributo que es un conjunto de nodos en un diccionario, donde la key es el nodo y el value son 
     los atributos del nodo.
    -def edge(self)(@property): Atributo que es un conjunto de aristas en un diccionario, donde la key es un nodo y los value 
     son diccionarios, donde la key es el nodo al que va la arista y el value los atributos de dicha arista.
    -def nodes(self): Devuelve una lista con todos los nodos.
    -def edges(self): Devuelve una lista con tuplas que representan las aristas (nodo1,nodo2)
    -def add_node(self, node, attr_dict=None): Añade el nodo al diccionario de nodos, si el elemento ya existía, en caso de que
     se especifique un nuevo atributo, se añadirá al diccionario de atributos. 'attr_dict' = dictionary
    -def add_edge(self, node1, node2, attr_dict=None): Añade una arista al diccionario de aristas, si uno de los nodos 
     especificados no existe, se creará el nodo de forma implícita. 'attr_dict' especifica un atributo para la arista, si ya
     contençia un atributo, se añade al diccionario de atributos.
    -def add_nodes_from(self, node_list, attr_dict=None): Añade todos los nodos especificados en la lista 'node_list', a todos
     les añade los atributos especificados en 'attr_dict'.
    -def add_edges_from(self, edge_list, attr_dict=None): Añade todas las aristas especificadas en la lista 'edge_list', a todas
     les añade los atributos especificados en 'attr_dict'.
    -def degree(self,node): Devuelve el grado del nodo 'node', si el nodo no existe, lanza una excepción.
    -def __getitem__(self, node): Devuelve los nodos a los cuales está conectado el nodo 'node', con los respectivos atributos
     de cada arista, en forma de diccionario. {node1:{attributes},node2:{attributes}}.
    -def __len__(self): Devuelve el número de nodos que hay en el grafo.
    -def neighbors(self, node): Devuelve una lista con los nodos incidentes en el nodo 'node'.
    -def remove_node(self, node1): Elimina el nodo 'node1' del grafo y todas sus aristas incidentes.
    -def remove_edge(self, node1, node2): Elimina la arista (node1,node2) del grafo. Ímplicitamente se elimina también la 
     arista (node2,node1).
    -def remove_nodes_from(self, node_list): Elimina todos los nodos especificados en la lista de nodos 'node_list'. De igual 
     forma que en la función remove_node, se elimina el nodo y todas sus aristas incidentes.
    -def remove_edges_from(self, edge_list): Elimina todas las aristas especificadas en la lista de aristas 'edge_list'. De igual
     forma que en la función remove_edge, se elimina la arista birideccional (se elimina tanto (node1,node2) como (node2,node1)).
"""
class Graph:
    
    def __init__(self):
        self._nodes = {}
        self._edges = {}
    
    @property
    def node(self):
        return self._nodes
    
    @property
    def edge(self):
        return self._edges
    
    def nodes(self):
        return list(self._nodes.keys())
    
    def edges(self):
        edges_list = []
        for n1 in self._edges.keys():
            for n2 in self._edges[n1].keys():
                if not (n2,n1) in edges_list:
                    edges_list.append((n1,n2))
        return edges_list
    
    # Método para añadir nodo, si existe el nodo, simplemente se actualizará, siempre se actualiza
    # con attr_dict, pero si el nodo no existe, entonces crea un diccionario nuevo y entonces actualiza
    def add_node(self, node, attr_dict={}):
        if node not in self._nodes: self._nodes[node]={}
        self._nodes[node].update(attr_dict)

    
    # Método para añadir arista, si cualquiera de los nodos pasados por parámetro no existe,
    # entonces se llama la función add_node() ya que controlando los nodos por separado, se
    # comprobarán los nodos igualmente. Si la arista no existe se crea y luego se actualiza
    def add_edge(self, node1, node2, attr_dict={}):
        self.add_node(node1)
        self.add_node(node2)
        
        if node1 not in self._edges: self._edges[node1]={node2:attr_dict}
        if node2 not in self._edges: self._edges[node2]={node1:attr_dict}
            
        if node1 not in self._edges[node2]: self._edges[node2][node1]=attr_dict
        else: self._edges[node2][node1].update(attr_dict)
            
        if node2 not in self._edges[node1]: self._edges[node1][node2]=attr_dict
        else: self._edges[node1][node2].update(attr_dict)
            
                
        
    def add_nodes_from(self, node_list, attr_dict=None):
        for new_node in node_list: self.add_node(new_node,attr_dict)
    
    def add_edges_from(self, edge_list, attr_dict=None):
        for new_edge in edge_list: self.add_edge(new_edge[0],new_edge[1],attr_dict)

    # Método para medir el grado de un nodo, puede no existir en las aristas, porque puede
    # ser un grafo no conexo, retorna error en caso de no existir el nodo
    def degree(self, node):
        if node in self._edges: return len(self._edges[node])
        if node in self._nodes: return 0
        raise ValueError("Node does'nt exists")
    
    # Método para retornar los nodos adyacentes al nodo parámetro, retorna error en caso de no
    # existir, o vacío en caso de no estar conectado
    def __getitem__(self, node):
        if node in self._edges: return self._edges[node]
        if node in self._nodes: return {}
        raise ValueError("Node does'nt exists")
    
    def __len__(self):
        return len(self._nodes)
    
    # Método para devolver los nodos vecinos, reutilizando el error del método __getitem__
    def neighbors(self, node):
        return [n for n in self[node]]
    
    #  Método para eliminar nodos y aristas o retornamos error si no existe
    def remove_node(self, node1):
        if node1 not in self._nodes: raise ValueError("Node does'nt exists")
        if node1 in self._edges: del self._edges[node1]
        del self._nodes[node1]
        for n in self._edges:
            if node1 in self._edges[n]: del self._edges[n][node1]
                
                
    
    # Método para eliminar arista, si no existen en el diccionario de aristas, tampoco en
    # en el diccionario de nodos, ya que se va controlando al añadir nodos o aristas, si no
    # están conectados, intenta remover igualmente, aunque no exista arista
    def remove_edge(self, node1, node2):
        if node1 not in self._nodes or node2 not in self._nodes: raise ValueError("Node does'nt exists")
        if node1==node2: raise ValueError("Same node")
        if node1 in self._edges and node2 in self._edges:
            if node1 in self._edges[node2]:
                del self._edges[node1][node2]
                del self._edges[node2][node1]
    
    def remove_nodes_from(self, node_list):
        for node in node_list:
            self.remove_node(node)
    
    def remove_edges_from(self, edge_list):
        for edge in edge_list:
            self.remove_edge(edge[0],edge[1])


