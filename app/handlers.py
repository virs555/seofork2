from models import Position

def parse_yandex_serp_response(json, domain: str) -> list[Position]:
    ...