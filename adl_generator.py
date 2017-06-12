import jinja2

def generate(adl, fileName, list_name):
	
	with open(fileName, 'r') as t:
		template = jinja2.Template(t.read())
	
	address_list = template.render(build_time=build_time, comments=comments, list_name=list_name, adl=adl)
	outputFileName = list_name+".rsc"

	with open(outputFileName, 'w') as outputFile:
		outputFile.write(address_list)
