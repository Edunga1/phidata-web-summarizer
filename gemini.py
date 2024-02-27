from os import getenv

import vertexai
from phi.assistant import Assistant
from phi.llm.gemini import Gemini

# To check Google Cloud free quota. filter by name: `Generate content requests per minute per project per base model per minute per region per base_model` or service: `Vertex AI`
# Script reference: https://github.com/phidatahq/phidata/tree/main/cookbook/gemini

# *********** Initialize VertexAI ***********
vertexai.init(project=getenv("PROJECT_ID"), location=getenv("LOCATION"))

assistant = Assistant(
    llm=Gemini(model="gemini-1.0-pro-vision"),
)
assistant.print_response("이름이 뭔가요? 당신은 어떤 언어 모델인가요?", markdown=True)
