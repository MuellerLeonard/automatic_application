# Automatic Cover Letter creation

- Does what the name says
- inputs are required for it to be more precise

## Inside /data

- **job_description.txt**:
  - copy and paste the job description
  - keep it as short as possible to reduce token count (cost)
- **documents.json**:
  - projects: add projects you worked on
  - ending: add CV conclusive sentences as template for the LLM
  - beginning: add CV introductions as template for the LLM
    - same as ending to keep it personal
  - tech_skills: list your technical skills here
  - soft_skills: list your strengths here
- **config.json**:
  - api_key: Add your **API KEY** for the LLM you want to use
    - Any LLM API and model that is compatible with OpenAI works
  - model_name: Add the name of the model you want to use
    - careful token usage is high
  - "honest_query": Query for the LLM
