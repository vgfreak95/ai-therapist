from autogen_ext.models.ollama import OllamaChatCompletionClient
from autogen_core.models import UserMessage
from pydantic import BaseModel

import asyncio


class StructuredOutput(BaseModel):
    first_name: str
    last_name: str


async def main():
    ollama_client = OllamaChatCompletionClient(
        model="llama3.1",
        # response_format=StructuredOutput,
    )
    result = await ollama_client.create(
        [UserMessage(content="Who was the first president of the US", source="user")]
    )
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
