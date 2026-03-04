import os
from dotenv import load_dotenv
import google.ai.generativelanguage as glm
from google.api_core.client_options import ClientOptions

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

client = glm.GenerativeServiceClient(
    client_options=ClientOptions(api_key=API_KEY)
)

models = client.list_models().models
for m in models:
    print(m.name)
