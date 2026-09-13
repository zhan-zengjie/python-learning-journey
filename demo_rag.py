from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FakeEmbeddings

# 读取我们自己写的txt文档
with open("article.txt","r",encoding="utf-8") as f:
    full_text = f.read()

# 将长文本切分成小块
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)
chunks = splitter.create_documents([full_text])

# 假的嵌入，仅做演示，不需要下载模型
embedding = FakeEmbeddings(size=512)

# 构建本地向量数据库
vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="./my_db"
)

retriever = vector_db.as_retriever(k=2)

if __name__ == "__main__":
    question = "RAG是什么？"
    result = retriever.invoke(question)
    print("====匹配检索出来的内容====")
    for piece in result:
        print(piece.page_content)
