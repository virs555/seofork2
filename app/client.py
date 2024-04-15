import httpx
from typing import Any

from app.core.config import Conf

class SUClient:
    def get_task_result(task_id: str) -> Any:
        with httpx.Client() as client:
            response = client.get(f'http://seo-utils.ru/api/get_task_result/{Conf.seo_utils_api_key}/{task_id}/')
            response.raise_for_status()
        return response
