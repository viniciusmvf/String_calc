import re
def add(string):
	string = _any_delimiter(string)
	if string:
		return _add_numbers_in_string(string)
	else:
		return 0 

def _any_delimiter(string):
	string = _custom_delimiter(string)
	string = string.replace('\n',',')
	return string

def _custom_delimiter(string):
	if string.startswith('//'):
		delimiter_spec, string = string.split('\n',1)
		delimiter = delimiter_spec[2:]
		delimiter = string[2]
		string = string.replace(delimiter, ',')
	return string

def _add_numbers_in_string(string):
	numbers =  map(int, string.split(','))
	_validate_numbers(numbers)
	return sum(numbers)

def _validate_numbers(numbers):
	if any(number < 0 for number in numbers):
		raise ValueError



