import discord
from typing import Optional, Dict, Union
import json



TABLE_NAME_KEY = "TABLE"
DATA_NAME_KEY = "NAME"
DATA_KEY = "DATA"


class Connection:
    def __init__(
        self,
        channel: discord.TextChannel, 
        tables: Dict[str, Dict[str, Dict[str, Union[dict, discord.TextChannel]]]]
    ):
        self._channel: discord.TextChannel = channel
        self._tables: Dict[str, Dict[str, Dict[str, Union[dict, discord.TextChannel]]]] = tables

    async def set_table(self, table_name: str, table: Dict[str, Dict[str, dict]]):
        await self.del_table(table_name)
        self._tables[table_name] = {}

        for data_name, data in table.items():
            data_dict = {
                TABLE_NAME_KEY : table_name,
                DATA_NAME_KEY : data_name,
                DATA_KEY : data
            }

            message: discord.Message = await self._channel.send(
                json.dumps(data_dict, ensure_ascii=False)
            )

            self._tables[table_name][data_name] = {
                "data" : data,
                "message" : message
            }
        
    def get_table(self, table_name: str) -> Optional[Dict[str, dict]]:
        table = self._tables.get(table_name)
        if table is None:
            return None

        table_dict = {}
        for data_name, value in table.items():
            table_dict[data_name] = value["data"]

        return table_dict

    async def del_table(self, table_name: str):
        table = self._tables.get(table_name)
        if table is None:
            return

        for value in table.values():
            await value["message"].delete()

        del self._tables[table_name]


    async def set_data(self, table_name: str, data_name: str, data: dict):
        await self.del_data(table_name, data_name)            

        data_dict = {
            TABLE_NAME_KEY : table_name,
            DATA_NAME_KEY : data_name,
            DATA_KEY : data
        }
        message: discord.Message = await self._channel.send(
            json.dumps(data_dict, ensure_ascii=False)
        )

        if table_name not in self._tables.keys():
            self._tables[table_name] = {}

        self._tables[table_name][data_name] = {
            "data" : data,
            "message" : message
        }

    def get_data(self, table_name: str, data_name: str) -> Optional[dict]:
        table = self._tables.get(table_name)
        if table is None:
            return None

        value = table.get(data_name)
        if value is None:
            return None

        return value["data"]

    async def del_data(self, table_name: str, data_name: str):
        table = self._tables.get(table_name)
        if table is None:
            return

        value = table.get(data_name)
        if value is None:
            return

        await value["message"].delete()
        del self._tables[table_name][data_name]

            


async def connect(channel: discord.TextChannel) -> Connection:
    if (type(channel) is not discord.TextChannel):
        raise TypeError("Argument \"channel\" type is not discord.TextChannel")

    tables: Dict[str, Dict[str, Dict[str, Union[dict, discord.TextChannel]]]] = {}
    
    async for message in channel.history(limit=None):
        loaded_data: dict = json.loads(message.content)

        table_name: str = loaded_data.get(TABLE_NAME_KEY)
        data_name: str = loaded_data.get(DATA_NAME_KEY)
        data: dict = loaded_data.get(DATA_KEY)

        if table_name is None:
            continue
        if data_name is None:
            continue
        if data is None:
            continue

        if table_name not in tables:
            tables[table_name] = {}

        tables[table_name][data_name] = {
            "data" : data,
            "message" : message
        }

    return Connection(channel, tables)