# AI Web Scraper

This project is an AI-powered web scraper built using `Streamlit` for the UI, `BeautifulSoup` for web scraping, and the `Groq` API for intelligent content parsing. It allows users to provide a website URL, scrape its content, and then ask specific questions about the scraped data, which is parsed accordingly.

## Features

- **Website Scraping:** Enter a website URL, and the app will retrieve and display the cleaned HTML body content.
- **Content Parsing:** Describe the information you want to extract from the scraped content, and the AI will parse the DOM content accordingly.
- **Interactive UI:** Built with Streamlit, the app provides a simple and interactive interface.

## How It Works

1. **Input a Website URL**: The user inputs a URL in the Streamlit interface.
2. **Scrape the Website**: The HTML content of the page is fetched using `requests` and parsed with `BeautifulSoup`.
3. **Clean the Content**: The scraper cleans the HTML content, removing unnecessary scripts and styles.
4. **Ask Questions**: The user can describe what they want to extract from the DOM, and the app uses the Groq API to parse the cleaned content based on the user’s description.
5. **Output**: The relevant data from the page is displayed in the app.
