# Text Summarizer Agent — ADK + Gemini on Cloud Run
A single AI agent built with [Google ADK](https://google.github.io/adk-docs/) that summarizes text using **Gemini 2.0 Flash**, deployed to **Google Cloud Run**.
## Project Structure
text_summarizer_agent/ ├── init.py # Package init ├── agent.py # Agent + tool definition main.py # FastAPI entry point requirements.txt # Python dependencies Dockerfile # Container image for Cloud Run

## Deploy
```bash
gcloud run deploy text-summarizer-agent \
  --source=. --region=us-central1 --project=silver-skylab \
  --set-env-vars="GOOGLE_GENAI_USE_VERTEXAI=TRUE,GOOGLE_CLOUD_PROJECT=silver-skylab,GOOGLE_CLOUD_LOCATION=us-central1" \
  --allow-unauthenticated --memory=1Gi
