from langchain_community.document_loaders import PyPDFDirectoryLoader


def load_documents(directory: str = "data/raw"):
    loader = PyPDFDirectoryLoader(directory, glob="*.pdf")
    return loader.load()
