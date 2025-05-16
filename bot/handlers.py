from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from api_client import APIClient
from api_exceptions import APIException
from normalization import prepare_mytasks_answer, prepare_done_anwser


router = Router()


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет")


@router.message(Command(commands=["mytasks"]))
async def command_mytasks_handler(message: Message) -> None:
    api_client = APIClient()

    try:
        tasks = await api_client.get_tasks_by_user_id(message.from_user.id)
    except APIException:
        await message.answer("Проблемы, пропробуйте позже...")
    else:
        if not tasks:
            await message.answer("У вас нет задач")
        else:
            await message.answer(prepare_mytasks_answer(tasks))


@router.message(Command(commands=["done"]))
async def command_done_handler(message: Message, command: CommandObject) -> None:
    api_client = APIClient()
    command_args: str = command.args.split()[0] if command.args else None

    if not command_args:
        await message.answer("Укажите номер задачи")

    try:
        task = await api_client.done_task(command_args)
    except APIException:
        await message.answer("Проблемы, пропробуйте позже...")
    else:
        if not task:
            await message.answer("Задача не найдена")
        else:
            await message.answer(prepare_done_anwser(task))
