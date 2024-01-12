from fastapi import FastAPI

app = FastAPI()

cursos = {
    1: {
        "titulo": "Introducao ao Java",
        "aulas": 149,
        "horas": 66
    },
    2: {
        "titulo": "Introducao ao Django",
        "aulas": 55,
        "horas": 39
    },
    3: {
        "titulo": "Machine Learning",
        "aulas": 30,
        "horas": 45
    }
}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
