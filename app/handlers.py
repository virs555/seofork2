from datetime import datetime

from app.models import Position, DeviceEnum, SearchEngineEnum
from app.client import SUClient

def convert_position(position, query, date):
    return Position(key=query,
                    position=position.pos,
                    url=position.url,
                    date=date,
                    region=213,
                    device=DeviceEnum.PC,
                    search_engine=SearchEngineEnum.YANDEX)

def convert_query(query, query_data, date, domain):
    filtered_positions = [position for position in query_data.results if domain in position.url]
    return [convert_position(position, query, date) for position in filtered_positions]

def parse_yandex_serp_response(task_id, domain: str) -> list[Position]:
    client = SUClient()
    response = client.get_task_result(task_id)
    positions = []
    date = response.result.created_at
    for query, query_data in response.result.data.items():
        positions += convert_query(query, query_data, date, domain)
    return positions
    
    #TODO добавить проверку на наличие данных в json
    #TODO Улучшить сопоставление домена в url
    #TODO Разобраться как лучше передавать дату, регион, девайс и поиск, которые для всех Position одинаковые в рамках 1-го съема
    #TODO Разобраться как сериализовать dataclass в json
