from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

client = Groq(api_key=api_key)

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)


def parser(dom_chunks, parse_description):
    """Parses DOM content chunks to extract specified information.

    Args:
        dom_chunks (list of str): Chunks of DOM content to be parsed.
        parse_description (str): Description of the information to extract.

    Returns:
        str: The extracted information from all chunks, concatenated together.
              Returns an empty string if no information matches the description.
    """
    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        prompt = template.format(dom_content=chunk, parse_description=parse_description)

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt}",
                }
            ],
            model="llama3-8b-8192",
        )

        response_text = chat_completion.choices[0].message.content
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(response_text)

    return "\n".join(parsed_results)
