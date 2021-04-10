import matplotlib.pyplot as plt
import numpy as np

def plot_inputs(inp, ant, title, filename_preffix=None):
	plt.clf()
	
	plt.figure(figsize=(6,3))

	plt.plot(np.arange(0,10,0.01),ant, color='red', label="Antecedente")
	plt.plot(np.arange(0,10,0.01),inp,"--", color='black', label="Entrada")

	plt.xlabel('$X$')
	plt.xlim(0,10)
	plt.legend()

	plt.grid(True)

	plt.title(title)

	if filename_preffix is not None:
		plt.savefig(filename_preffix+"_inputs.png")
	else:
		plt.show()

def plot_outputs(output, cons, title, filename_preffix=None):
	plt.clf()
	
	plt.figure(figsize=(6,3))

	plt.plot(np.arange(0,10,0.01),cons, color='red', label="Consequente")
	plt.plot(np.arange(0,10,0.01),output,"--", color='black', label="Saída")
	plt.fill_between(np.arange(0,10,0.01), 0, output, facecolor="orange")

	plt.xlabel('$Y$')
	plt.xlim([0,10])
	plt.legend()

	plt.grid(True)

	plt.title(title)

	if filename_preffix is not None:
		plt.savefig(filename_preffix+"_outputs.png")
	else:
		plt.show()