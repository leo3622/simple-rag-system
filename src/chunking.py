from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

MARKDOWN_SEPARATORS = [
    "\n#{1,6} ",
    "\n```",
    "\n---\n",
    "\n***\n",
    "\n___\n",
    "\n\n",
    "\n",
    " ",
    "",
]

def chunk_text(document: list[Document]) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        model_name="text-embedding-3-small",
        chunk_size=500,
        chunk_overlap=50,
        add_start_index=True,
        strip_whitespace=True,
        separators=MARKDOWN_SEPARATORS,
        is_separators_regex=True,
    )
    return splitter.split_documents(document)
