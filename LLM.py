from openai import OpenAI
import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
from prompts import prompts

class SearchingTerms(BaseModel):
        Terms: List[str]

def generateST(prompt, prompting_tech):
    load_dotenv()
    
    
    _prompt = ''
    if "CoT" in prompting_tech: _prompt += prompts.CoT
    if "Few_Shot" in prompting_tech: _prompt += prompts.Few_shot
    _prompt += prompt
    client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    responses=client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """Please recommend 3 search terms for finding relevant arXiv papers for the following topic or situation.
                Format: Terms: List[str]
                """
            },
            {
                "role":"user",
                "content": _prompt
            }
        ],
        response_format=SearchingTerms
    )
    return(responses.choices[0].message.parsed)


class SummarizePaper(BaseModel):
        description: str
        Relevance: float

def SummarizePP(prompt, paper, prompting_tech):
    load_dotenv()
       
    _prompt = ''
    if "role_playing" in prompting_tech: _prompt += prompts.Role_Playing


    _prompt += "Paper Title: \n"
    _prompt += paper["Title"]
    _prompt += "Abstract of paper: \n"
    _prompt += paper["Abstract"]
    _prompt += "\n\nquestion: \n"
    _prompt += prompt

    client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    responses=client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """Summarize the following paper, and explain its relevance to the question in about 50 words. Also, evaluate the relevance to the question on a scale of 0–100%.
                Format: 
                description: str
                Relevance: float
                """
            },
            {
                "role":"user",
                "content": _prompt
            }
        ],
        response_format=SummarizePaper
    )
    return(responses.choices[0].message.parsed)