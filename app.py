import streamlit as st
from src.helper import text_extraction, get_text_chunks, get_conversational_chain, create_vector_embeddings
from google.generativeai import configure, list_models

def user_input(user_req):
    """Function to take input from the user and give output using llm."""
    response = st.session_state.conversation({'question' : user_req, 'chat_history' : None})
    st.session_state.chatHistory = response['chat_history']   # Storing the answer given by the model as chat history.
    for i, message in enumerate(st.session_state.chatHistory):
        if i%2 == 0:
            st.write("User :", message.content)
        else:
            st.write("Reply :", message.content)

def main():
    st.set_page_config("Information Retrieval")  # Setting the name of the webpage.
    st.header("Information-Retrieval-System")   # Setting the heading of the page.

    user_req = st.text_input("Ask any question regarding the uploaded PDF")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    if user_req:  # If the user has asked any question it will be sent to the llm.
        user_input(user_req)

    with st.sidebar:   # Writing all the contents of the sidebar.
        st.title("Menu")
        pdf_docs = st.file_uploader("Upload your PDF files and click on the Submit & Process Button", accept_multiple_files = True)
        if st.button("Submit & Process"):
            with st.spinner("Processing...."):  # This will create a circular loading icon which will represent the processing and once it's done the code inside this block will run.
                raw_text = text_extraction(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = create_vector_embeddings(text_chunks)
                get_conversational_chain(vector_store)
                st.session_state.conversation = get_conversational_chain(vector_store)   # Creating a session using streamlit whose memory will be kept until the conversation is over.

                st.success("Done")   # If the processing is completed this message will be shown.


if __name__ == "__main__":     # This is called as modular coding by this particular statement our script will start running from this line.
    main()