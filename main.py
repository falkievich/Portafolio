from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Sample data (you'll replace with your actual information)
PROJECTS = [
    {
        "id": 1,
        "title": "Portfolio Website",
        "description": "A personal portfolio website built with FastAPI and Jinja2",
        "technologies": ["Python", "FastAPI", "Jinja2"],
        "link": "#"
    },
    {
        "id": 2,
        "title": "Data Analysis Project",
        "description": "A comprehensive data analysis project using pandas and matplotlib",
        "technologies": ["Python", "Pandas", "Matplotlib"],
        "link": "#"
    }
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "name": "Thiago Falkievich",
        "title": "Web Developer & Designer"
    })

@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    return templates.TemplateResponse("projects.html", {
        "request": request,
        "projects": PROJECTS
    })

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {
        "request": request,
        "skills": [
            "Python", "FastAPI", "JavaScript", 
            "React", "Docker", "Git"
        ]
    })

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {
        "request": request
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)