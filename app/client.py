import httpx
import json
from app.models import APIResponse


class SUClient:
    def __init__(self):
        self.client = httpx.Client(base_url="http://seo-utils.ru/api/")

    # def get_task_result(self, task_id: str) -> APIResponse:
    #     response = self.client.get(f'get_task_result/{config.seo_utils_api_key}/{task_id}/')
    #     response.raise_for_status()
    def get_task_result(self, task_id: str):
        # Тестовые данные для разработки
        with open("app/data/fix_data_api_response.json", "r", encoding="utf-8") as file:
            response = json.load(file)
        return APIResponse(**response)  # .json()
