from langchain_core.tools import tool


@tool("search", parse_docstring=True)
def dummy_web_search(query: str) -> list[str]:
    """
    You are a helpful supplier researcher that uses tools to answer questions
precisely after doing thorough research on google and document search. The google
search tool can provide customer sentiment on the suppliers. The document search tool
has the procurement requisition rules and past year supplier review.

    Args:
        query: User query to search in documents and web.

    Returns:
        Dummy list of search results.
    """
    return ["IBM watsonx.ai"]
