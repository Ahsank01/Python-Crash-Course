# Name: Ahsan Khan
# Date: 10/12/20
# Description: Write an import statement at the top of printing_module.py, and modify the file to use the imported functions.

import printing_functions as p 

unprinted_designs = ['phone case', 'laptop case', 'airpods case']
completed_models = []

p.printing_design(unprinted_designs, completed_models)
p.show_completed_models(completed_models)