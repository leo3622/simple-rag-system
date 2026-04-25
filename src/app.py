from retriever import search_similar_chunks


def main() -> None:
    query = input("Enter your query: ")
    results = search_similar_chunks(query)
    if not results:
        print("No relevant chunks found.")
        return
    print(f"Top {len(results)} relevant chunks:")
    for i, chunk in enumerate(results, 1):
        print(f"{i}. {chunk.text} (Source: {chunk.source}, Page: {chunk.page}, Score: {chunk.score:.4f})")


if __name__ == "__main__":
    main()
