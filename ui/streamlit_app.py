import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/query"
UPLOAD_URL = "http://127.0.0.1:8000/upload"

st.set_page_config(
    page_title="Customer Support RAG Agent",
    page_icon="🤖",
    layout="wide"
)

st.title(
    "🤖 Customer Support RAG Agent"
)

# Session Memory
if "messages" not in st.session_state:

    st.session_state.messages = []

# Sidebar
with st.sidebar:

    st.header(
        "Upload Document"
    )

    uploaded_file = st.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )

    if uploaded_file:

        if st.button(
            "Upload PDF"
        ):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf"
                )
            }

            response = requests.post(
                UPLOAD_URL,
                files=files
            )

            if response.status_code == 200:

                st.success(
                    response.json()["message"]
                )

            else:

                st.error(
                    "Upload Failed"
                )

    st.divider()

    if st.button(
        "Clear Chat"
    ):

        st.session_state.messages = []

        st.rerun()

# Display Chat History
for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )

        if message.get(
            "sources"
        ):

            with st.expander(
                "Sources"
            ):

                for source in message["sources"]:

                    st.write(
                        source
                    )

# Chat Input
question = st.chat_input(
    "Ask a question..."
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message(
        "user"
    ):

        st.markdown(
            question
        )

    payload = {
        "question": question
    }

    try:

        response = requests.post(
            API_URL,
            json=payload,
            timeout=60
        )

        if response.status_code == 200:

            data = response.json()

            answer = data["answer"]

            sources = data.get(
                "sources",
                []
            )

            with st.chat_message(
                "assistant"
            ):

                st.markdown(
                    answer
                )

                if sources:

                    with st.expander(
                        "Sources"
                    ):

                        for source in sources:

                            st.write(
                                source
                            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                }
            )

        else:

            st.error(
                f"API Error: {response.status_code}"
            )

    except Exception as e:

        st.error(
            str(e)
        )