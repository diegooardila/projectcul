from fastapi import FastAPI
from routes.usuario_routes import router as usuario_router
from routes.periodo_acadmico_routes import router as periodo_academico_router
from routes.inscripcion_routes import router as inscripcion_router
from fastapi.middleware.cors import CORSMiddleware
from routes.facultad_routes import router as facultad_router
from routes.estudiante_routes import router as estudiante_router

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



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)