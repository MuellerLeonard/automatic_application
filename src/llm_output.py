# text file for job desc
# insertion of projects
# Query

from llm import LLM
from utils import read_text_from_file 
import json

# get projects

class Output():
	
	def __init__(self, projects_string, beginnings_string, endings_string, tech_skills_string, soft_skills_string):
		"""Load all prompt strings"""
	
		# Job Description
		self.job_description = read_text_from_file("../data/job_description.txt")	
		# Other Input
		self.projects_string = projects_string
		self.beginnings_string = beginnings_string
		self.endings_string = endings_string
		self.tech_skills_string = tech_skills_string
		self.soft_skills_string = soft_skills_string
			
		with open("../data/config.json") as file:
			config = json.load(file)
			self.query = config["queries"]["honest_query"]
			self.model_name = config["llms"]["model_name"]
	
	def llmOutput(self, help=False):
		"""Give input to a Chatbot

		Args:
			help: Boolean to show additional logs

		Returns:
			cover_letter: output string of the llm
		"""
	
		llm = LLM()
	
		message = [
            {
                "role": "system",
                "content": self.query 
            },
            {
                "role": "user",
                "content": f"1 Stellenbeschreibung: {self.job_description} \n"
            },
            {
                "role": "user",
                "content": f"2 Projektliste: {self.projects_string} \n" 
            },
			{
                "role": "user",
                "content": f"3 Einleitungen: {self.beginnings_string} \n" 
            },
			{
                "role": "user",
                "content": f"4 Schlusssaetze: {self.endings_string} \n" 
            },
			{
                "role": "user",
                "content": f"5 Tech Skills: {self.tech_skills_string} \n" 
            },
			{
                "role": "user",
                "content": f"6 Soft Skills: {self.soft_skills_string} \n" 
				},

		]
	    
		if help:
			print(message[0]['content'])
			print(message[1]['content'])
			print(message[2]['content'])
			print(message[3]['content'])
			print(message[4]['content'])
			print(message[5]['content'])
			print(message[6]['content'])
	
		cover_letter = llm.ask(model=self.model_name, message=message, help=help)	

	
		return cover_letter 
