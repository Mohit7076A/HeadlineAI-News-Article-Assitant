import openai
import requests
import pathway as pw
from pathway.xpacks.llm import embedders
from pathway.xpacks.llm.llms import LiteLLMChat
from pathway.stdlib.indexing import default_vector_document_index
from pathway.xpacks.llm.question_answering import answer_with_geometric_rag_strategy_from_index
import pandas as pd
import config

# Set OpenAI API key
openai.api_key = config.OPENAI_API_KEY

# Fetch news data from News API
def fetch_news(api_key, query='latest'):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

# Summarize an article using OpenAI's LLM and Pathway
def summarize_article(article_content, model):
    prompt = f"Summarize the following article:\n\n{article_content}"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=150
    )
    summary = response.choices[0].text.strip()
    return summary

# Answer user queries based on the indexed news articles
def answer_user_query(query, model, embedder, index):
    query_df = pd.DataFrame({"query": [query]})
    answers = answer_with_geometric_rag_strategy_from_index(
        model, index, pw.debug.table_from_pandas(query_df), num_relevant=5
    )
    return answers

def main():
    # Initialize Pathway components
    embedder = embedders.SentenceTransformerEmbedder(config.EMBEDDING_MODEL)
    model = LiteLLMChat(
        model=config.LLM_MODEL,
        temperature=0.7,
        top_p=0.9,
        api_base="http://localhost:11434"  # Replace with your LLM service endpoint
    )

    # Fetch and process news data
    news_data = fetch_news(config.NEWS_API_KEY)
    articles = news_data.get('articles', [])
    article_contents = [article['content'] for article in articles if article.get('content')]
    
    # Load data into Pathway and create an index
    pw_data = pw.debug.table_from_pandas(pd.DataFrame({"content": article_contents}))
    index = default_vector_document_index(
        pw_data.content, 
        pw_data, 
        embedder=embedder, 
        dimensions=embedder.get_embedding_dimension()
    )

    # Process each article and print summaries
    for article in articles:
        content = article['content']
        summary = summarize_article(content, model)
        print(f"Title: {article['title']}\nSummary: {summary}\n")

    # Example query
    query = "Latest advancements in AI technology"
    answer = answer_user_query(query, model, embedder, index)
    print(f"Query: {query}\nAnswer: {answer}\n")

if __name__ == "__main__":
    main()
