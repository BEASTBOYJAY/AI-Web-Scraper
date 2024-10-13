import requests
from bs4 import BeautifulSoup


def get_html_content(website):
    """Fetches the HTML content of a given website.

    Args:
        website (str): The URL of the website to fetch content from.

    Returns:
        str: The prettified HTML content if successful, or an error message.
    """
    try:
        response = requests.get(website)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            return soup.prettify()
        else:
            return f"Failed to retrieve content. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"


def get_body_content(html_content):
    """Extracts the body content from the provided HTML.

    Args:
        html_content (str): The HTML content from which to extract the body.

    Returns:
        str: The body content as a string, or an empty string if no body is found.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def get_cleaned_body_content(body_content):
    """Cleans the body content by removing scripts and styles.

    Args:
        body_content (str): The body content to clean.

    Returns:
        str: The cleaned body content with scripts and styles removed.
    """
    soup = BeautifulSoup(body_content, "html.parser")
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    """Splits the DOM content into chunks of specified maximum length.

    Args:
        dom_content (str): The DOM content to split.
        max_length (int, optional): The maximum length of each chunk. Defaults to 6000.

    Returns:
        list of str: A list containing chunks of the DOM content.
    """
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
