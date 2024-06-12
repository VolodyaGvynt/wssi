
import numpy as np 
import matplotlib.pyplot as plt
import networkx as nx

class Neuron:  
    def __init__(self, n_inputs, bias = 0., weights = None):  
        self.b = bias
        if weights: self.ws = np.array(weights)
        else: self.ws = np.random.rand(n_inputs) * 0.01

    def _f(self, x): #activation function (here: leaky_relu)
        return max(x*.1, x)   

    def _f_deriv(self, x):
        return 1 if x > 0 else 0.1

    def __call__(self, xs): #calculate the neuron's output: multiply the inputs with the weights and sum the values together, add the bias value,
                            # then transform the value via an activation function
        self.input = xs
        self.z = xs @ self.ws + self.b
        self.out = self._f(self.z)
        return self.out

    def upd_weights(self, d, l_rate):
        self.ws += l_rate * d * self.input
        self.b += l_rate * d 


class NeuronNetwork:
  def __init__(self):
    self.structure = [3, 4, 4, 1]
    self.layers = []

    for i in range(len(self.structure) - 1):
      layer =  [Neuron(self.structure[i]) for _ in range(self.structure[i + 1])]
      self.layers.append(layer)

  def forward(self, x): 
    self.activations = [x]
    for layer in self.layers:
      x = np.array([neuron(x) for neuron in layer])
      self.activations.append(x)
    return x

  def backward(self, y_true, l_rate=0.001):
    deltas = []

    out_layer = self.layers[-1]
    d = [(neuron.out - y_true) * neuron._f_deriv(neuron.z) for neuron in out_layer] 
    deltas.append(d)

    for i in reversed(range(len(self.layers) - 1)):
      layer = self.layers[i]
      next_layer = self.layers[i + 1]
      d = []
      for j, neuron in enumerate(layer):
        error = sum(next_neuron.ws[j] * next_d for next_neuron, next_d in zip(next_layer, deltas[-1]))
        d.append(error * neuron._f_deriv(neuron.z))
      deltas.append(d)

    deltas.reverse()

    for l in range(len(self.layers)):
      layer = self.layers[l]
      for i, neuron in enumerate(layer):
        neuron.upd_weights(deltas[l][i], l_rate)

  def train(self, X, y, epochs = 1000, l_rate = 0.001):
    for e in range(epochs):
            for xi, yi in zip(X, y):
                self.forward(xi)
                self.backward(yi, l_rate)
            if e % 100 == 0:
                loss = np.mean([(self.forward(xi) - yi) ** 2 for xi, yi in zip(X, y)])
                print(f'e:{e},l:{loss}')

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

X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

y = np.array([0, 1, 1, 0])

network.train(X, y, epochs = 1000, l_rate=0.001)

for xi in X:
    out = network.forward(xi)
    print(f"in: {xi},out:{out}")

network.visualize()
