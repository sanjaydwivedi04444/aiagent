import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI(title="My AI Agent")

client = OpenAI(
    api_key="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"
)


class AgentRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"status": "AI agent is running"}


@app.post("/agent")
def run_agent(request: AgentRequest):
    try:
        response = client.responses.create(
            model="gpt-4o",
            input=request.message
        )

        return {
            "answer": response.output_text
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="The agent could not process the request."
        )