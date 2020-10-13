# Name: Ahsan Khan
# Date: 10/12/20
# Description: Put the functions dor the example printing_module.py in a separate file called printing_functions.py.
#			   Write an import statement at the top of printing_module.py, and modify the file to use the imported functions.

def printing_design(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design.title()}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nThe following models have been printed")
	for model in completed_models:
		print(model.title())