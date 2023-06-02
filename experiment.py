import os

import combinations
import plot
from datetime import datetime

class Experiment:

	def __init__(self, name, description, inp, antecedents, consequents, tnorm, implication):
		self.name = name
		self.description = description
		self.inp = inp
		self.antecedents = antecedents
		self.consequents = consequents
		self.tnorm = tnorm
		self.implication = implication

	def make_dir(self):
		if not os.path.exists('./experiments/'+self.name):
			os.mkdir('./experiments/'+self.name)

	def generate_description(self):
		with open('./experiments/'+self.name+'/description.txt', 'w') as f:
			f.write("Name: {}\n".format(self.name))
			f.write("Description: {}\n".format(self.description))
			f.write("Created at: {}\n".format(datetime.now()))
		

	def run_combinations(self, detailed=False):
		outputs = [{
					'name': 'bks_conj',
					'function':combinations.bks_conj,
					'detailed': False,
					'output': []
				},{
					'name': 'bks_imp',
					'function':combinations.bks_imp,
					'detailed': False,
					'output': []
				},{
					'name': 'cri_conj',
					'function':combinations.cri_conj,
					'detailed': False,
					'output': []
				},{
					'name': 'cri_imp',
					'function':combinations.cri_imp,
					'detailed': False,
					'output': []
				}]

		if detailed:
			outputs+=[{
						'name': 'bks_conj_detailed_A_less_Ai',
						'plot_title': r"$A' \leq A_1$",
						'function':combinations.bks_conj_detailed_A_less_Ai,
						'detailed': True,
						'related_name': 'bks_conj',
						'related_output': [],
						'output': []
					},{
						'name': 'bks_conj_detailed_A_greater_Ai',
						'plot_title': r"$A'>A_1$",
						'function':combinations.bks_conj_detailed_A_greater_Ai,
						'detailed': True,
						'related_name': 'bks_conj',
						'related_output': [],
						'output': []
					},{
					# },{
					# 	'name': 'bks_conj_detailed_A_less_Bi',
					# 	'plot_title': r"$A' \leq B_1(y)$",
					# 	'function':combinations.bks_conj_detailed_A_less_Bi,
					# 	'detailed': True,
					# 	'related_name': 'bks_conj',
					# 	'related_output': [],
					# 	'output': []
					# },{
					# 	'name': 'bks_conj_detailed_A_greater_Bi',
					# 	'plot_title': r"$A'>B_1(y)$",
					# 	'function':combinations.bks_conj_detailed_A_greater_Bi,
					# 	'detailed': True,
					# 	'related_name': 'bks_conj',
					# 	'related_output': [],
					# 	'output': []
					# },{
					# 	'name': 'cri_imp_detailed_A_less_Ai',
					# 	'plot_title': r"$A' \leq A_1$",
					# 	'function':combinations.cri_imp_detailed_A_less_Ai,
					# 	'detailed': True,
					# 	'related_name': 'cri_imp',
					# 	'related_output': [],
					# 	'output': []
					# },{
					# 	'name': 'cri_imp_detailed_A_greater_Ai',
					# 	'plot_title': r"$A'>A_1$",
					# 	'function':combinations.cri_imp_detailed_A_greater_Ai,
					# 	'detailed': True,
					# 	'related_name': 'cri_imp',
					# 	'related_output': [],
					# 	'output': []
					# },{
						'name': 'cri_imp_detailed_Ai_less_Bi',
						'plot_title': r"$A_i \leq B_1(y)$",
						'function':combinations.cri_imp_detailed_Ai_less_Bi,
						'detailed': True,
						'related_name': 'cri_imp',
						'related_output': [],
						'output': []
					},{
						'name': 'cri_imp_detailed_Ai_greater_Bi',
						'plot_title': r"$A_i>B_1(y)$",
						'function':combinations.cri_imp_detailed_Ai_greater_Bi,
						'detailed': True,
						'related_name': 'cri_imp',
						'related_output': [],
						'output': []
					}]

		for idx,comb in enumerate(outputs):	
			print("Calculating inference {} of {}".format(idx+1, len(outputs)))		
			comb['output'] = comb['function'](self.inp, self.antecedents, self.consequents, self.tnorm, self.implication)	

		# assign related output to detailed inferences (need to refactor this asap)
		if detailed:
			for comb1 in outputs:
				if comb1['detailed']:
					related_name = comb1['related_name']
					for comb2 in outputs:
						if comb2['name'] == related_name:
							comb1['related_output'] = comb2['output']
							break

		return outputs


	def run_combinations_beta(self):
		print("Runing combinations with beta")
		outputs =[{					
					'name': 'bks_conj_beta',
					'function':combinations.bks_conj_detailed_beta,
					'related_function':combinations.bks_conj,
					'output': [],
					'beta': None,
					'output_beta': []
				},{
					'name': 'cri_imp_beta',
					'function':combinations.cri_imp_detailed_beta,
					'related_function':combinations.cri_imp,
					'output': [],
					'beta': None,
					'output_beta': []
				}]

		for idx,comb in enumerate(outputs):
			print("Calculating inference {} of {} (beta)".format(idx+1, len(outputs)))

			comb['output_beta'], comb['beta'] = comb['function'](self.inp, self.antecedents, self.consequents, self.tnorm, self.implication)

			comb['output'] = comb['related_function'](self.inp, self.antecedents, self.consequents, self.tnorm, self.implication)

		return outputs


	def run_combinations_inputs(self):
		print("Runing combinations with inputs detailed")
		outputs = [{					
					'name': 'bks_conj_inputs',
					'function':combinations.bks_conj_detailed_inputs,					
					'output': [],
					'detailed_inp': [],
					'detailed_ant': []
				},{
					'name': 'cri_imp_inputs',
					'function':combinations.cri_imp_detailed_inputs,					
					'output': [],
					'detailed_inp': [],
					'detailed_ant': []
				},{
					'name': 'cri_conj_inputs',
					'function':combinations.cri_conj_detailed_inputs,					
					'output': [],
					'detailed_inp': [],
					'detailed_ant': []
				},{
					'name': 'bks_imp_inputs',
					'function':combinations.bks_imp_detailed_inputs,					
					'output': [],
					'detailed_inp': [],
					'detailed_ant': []
				}]

		for idx,comb in enumerate(outputs):
			print("Calculating inference {} of {} (inputs)".format(idx+1, len(outputs)))

			comb['output'], comb['detailed_inp'], comb['detailed_ant'] = comb['function'](self.inp, self.antecedents, self.consequents, self.tnorm, self.implication)			

		return outputs


	def generate_plots(self, outputs, detailed=False):

		input_filename_preffix = "./experiments/"+self.name+"/"+self.name
		plot.plot_inputs(self.inp, self.antecedents, "Inputs", filename_preffix=input_filename_preffix)

		for comb in outputs:
			filename_preffix = "./experiments/"+self.name+"/"+self.name+"_"+comb['name']

			if comb['detailed']:
				plot.plot_detailed(comb['related_output'], comb['output'], self.consequents, comb['plot_title'], filename_preffix=filename_preffix)
			else:
				plot.plot_outputs(comb['output'], self.consequents, "Outputs", filename_preffix=filename_preffix)


	def generate_plots_beta(self, outputs):
		for comb in outputs:
			filename_preffix = "./experiments/"+self.name+"/"+self.name+"_"+comb['name']

			# TODO: refactor plot title to a more meaningful name
			plot.plot_detailed_beta(comb['output'], comb['output_beta'], comb['beta'], self.consequents, "Beta Output", filename_preffix=filename_preffix)


	def generate_plots_inputs(self, outputs):
		for comb in outputs:
			filename_preffix = "./experiments/"+self.name+"/"+self.name+"_"+comb['name']
			
			plot.plot_detailed_inputs(comb['output'], comb['detailed_inp'], comb['detailed_ant'], self.consequents, "Detailed Inputs", filename_preffix=filename_preffix)


	def run_full_experiment(self, detailed=False, beta=False, inputs=False):
		self.make_dir()

		self.generate_description()

		outputs = self.run_combinations(detailed)

		self.generate_plots(outputs, detailed)

		if beta:
			outputs = self.run_combinations_beta()

			self.generate_plots_beta(outputs)

		if inputs:
			outputs = self.run_combinations_inputs()

			self.generate_plots_inputs(outputs)