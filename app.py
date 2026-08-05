import uvicorn
from fastapi import FastAPI
from langserve import add_routes
import os

# IMPORTANT:
# Import your RAG runnable/chain here.
# Change "rag" to the Python filename that contains your chain.
# Example: if rag.py contains `rag_chain = ...`, keep this line:
from rag import rag_chain

app = FastAPI(
    title="RAG Agent API",
    version="1.0",
    description="LangServe API for the RAG application"
)

# Simple health route for Render
@app.get("/")
def home():
    return {
        "status": "running",
        "message": "RAG Agent API is running",
        "playground": "/agent/playground/"
    }

# Expose the LangChain/LangGraph runnable through LangServe
add_routes(
    app,
    rag_chain,
    path="/agent",
    playground_type="default"
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        reload=False
    )
