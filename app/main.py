from fastapi import FastAPI
from app.handlers import parse_yandex_serp_response

app = FastAPI()


@app.get("/yandex")
def get_yandex_results():
    return parse_yandex_serp_response('41167582', '1000.menu')