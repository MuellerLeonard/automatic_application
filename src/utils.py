from typing import List

def read_text_from_file(path):
	with open(path, "r", encoding="utf-8") as f:
		return f.read()

def list_with_inner_list_to_string(L: List[[str]]) -> str:
	string = ""
	
	for i in range(len(L[0])):
		string = string + f"{i}." + L[0][i] + "\n"	
		if(i == len(L[0]) -1):
			string = string + f"{i}." + L[0][i]
	return string

def string_to_file(path: str, string: str):
	with open(path, 'w') as file:
		file.write(string)	
