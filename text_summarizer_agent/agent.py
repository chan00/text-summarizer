"""
Text Summarizer Agent — Built with Google ADK + Gemini.

This agent accepts a block of text and returns a concise summary.
It exposes a single tool (`summarize_text`) that the LLM can invoke.
"""

from google.adk.agents import Agent


def summarize_text(text: str) -> dict:
    """Summarizes the given text into a short, concise summary.

    This function is used as a *tool* by the agent. The Gemini model
    will call this tool when it decides the user is asking for a
    summary. Because ADK tools are just Python functions, the model
    receives the docstring as the tool description and uses the
    function signature to understand the expected arguments.

    Args:
        text: The text content that should be summarized.

    Returns:
        dict: A dictionary with:
            - status (str): "success" or "error"
            - text (str): The original text echoed back
              so the model can produce a summary from it.
    """
    if not text or not text.strip():
        return {
            "status": "error",
            "error_message": "No text provided. Please provide text to summarize.",
        }

    # Return the text back to the model so it can produce a summary.
    # The heavy lifting (actual summarization) is done by Gemini
    # via the agent instruction.
    return {
        "status": "success",
        "text": text,
    }


# ── Root Agent Definition ────────────────────────────────────────
root_agent = Agent(
    name="text_summarizer_agent",
    model="gemini-2.0-flash",
    description="An agent that summarizes any text provided by the user.",
    instruction=(
        "You are a professional text summarization assistant. "
        "When the user provides text, use the `summarize_text` tool to "
        "receive the text, then return a clear, concise summary. "
        "Keep summaries to 2-4 sentences unless the user asks for more "
        "or less detail. Preserve the key facts and main ideas."
    ),
    tools=[summarize_text],
)
