from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_openai import AzureOpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter

# 1. Load the file
# 2. Split the document into chunks
# 3. Embedding
# 4. Store the result in chromadb

file_path = "books/example1.txt"
persistent_dir = "db"

# from langchain_community.vectorstores import Chroma

az_emb = AzureOpenAIEmbeddings()

# from langchain_huggingface import HuggingFaceEmbeddings
# hf_emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

loader = TextLoader(file_path=file_path)
docs = loader.load()

splitter = CharacterTextSplitter(chunk_size=1000, separator="", chunk_overlap=0)
chunks = splitter.split_documents(docs)


db = Chroma.from_documents(
    documents=chunks[:30],
    collection_name="azure_emb",
    embedding=az_emb,
    persist_directory=persistent_dir,
)

db2 = Chroma(
    persist_directory=persistent_dir,
    collection_name="azure_emb",
    embedding_function=az_emb,
)

query = "Who is Caius Marcius?"

retriever = db2.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 3, "score_threshold": 0.6},
)

selected_chunks = retriever.invoke(query)
len(selected_chunks)
print(selected_chunks[0].page_content)
