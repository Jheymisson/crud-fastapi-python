from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from models import Curso

app = FastAPI()

cursos = {
    1: {
        "id": 1,
        "titulo": "Introducao ao Java",
        "aulas": 149,
        "horas": 66
    },
    2: {
        "id": 2,
        "titulo": "Introducao ao Django",
        "aulas": 55,
        "horas": 39
    },
    3: {
        "id": 3,
        "titulo": "Machine Learning",
        "aulas": 30,
        "horas": 45
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Cursos nao encontrado')


@app.post('/cursos')
async def post_curso(curso: Curso):
    if curso.id is None:
        curso.id = max(cursos.keys(), default=0) + 1

    if curso.id not in cursos:
        cursos[curso.id] = curso.model_dump()
        return cursos[curso.id]


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        curso.id = curso_id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com id {curso_id}')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
