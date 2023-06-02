import matplotlib.pyplot as plt
import numpy as np
import defuzz

def plot_inputs(inp, antecedents, title, filename_preffix=None):
	plt.clf()
	
	plt.figure(figsize=(6,3))

	color_palette = ['red', 'blue', 'green']

	i = 1
	for ant, color in zip(antecedents, color_palette):
		plt.plot(np.arange(0,10,0.01),ant, color=color, label=r"$A_"+str(i)+"$")
		i+=1

	plt.plot(np.arange(0,10,0.01),inp,"--", color='black', label="Input")

	plt.xlabel('$X$')
	plt.xlim(0,10)
	plt.legend()

	plt.grid(True)

	plt.title(title)
	plt.tight_layout()

	if filename_preffix is not None:
		plt.savefig(filename_preffix+"_inputs.png")
	else:
		plt.show()

def plot_outputs(output, consequents, title, filename_preffix=None):
    plt.clf()
    
    plt.figure(figsize=(6,3))

    color_palette = ['red', 'blue', 'green']

    i = 1
    for cons, color in zip(consequents, color_palette):
        plt.plot(np.arange(0,10,0.01),cons, color=color, label=r"$B_"+str(i)+"$")
        i+=1

    plt.plot(np.arange(0,10,0.01),output,"--", color='black', label="Output")
    plt.fill_between(np.arange(0,10,0.01), 0, output, facecolor="orange")
    
    centroid = defuzz.centroid(output, np.arange(0,10,0.01))
    mom = defuzz.mom(output, np.arange(0,10,0.01))

    plt.axvline(centroid, color="cyan", linestyle="dotted", label="centroid")
    plt.axvline(mom, color="magenta", linestyle=(0,(5,10)), label="mean of maximum")

    plt.xlabel('$Y$')
    plt.xlim([0,10])
    plt.legend()

    plt.grid(True)

    plt.title(title)
    plt.tight_layout()

    if filename_preffix is not None:
        plt.savefig(filename_preffix+"_outputs.png")
    else:
        plt.show()


def plot_detailed(output, output_detailed, consequents, title, filename_preffix=None):
	plt.clf()
	
	plt.figure(figsize=(6,3))

	color_palette = ['red', 'blue', 'green']

	i = 1
	for cons, color in zip(consequents, color_palette):
		plt.plot(np.arange(0,10,0.01),cons, color=color, label=r"$B_"+str(i)+"$")
		i+=1

	plt.plot(np.arange(0,10,0.01),output,"x-", color='blue', label="Final output")
	plt.plot(np.arange(0,10,0.01),output_detailed,"--", color='black', label="Output")
	plt.fill_between(np.arange(0,10,0.01), 0, output_detailed, facecolor="orange")

	plt.xlabel('$Y$')
	plt.xlim([0,10])
	plt.legend()

	plt.grid(True)

	plt.title(title)
	plt.tight_layout()

	if filename_preffix is not None:
		plt.savefig(filename_preffix+"_outputs.png")
	else:
		plt.show()


def plot_detailed_beta(output, output_beta, beta, consequents, title, filename_preffix=None):
	plt.clf()
	
	plt.figure(figsize=(6,3))

	color_palette = ['red', 'blue', 'green']

	i = 1
	for cons, color in zip(consequents, color_palette):
		plt.plot(np.arange(0,10,0.01),cons, color=color, label=r"$B_"+str(i)+"$")
		i+=1

	plt.plot(np.arange(0,10,0.01),output,"x-", color='blue', label="Final output")
	plt.plot(np.arange(0,10,0.01),output_beta,"--", color='black', label="Output")
	plt.axhline(y=beta, color='green', linestyle='--', label="beta")
	plt.fill_between(np.arange(0,10,0.01), 0, output_beta, facecolor="orange")

	plt.xlabel('$Y$')
	plt.xlim([0,10])
	plt.legend()

	plt.grid(True)

	plt.title(title)
	plt.tight_layout()

	if filename_preffix is not None:
		plt.savefig(filename_preffix+"_outputs.png")
	else:
		plt.show()


def plot_detailed_inputs(output, detailed_inp, detailed_ant, consequents, title, filename_preffix=None):
	plt.clf()
	
	plt.figure(figsize=(6,3))

	color_palette = ['red', 'blue', 'green']

	i = 1
	for cons, color in zip(consequents, color_palette):
		plt.plot(np.arange(0,10,0.01),cons, color=color, label=r"$B_"+str(i)+"$")
		i+=1

	plt.plot(np.arange(0,10,0.01),output,"x-", color='blue', label="Final output")
	plt.plot(np.arange(0,10,0.01),detailed_inp,"--", color='cyan', label=r"$A'(x)$")
	plt.plot(np.arange(0,10,0.01),detailed_ant,"--", color='purple', label=r"$A_i(x)$")	
	plt.fill_between(np.arange(0,10,0.01), 0, output, facecolor="orange")

	plt.xlabel('$Y$')
	plt.xlim([0,10])
	plt.legend()

	plt.grid(True)

	plt.title(title)
	plt.tight_layout()

	if filename_preffix is not None:
		plt.savefig(filename_preffix+"_outputs.png")
	else:
		plt.show()