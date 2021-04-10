import os

import combinations
import plot

class Experiment:

	def __init__(self, name, description, inp, ant, cons, tnorm, implication):
		self.name = name
		self.description = description
		self.inp = inp
		self.ant = ant
		self.cons = cons
		self.tnorm = tnorm
		self.implication = implication

	def make_dir(self):
		if not os.path.exists('./experiments/'+self.name):
			os.mkdir('./experiments/'+self.name)

	def generate_description(self):
		with open('./experiments/'+self.name+'/description.txt', 'w') as f:
			f.write("Name: {}\n".format(self.name))
			f.write("Description: {}\n".format(self.description))
		

	def run_combinations(self):
		outputs = [{
					'name': 'bks_conj',
					'function':combinations.bks_conj,
					'output': []
				},{
					'name': 'bks_imp',
					'function':combinations.bks_imp,
					'output': []
				},{
					'name': 'cri_conj',
					'function':combinations.cri_conj,
					'output': []
				},{
					'name': 'cri_imp',
					'function':combinations.cri_imp,
					'output': []
				}]

		for comb in outputs:
			comb['output'] = comb['function'](self.inp, self.ant, self.cons, self.tnorm, self.implication)

		return outputs

	def generate_plots(self, outputs):
		for comb in outputs:
			filename_preffix = "./experiments/"+self.name+"/"+self.name+"_"+comb['name']

			plot.plot_inputs(self.inp, self.ant, "Entradas", filename_preffix=filename_preffix)

			plot.plot_outputs(comb['output'], self.cons, "Saídas", filename_preffix=filename_preffix)

	def run_full_experiment(self):
		self.make_dir()

		self.generate_description()

		outputs = self.run_combinations()

		self.generate_plots(outputs)