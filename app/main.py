from routes.usuario_routes import router as usuario_router
from routes.periodo_acadmico_routes import router as periodo_academico_router
from routes.inscripcion_routes import router as inscripcion_router
from routes.facultad_routes import router as facultad_router
from routes.estudiante_routes import router as estudiante_router
from routes.estado_routes import router as estado_router
from routes.docente_routes import router as docente_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    "ep-raspy-block-aio4kl2c-pooler.c-4.us-east-1.aws.neon.tech",
    "http://localhost"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuario_router)
app.include_router(periodo_academico_router)
app.include_router(inscripcion_router)
app.include_router(facultad_router)
app.include_router(estudiante_router)
app.include_router(estado_router)
app.include_router(docente_router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)