import sys

from phi.assistant.assistant import Assistant
from phi.llm.ollama.chat import Ollama

from toolkit.web import WebVisitor


url = sys.argv[1]
message = f"""
Summarize the content of the site.

Please divide it into 3 sections with horizontal lines.

The first section should summarize the main content in 10 lines or less.
In the second section, include up to three of the most reactive comments in their entirety.
The last section should summarize all comments. You don't need to include the full text.
"""

# local LLM doesn't uses tools
assistant = Assistant(
    tools=[WebVisitor()],
    llm=Ollama(
        model='gemma:7b',
        host='localhost:11434',
        options={'temperature': 0},
    ),
    description='Summarize the content of the site. the content contains HTML tags.',
)
assistant.print_response(message, markdown=True)
