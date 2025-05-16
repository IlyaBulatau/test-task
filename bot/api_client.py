import logging
from typing import NoReturn

import aiohttp
from aiohttp import ClientTimeout

from api_exceptions import APIException
from schemes import TaskScheme
from settings import API_KEY, API_URL


logger = logging.getLogger(__name__)


class APIClient:
    def __init__(
        self, base_url: str = API_URL, api_key: str = API_KEY, timeout: int = 10
    ):
        self._base_url = base_url.strip("/")
        self._api_key = api_key
        self._headers = {"AUTHENTICATION": api_key}
        self._timeount: int = timeout

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def api_key(self) -> str:
        return self._api_key

    async def get_tasks_by_user_id(self, user_id: str) -> list[TaskScheme] | NoReturn:
        url = "/api/v1/tasks"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    self.base_url + url,
                    params={"telegram_user_id": user_id},
                    timeout=ClientTimeout(total=self._timeount),
                    headers=self._headers,
                ) as response:
                    if response.status == 200:
                        result: list[TaskScheme] = await response.json()

                        return result

                    raise APIException()
        except aiohttp.ClientConnectorError as exc:
            logger.error(exc)
            raise APIException() from exc

    async def done_task(self, task_id: str) -> TaskScheme | NoReturn | None:
        url = f"/api/v1/tasks/{task_id}/"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.patch(
                    self.base_url + url,
                    timeout=ClientTimeout(total=self._timeount),
                    headers=self._headers,
                    json={"status": "done"},
                ) as response:
                    if response.status == 200:
                        result: TaskScheme = await response.json()
                        return result

                    elif response.status == 404:
                        return None

                    raise APIException()

        except aiohttp.ClientConnectionError as exc:
            logger.error(exc)
            raise APIException() from exc
