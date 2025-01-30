import os
from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"] = "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"


api_key = os.getenv("GROQ_API_KEY")


if not api_key:
    raise ValueError("GROQ_API_KEY is not set. Please set it in your environment.")

llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.3-70b-versatile")

if __name__ == "__main__":
    response = llm.invoke("Two most important ingredients in samosa are ")
    print(response.content)
