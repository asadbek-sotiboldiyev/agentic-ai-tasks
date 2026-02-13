# from langchain.embeddings import
from langchain.vectorstores import FAISS
from transformers import AutoModel, AutoTokenizer

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
model = AutoModel.from_pretrained(EMBEDDING_MODEL)

texts = [
    "LangChain LLM asosidagi ilovalarni yaratish uchun ishlatiladi",
    "Vector database embeddinglar bilan ishlaydi",
    "FAISS lokal vector storage hisoblanadi",
    "Embedding matnning ma'nosini saqlaydi",
]

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_texts(texts, embeddings)

query = "vector database nima?"
docs = db.similarity_search(query)

print(docs[0].page_content)
