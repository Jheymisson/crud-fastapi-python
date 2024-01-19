from typing import Optional, Any

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header

from fastapi.responses import JSONResponse
from fastapi import Depends
from time import sleep

from models import Curso

def fake_db():
    try:
        print('Abrindo conexao com o banco de dados')
        sleep(1)
    finally:
        print('Fechando conexao com o banco de dados')
        sleep(1)


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
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(
    title='Id do curso',
    description='Deve ser entre 1 e 3', gt=0, le=3),
    db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Cursos nao encontrado')

@app.post('/cursos')
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    if curso.id is None:
        curso.id = max(cursos.keys(), default=0) + 1

    if curso.id not in cursos:
        cursos[curso.id] = curso.model_dump()
        return cursos[curso.id]

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        curso.id = curso_id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com id {curso_id}')

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        #return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com id {curso_id}')

@app.get('/calculadora')
async def calculadora(a: int = Query(...),
                      b: int = Query(...),
                      x: str = Header(default=None),
                      c: Optional[int] = None):
    soma: int = a + b
    if c:
        soma += c
    print(f'X: {x}')

    return {'Resultado': soma}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
