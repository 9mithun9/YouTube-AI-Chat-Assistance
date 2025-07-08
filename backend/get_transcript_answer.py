# backend/get_transcript_answer.py

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def get_transcript_and_answer(video_id: str, question: str) -> str:
    from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain_openai import OpenAIEmbeddings, ChatOpenAI
    from langchain_community.vectorstores import FAISS
    from langchain_core.prompts import PromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from langchain.schema.runnable import RunnableParallel, RunnableLambda, RunnablePassthrough

    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([d['text'] for d in transcript_list])
    except TranscriptsDisabled:
        return "Transcript is not available for this video."
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.create_documents([transcript])

    # Pass the API key here
    vector_store = FAISS.from_documents(docs, OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY))
    retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k': 3})

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "You are an expert assistant. Generate answers for this question: '{question}' "
            "based on the context below:\n\n{context}"
        )
    )

    model = ChatOpenAI(model="gpt-4o", openai_api_key=OPENAI_API_KEY)

    chain_parallel = RunnableParallel({
        'context': retriever | RunnableLambda(lambda docs: "\n\n".join(doc.page_content for doc in docs)),
        'question': RunnablePassthrough()
    })

    chain = chain_parallel | prompt | model | StrOutputParser()

    return chain.invoke(question)
