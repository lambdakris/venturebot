import os
import dspy
from dotenv import load_dotenv

def configure_dspy():
    # Load environment variables
    load_dotenv()

    openai_base_url = os.environ["AZURE_OPENAI_BASE_URL"]
    openai_api_key = os.environ["AZURE_OPENAI_API_KEY"]

    lm = dspy.LM(
        model="openai/gpt-5-mini",
        api_base=openai_base_url,
        api_key=openai_api_key,
    )

    # Configure DSPy
    dspy.settings.configure(lm=lm)
