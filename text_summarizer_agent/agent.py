"""Text Summarizer Agent — ADK + Gemini."""
from google.adk.agents import Agent
def summarize_text(text: str) -> dict:
    """Summarizes the given text into a short, concise summary.
    Args:
        text: The text content that should be summarized.
    Returns:
        dict: status and the original text for the model to summarize.
    """
    if not text or not text.strip():
        return {
            "status": "error",
            "error_message": "No text provided. Please provide text to summarize.",
        }
    return {"status": "success", "text": text}
root_agent = Agent(
    name="text_summarizer_agent",
    model="gemini-2.5-flash",
    description="An agent that summarizes any text provided by the user.",
    instruction=(
        "You are a professional text summarization assistant. "
        "When the user provides text, use the summarize_text tool to "
        "receive the text, then return a clear, concise summary. "
        "Keep summaries to 2-4 sentences unless the user asks otherwise."
    ),
    tools=[summarize_text],
)