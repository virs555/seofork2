import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

@dataclass
class Conf:
    seo_utils_api_key = os.getenv('SEO_UTILS_API_KEY')
    seo_utils_url = 'http://seo-utils.ru'