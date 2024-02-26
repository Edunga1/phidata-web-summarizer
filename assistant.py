import sys

from phi.assistant.assistant import Assistant
from requests import get


def get_html(url: str):
    """Get the HTML of a webpage.

    Args:
        url (str): The URL of the webpage.

    Returns:
        str: The HTML of the webpage.
    """
    return get(url).text


url = sys.argv[1]
message = f"""
`${url}` 사이트의 내용을 요약해주세요.

horizontal line으로 총 3개 구역을 나눠주세요.

첫 번째 구역은 본문 내용을 10줄 이내로 요약해주세요.
두 번째 구역은 리액션이 많은 덧글을 최대 3개까지 원문 그대로 포함해주세요.
마지막 구역은 모든 덧글을 요약해 주세요. 원문은 포함하지 않아도 됩니다.
"""

assistant = Assistant(tools=[get_html], show_tools_calls=True)
assistant.print_response(message, markdown=True)
