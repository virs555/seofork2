import os
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class Conf:
    seo_utils_api_key: str | None
    seo_utils_url: str | None


def load():
    load_dotenv()
    return Conf(
        seo_utils_api_key=os.getenv("SEO_UTILS_API_KEY"),
        seo_utils_url=os.getenv("SEO_UTILS_URL"),
    )


config = load()
