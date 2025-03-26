from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# Montar la carpeta public como archivos estáticos
app.mount("/public", StaticFiles(directory="public"), name="public")

# Configure Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

PROJECTS = [
    {
        "id": 1,
        "title": "(GLI-SPP) Gestión de Legajos de Internos del Servicio Penitenciario Provincial",
        "description": "En este proyecto, lideré el desarrollo del sistema de gestión de legajos de internos para el Servicio Penitenciario     Provincial de Corrientes. Mi responsabilidad principal fue la construcción del backend, lo que incluyó el diseño de los endpoints, la implementación de diversas funciones y la creación de una nueva base de datos relacional para almacenar toda la información de los internos de las unidades penitenciarias de la provincia. Durante el proceso, me aseguré de normalizar las tablas y organizar la información de manera eficiente. Además, desempeñé el rol de Project Manager, gestionando las actividades del equipo, realizando el análisis de requerimientos y manteniendo comunicación constante con los clientes, incluidos los agentes penitenciarios y directores a cargo del proyecto.",
        "technologies": ["Python", "FastAPI", "SQLAlchemy", "Pydantic", "MySQL", "Trello"],
        "image": "/static/images/proyecto_penitenciaria.webp",  # Ruta de la imagen
        "link": "privado"
    },
    {
        "id": 2,
        "title": "Data Analysis Project",
        "description": "Desarrollo de Aplicación Web para Estudiantes de Fonoaudiología - Diseñé e implementé una plataforma web con autenticación de usuarios, permitiendo a los fonoaudiólogos gestionar perfiles de pacientes, registrar informes clínicos y acceder a herramientas interactivas de enseñanza para niños de 4 a 7 años. La aplicación incorpora juegos educativos diseñados para reforzar habilidades lingüísticas y comunicativas, brindando una experiencia atractiva y funcional. Además, lideré la gestión del proyecto, recopilando requisitos mediante entrevistas con especialistas y adaptando la aplicación a su metodología de trabajo. Coordiné el desarrollo para garantizar una interfaz intuitiva y una funcionalidad alineada con los objetivos terapéuticos, optimizando la experiencia del usuario y la eficacia del proceso de enseñanza.",
        "technologies": ["Node.js", "Tailwind CSS", "JavaScript", "MongoDB Atlas"],
        "image": "/static/images/FonApp_Login.webp",  # Ruta de la imagen
        "link": "https://github.com/falkievich/FonApp"
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
            "Python", "FastAPI", "Jinja2", 
            "MySQL", "Docker", "Git" , "Trello", 
            "Vercel", "Microsoft Access", "Numpy", 
            "MongoDB", "Project Manager"
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

# Para compatibilidad con Vercel
def create_app():
    return app

# Punto de entrada para Vercel
app_vercel = create_app()