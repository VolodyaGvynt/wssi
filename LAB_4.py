
import numpy as np 
import matplotlib.pyplot as plt
import networkx as nx

class Neuron:  
    def __init__(self, n_inputs, bias = 0., weights = None):  
        self.b = bias
        if weights: self.ws = np.array(weights)
        else: self.ws = np.random.rand(n_inputs)

    def _f(self, x): #activation function (here: leaky_relu)
        return max(x*.1, x)   

    def __call__(self, xs): #calculate the neuron's output: multiply the inputs with the weights and sum the values together, add the bias value,
                            # then transform the value via an activation function
        return self._f(xs @ self.ws + self.b) 


class NeuronNetwork:
  def __init__(self):
    self.structure = [3, 4, 4, 1]
    self.layers = []

    for i in range(len(self.structure) - 1):
      layer =  [Neuron(self.structure[i]) for _ in range(self.structure[i + 1])]
      self.layers.append(layer)

  def forward(self, x): 
    for layer in self.layers:
      x = np.array([neuron(x) for neuron in layer])
    return x

  def visualize(self):
    G = nx.DiGraph()
    pos = {}
    layer_start = 0

    for i, layer_size in enumerate(self.structure):
      next_layer_start = layer_start + layer_size

      for j in range(layer_size):
        node = layer_start + j
        G.add_node(node)
        pos[node] = (i, -j)
        
        if i > 0: 
          for prev in range(layer_start - self.structure[i-1], layer_start):
            G.add_edge(prev, node)

      layer_start = next_layer_start

    nx.draw(G, pos, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=10)
    plt.show()

network = NeuronNetwork()
network.visualize()
