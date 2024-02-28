from phi.tools.toolkit import Toolkit
from requests import get


class WebVisitor(Toolkit):
    def get_html(self, url: str):
        """Get the HTML of a webpage.

        Args:
            url (str): The URL of the webpage.

        Returns:
            str: The HTML of the webpage.
        """
        return get(url).text
