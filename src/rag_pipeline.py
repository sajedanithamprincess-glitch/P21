class RAGPipeline:
    def __init__(self, vector_store, llm_service, top_k=5):
        self.vector_store = vector_store
        self.llm_service = llm_service
        self.top_k = top_k

    def ask(self, query):
        results = self.vector_store.similarity_search_with_score(query, k=self.top_k)

        context_blocks = []

        for i, (doc, score) in enumerate(results, 1):
            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", "N/A")

            block = f"""
Document {i}
Source: {source}
Page: {page}
Similarity Score: {score:.4f}

Content:
{doc.page_content}
"""
            context_blocks.append(block)

        context_text = "\n".join(context_blocks)

        return self.llm_service.generate_answer(query, context_text)