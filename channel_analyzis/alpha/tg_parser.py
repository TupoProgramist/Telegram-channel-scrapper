from telethon import TelegramClient
import json
import argparse
import asyncio
import datetime
from dotenv import load_dotenv
from typing import Self
import os

load_dotenv()


class TgChannel:
    def __init__(self, name: str, link: str, id: int) -> Self:
        self.name = name
        self.link = link
        self.id = id
        self.messages: list[TgMessage] = []

    async def from_link(client: TelegramClient, link: str) -> Self:
        channel_entity = await client.get_entity(link)
        name = channel_entity.username
        id = channel_entity.id
        return TgChannel(name, link, id)

    async def retrive_messages(self, client: TelegramClient, msg_number=10):
        channel = await client.get_entity(self.link)
        msgs_entitys = await client.get_messages(channel, limit=msg_number)
        msgs = [
            TgMessage(msg_entity.message, msg_entity.date, msg_entity.id, self)
            for msg_entity in msgs_entitys
        ]
        self.messages.extend(msgs)

    def to_json(self) -> dict:
        return {
            "name": self.name,
            "link": self.link,
            "messages": [msg.to_json() for msg in self.messages],
        }


class TgMessage:
    def __init__(
        self, text: str, date: datetime, id: int, source_channel: TgChannel = None
    ) -> None:
        self.text = text
        self.date = date
        self.id = id
        self.channel = source_channel

    def to_json(self) -> dict:
        return {
            "content": self.text,
            "date": self.date.strftime("%d.%m.%Y %H:%M:%S"),
            "id": self.id,
            "channel_name": self.channel.name,
        }


parser = argparse.ArgumentParser()
parser.add_argument("--channel_link")
parser.add_argument("--output", required=True)
parser.add_argument("--messages_number", default=10)
args = parser.parse_args()

TELEGRAM_API_ID = os.environ.get("TELEGRAM_API_ID")
TELEGRAM_API_HASH = os.environ.get("TELEGRAM_API_HASH")
CHANNEL_LINK = args.channel_link
OUTPUT_PATH = args.output
MESSAGES_NUMBER = args.messages_number
header = ["datetime", "message"]


async def retrive_messages(client, channel_id, msg_number):
    channel = await client.get_entity(channel_id)
    return await client.get_messages(channel, limit=msg_number)


def reset_json(path):
    with open(path, "w", encoding="UTF8") as f:
        json.dump({"channel_name": "", "messages": []}, f)


def append_json(messages, path):
    with open(path, "r", encoding="UTF8", newline="") as f:
        json_object = json.load(f)

    with open(path, "w", encoding="UTF8", newline="") as f:
        json_object["messages"].extend(messages)
        json.dump(json_object, f, ensure_ascii=False)


async def main():
    if CHANNEL_LINK == None:
        raise Exception("Channel link is not specified!")
    async with TelegramClient(
        "parse_blocks", TELEGRAM_API_ID, TELEGRAM_API_HASH
    ) as client:
        channel = await TgChannel.from_link(client, CHANNEL_LINK)
        await channel.retrive_messages(client, msg_number=MESSAGES_NUMBER)
        messages = [msg.to_json() for msg in channel.messages]
        append_json(messages, OUTPUT_PATH)

    # reset_json(OUTPUT_PATH)


if __name__ == "__main__":
    asyncio.run(main())
