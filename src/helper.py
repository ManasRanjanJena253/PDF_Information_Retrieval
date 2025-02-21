# Importing dependencies
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

from google.generativeai import configure, list_models

configure(api_key=GOOGLE_API_KEY)
available_models = list_models()
for model in available_models:
    print(model.name, model.supported_generation_methods)


# Creating some helper functions

def text_extraction(pdf_docs):
    """Function to extract text from a given pdf."""
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    """Function to split the entire text corpus into smaller parts to not exceed the context length
    the llm model that is being used."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000,
                                                   chunk_overlap = 20)
    chunks = text_splitter.split_text(text)
    return chunks

def create_vector_embeddings(text_chunks):
    """Function to convert the text chunks into their vector embeddings."""
    embeddings = GoogleGenerativeAIEmbeddings(google_api_key = GOOGLE_API_KEY,
                                              model = 'models/embedding-001')  # Creating an instance for our embedding model.
    vector_store = FAISS.from_texts(text_chunks, embedding = embeddings)
    return vector_store

def get_conversational_chain(vector_store):
    """Function to get the conversation occurring with the model"""
    llm = ChatGoogleGenerativeAI(temperature = 0.65,
                                 google_api_key = GOOGLE_API_KEY,
                                 model = "chat-bison-001")
    memory = ConversationBufferMemory(memory_key = 'chat_history',
                                      return_messages = True)    # This will store the memory regarding that particular conversation.
    conversation_chain = ConversationalRetrievalChain.from_llm(llm = llm,
                                                               retriever = vector_store.as_retriever(),
                                                               memory = memory)
    return conversation_chain

