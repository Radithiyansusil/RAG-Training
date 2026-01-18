import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders.youtube import YoutubeLoader

# Load PDF
loader = PyPDFLoader(r"D:\\Git\\aaksah_rag_course\\RAG-Training\\Book-1.pdf")
pdf_pages = loader.load()
print(pdf_pages[0])
print("\n" + "="*50 + "\n")

# Load YouTube video - Fixed version
url = "https://www.youtube.com/watch?v=kqtD5dpn9C8"

try:
    # Don't add video info to avoid pytube issues
    loader = YoutubeLoader.from_youtube_url(
        url,
        add_video_info=False,  # Set to False to avoid pytube
        language=["en", "en-US"]
    )
    docs = loader.load()
    print(f"Loaded {len(docs)} YouTube documents")
    print(f"Transcript preview: {docs[0].page_content[:300]}...")
    print(f"\nMetadata: {docs[0].metadata}")
except Exception as e:
    print(f"Error loading YouTube video: {e}")