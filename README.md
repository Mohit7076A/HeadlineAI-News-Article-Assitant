# HeadlineAI-News-Article-Assitant

**HeadlineAI** is a news article assistant that provides concise summaries and answers user queries based on the latest news. The project integrates OpenAI’s models and Pathway’s document indexing to deliver accurate and insightful responses. This is initial phase of project. Project still in progress.

## Key Features

- **Summarization**: Generate brief summaries of news articles.
- **Query Answering**: Respond to user queries using news context.
- **Real-time News**: Fetch and process news articles from the News API.

## Technologies

- **OpenAI**: Used for article summarization and query answering.
- **Pathway**: Utilized for document indexing and retrieval, enabling efficient context-based responses.

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/HeadlineAI.git
   cd HeadlineAI
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Or use Docker:

   ```bash
   docker-compose up --build
   ```

3. **Configure API Keys**

   Create a `.env` file and add your OpenAI and News API keys:

   ```bash
   OPENAI_API_KEY=your_openai_api_key
   NEWS_API_KEY=your_news_api_key
   ```

## Highlight

This project showcases Pathway’s capability to efficiently handle document indexing and retrieval, enhancing the effectiveness of AI-driven summarization and query answering.
