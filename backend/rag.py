from typing import List

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

from langchain_core.documents import Document

from config import *


search_client = SearchClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    index_name=AZURE_SEARCH_INDEX,
    credential=AzureKeyCredential(AZURE_SEARCH_KEY),
)


def search_documents(query: str, top: int = 5) -> List[Document]:

    results = search_client.search(
        search_text=query,
        top=top
    )

    documents = []

    for item in results:

        documents.append(
            Document(
                page_content=item["content_text"],
                metadata={
                    "title": item.get("document_title"),
                    "path": item.get("content_path"),
                    "id": item.get("content_id"),
                }
            )
        )

    return documents



