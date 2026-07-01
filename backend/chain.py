from rag import search_documents

from llm import llm

from prompt import prompt

from langchain_core.output_parsers import StrOutputParser


parser = StrOutputParser()


def ask(question):

    docs = search_documents(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    chain = (
        prompt
        | llm
        | parser
    )

    answer = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    return {
        "answer": answer,
        "sources": [
            doc.metadata
            for doc in docs
        ]
    }


result = ask(
    "Summarize Kunal LOR.pdf"
)

print(result["answer"])

print(result["sources"])