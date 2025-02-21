# 📄 PDF Information Retrieval System

This project retrieves and answers questions about the content of uploaded PDF documents by combining powerful tools such as LangChain, Google's Gemini API, PyPDF2, and Streamlit. It extracts text from PDFs, splits the text into manageable chunks, creates vector embeddings for efficient retrieval, and provides an interactive conversational interface to query the document.

## ✨ Features

- 🔍 **PDF Text Extraction:**  
  Uses [PyPDF2](https://pypi.org/project/PyPDF2/) to extract text from PDF files.

- 📏 **Text Chunking:**  
  Utilizes LangChain's `RecursiveCharacterTextSplitter` to divide large texts into smaller, manageable chunks.

- 🧠 **Vector Embeddings:**  
  Converts text chunks into vector embeddings using Google's Gemini API via LangChain for semantic search.

- 💬 **Conversational Retrieval:**  
  Implements a conversational retrieval chain that allows interactive Q&A sessions about the PDF content.

- 🎨 **User-Friendly Interface:**  
  Built with [Streamlit](https://streamlit.io/) for a responsive and interactive web-based interface.

## 🛠 Technologies Used

- **LangChain**: For text processing, embeddings, and conversational retrieval chains.
- **Google Gemini API**: For generating embeddings and powering the language model.
- **PyPDF2**: For extracting text from PDF files.
- **Streamlit**: For creating a user-friendly web interface.
- **FAISS**: For efficient vector storage and retrieval (if using FAISS for vector stores).

## 🚀 Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Create a Virtual Environment (optional but recommended):**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the root directory with the following content (replace the placeholder with your actual API key):

   ```plaintext
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## 🎯 Usage

1. **Run the Streamlit App:**

   ```bash
   streamlit run app.py
   ```

2. **Interact with the App:**
   - 📤 Use the sidebar to upload one or multiple PDF files.
   - ⏳ Click on the "Submit & Process" button to extract text and build the vector embeddings.
   - ❓ Ask questions in the main interface to retrieve information from the PDF documents.
   - 📝 The conversation history will be maintained during your session for context-aware responses.

## 📂 Project Structure

```
├── .env                 # Environment variables (e.g., API keys)
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
└── src
    └── helper.py        # Helper functions for text extraction, chunking, embeddings, and conversational chain setup
```

## 🔮 Future Enhancements

- 📄 **Enhanced Document Parsing:**  
  Support additional document formats beyond PDFs.
- 🧠 **Improved Conversational Memory:**  
  Enhance the conversation history to better handle long interactions.
- 🎨 **UI Improvements:**  
  Expand the Streamlit interface with additional features and styling.
- ☁️ **Deployment:**  
  Containerize the application for deployment to cloud platforms.

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.



