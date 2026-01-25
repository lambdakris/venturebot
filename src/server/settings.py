import os
import dspy
from dotenv import load_dotenv

def configure_dspy():
    # Load environment variables
    load_dotenv()

    # Obtain openai api key
    openai_api_key = os.environ["OPENAI_API_KEY"]
    
    # Configure OpenAI gpt-5-mini as the LM
    lm = dspy.LM(model='openai/gpt-5-mini', api_key=openai_api_key)
    
    # Configure DSPy
    dspy.settings.configure(lm=lm)
