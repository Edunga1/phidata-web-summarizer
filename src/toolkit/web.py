from phi.tools.toolkit import Toolkit
from requests import get


class WebVisitor(Toolkit):
    def __init__(self):
        super().__init__(name="web-visitor")

        self.register(self.get_html)

    def get_html(self, url: str) -> str:
        """Use this function to get the content of a webpage.

        Args:
            url (str): The URL of the webpage.

        Returns:
            The content of the webpage.
            May contain HTML, CSS, JavaScript, etc.
        """
        return get(url).text
