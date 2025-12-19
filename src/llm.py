import requests
import json

import time

from typing import List, Dict

from openai import OpenAI

class LLM():

    MAX_RETRIES = 2

    def __init__(self):
        self.nr_retries = 0

    def get_prediction(self, completion):
        try:
            choices = completion.choices
            if not isinstance(choices, list):
                raise ValueError(f"'choices' is not a list: {choices!r}")
            msg = choices[0].message
            if not hasattr(msg, 'content'):
                raise ValueError(f"'message' has no 'content': {msg!r}")
            return msg.content
        except Exception as e:
            print("ERROR extracting content:", e)
            return None

    def ask(self, model: str, message: List[Dict], help=False) -> str:
        with open("../data/config.json") as file:
            llms = json.load(file)["llms"]
        
        XAI_API_KEY = llms["api_key"]
        client = OpenAI(
            api_key=XAI_API_KEY,
            base_url="https://api.x.ai/v1",
        )

        completion = client.chat.completions.create(
            model=model,
            messages=message,
        )

        if help:
            if completion.usage:
                print(completion.usage.to_json())
       
        content = self.get_prediction(completion)

        return content
