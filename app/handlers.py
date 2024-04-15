from datetime import datetime

from app.models import Position, DeviceEnum, SearchEngineEnum
from app.client import SUClient


def parse_yandex_serp_response(task_id, domain: str) -> list[Position]:
    json_pos = SUClient.get_task_result(task_id).json()
    positions = []
    date = datetime.strptime(json_pos['result']['created_at'], '%Y-%m-%d %H:%M:%S')
    #TODO добавить проверку на наличие данных в json
    for query, query_data in json_pos['result']['data'].items():
        for pos in query_data['results']:
            if domain in pos['url']:
                #TODO Улучшить сопоставление домена в url
                positions.append(Position(key=query,
                             pos=pos['pos'],
                             url=pos['url'],
                             date=date,
                             region=213,
                             device=DeviceEnum.pc,
                             search_engine=SearchEngineEnum.yandex))
                #TODO Разобраться как лучше передавать дату, регион, девайс и поиск, которые для всех Position одинаковые в рамках 1-го съема
    return positions
    #TODO Разобраться как сериализовать dataclass в json
