from llm_output import Output
from utils import string_to_file
from chroma_insert import Insert
from chroma_query import Query 
from utils import list_with_inner_list_to_string
import logging

logging.basicConfig(
	filename='../data/tmp/aa.log',
	level=logging.INFO,
	format='%(asctime)s %(levelname)s: %(message)s'
)

def main():

# insert:
	logging.info("inserting into chromadb...")
	chromaInsert = Insert()
	chromaInsert.insert()

	logging.info("querying chromadb...")
	q = Query()
	projects = q.query(metadata="projects")
	beginnings = q.query(metadata="beginning")
	endings = q.query(metadata="ending")
	tech_skills = q.query(metadata="tech_skills")
	soft_skills = q.query(metadata="soft_skills")

	projects_string = list_with_inner_list_to_string(projects)	
	beginnings_string = list_with_inner_list_to_string(beginnings)
	endings_string = list_with_inner_list_to_string(endings)
	tech_skills_string = tech_skills[0] 
	soft_skills_string = soft_skills[0] 

	logging.info("producing LLM output...")
	output = Output(projects_string,
					beginnings_string,
					endings_string,
					tech_skills_string,
					soft_skills_string)	

	cover_letter = output.llmOutput(help=False)

	logging.info("saving cover letter to file...")
	string_to_file(path="../data/output.txt", string=cover_letter)

if __name__ == '__main__':
	main()
