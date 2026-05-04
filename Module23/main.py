from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

@app.post("/developer/")
def create_developer(developer: Developer):
    return {"message": "Developer creates", "developer": developer}

@app.post("/project/")
def create_project(project: Project):
    return {"message": "Project created", "project": project}

@app.get("/project/")
def get_projects():
    sample_project = Project(
        title="Test",
        description="This is a test project",
        language=["Python", "PHP"],
        lead_developer=Developer(name="Dren", experience=5)
    )
    return {"projects": [sample_project]}