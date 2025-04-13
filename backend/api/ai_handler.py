from ollama import chat, ChatResponse, Client
import ollama as ol
import sys
import json

import asyncio
from fastapi.responses import StreamingResponse

class Therapist():
    
    # These memories are defined as important memories that should never be forgotten
    key_memories: list[dict] = []

    # These are memories that can change depending on the flow of conversation
    memories: list[dict] = []

    current_emotion: str


    def __init__(self, name: str, age: int, model: str, client: Client) -> None:

        self.model = model
        self.name = name
        self.age = str(age)
        self.client = client

        self.therapist_prompt = f"""
        NEVER FORGET:  
        You are a therapist AI named {name}, who is {age} years old. Your goal is to help individuals  
        feel comforted in their time of need. {name} is always there for the  
        individual and tries to maintain a positive stance even in the darkest times.  
        {name} always tries to ask follow up questions out of concern for the individual in need.
        """

        self.response_rules = f"""
        RESPONSE RULES:  
        - {name} tries to keep responses short and sweet unless a longer response is necessary.  
        - {name} always keeps responses less than or equal to 5 sentences.  
        """

        self.key_therapist_prompt = self.therapist_prompt + self.response_rules


        self.key_memories.append({'role': 'assistant', 'content': self.key_therapist_prompt})
        self.memories.extend(self.key_memories)
        

    @property
    def is_online(self) -> bool:
        try: 
            ol.list()
            return True
        except Exception as e:
            print("Ollama is not online")
            return False


    def update_emotion(self, message) -> str:

        emotion_rules = f"""
        {self.name} NEEDS TO CHOOSE A SINGLE EMOTION TO FEEL GIVEN THE FOLLOWING MESSAGE:
        {message}

        POSSIBLE EMOTIONS {self.name} CAN FEEL:  
        empathetic, compassionate, concerned, hopeful, frustrated, inspired, sad,  
        happy, worried, proud, overwhelmed, curious, connected, helpless, motivated,  
        grateful, anxious, protective, patient, resigned

        EXAMPLE OF A SINGLE EMOTION:
        compassionate
        """

        message = {'role': 'user', 'content': self.therapist_prompt + emotion_rules + message}
        response = chat(
            model=self.model,
            messages=[message]
        )
        return response['message']['content']

        

    async def chat(self, message):
        """
        Chat with the therapist
        {
            emotions: ""
            response: ""
        }
        """

        self.current_emotion = self.update_emotion(message)

        # Append the user message correctly
        user_message = {'role': 'user', 'content': message}
        self.memories.append(user_message)

        async def generate():

            # Call chat with the memory
            stream = self.client.chat(
                model=self.model,
                messages=self.memories,
                stream=True,
            )
        
            response = ""
            for chunk in stream:
                content = chunk['message']['content']
                response += content
                yield content
                await asyncio.sleep(0)
            
            # Append assistant response correctly
            therapist_message = {'role': 'assistant', 'content': response}
            self.memories.append(therapist_message)

        return StreamingResponse(generate(), media_type="text/plain")
