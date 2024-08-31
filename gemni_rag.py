from langchain_community.document_loaders import TextLoader # type: ignore
from langchain.indexes import VectorstoreIndexCreator # type: ignore
from langchain.text_splitter import CharacterTextSplitter # type: ignore
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings # type: ignore
from dotenv import load_dotenv # type: ignore
import os




# Load environment variables from .env file
load_dotenv()

# Initialize the Google Generative AI with the correct API key parameter
llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")  # Corrected typo here
)

try:
    loader = TextLoader("Data.txt")
except Exception as e:
    print(f"Error loading data: {e}")
    loader = None


# creating embadding
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")


# creating text splitter

text_splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)


# vector store creation
index_creator = VectorstoreIndexCreator(
    embedding=embedding,
    text_splitter=text_splitter,
)


index = index_creator.from_loaders([loader])


# Query the index with llm
while True:
    human_message = input("Ask any question about human diseases: ")
    response = index.query(human_message, llm = llm)
    print(response)








