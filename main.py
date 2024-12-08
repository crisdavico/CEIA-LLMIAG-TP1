import streamlit as st
from cv_processor import procesar_cv
from embeddings import crear_embeddings
import os
from groq import Groq


def main():
    st.title("Chatbot sobre mi CV")
    st.write("Hazme una pregunta sobre mi experiencia y habilidades.")

    # Inicializa el historial de conversación en el estado de la sesión
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []

    # Procesar CV y crear embeddings (solo la primera vez)
    if 'qa_chain' not in st.session_state:
        with st.spinner('Procesando el CV y configurando el chatbot...'):
            path = os.path.join(os.path.dirname(__file__), "cv_prueba.pdf")
            docs = procesar_cv(path)
            qa_chain = crear_embeddings(docs)
            st.session_state.qa_chain = qa_chain
            st.success('Chatbot configurado exitosamente.')
    else:
        qa_chain = st.session_state.qa_chain

    pregunta = st.text_input("Escribe tu pregunta aquí:")
    if st.button("Enviar") and pregunta:
        with st.spinner('Generando respuesta...'):
            pinecone_search = qa_chain.similarity_search(pregunta, k=3)
            rag = " ".join([resultado.page_content for resultado in pinecone_search])

            # Carga la clave de API de GROQ desde las variables de entorno
            groq_api_key = os.environ.get("GROQ_API_KEY")

            # Crea el cliente de GROQ
            client = Groq(
                api_key=groq_api_key,
            )

            # Agrega el mensaje del usuario al historial de conversación
            st.session_state.conversation_history.append({"role": "user", "content": pregunta + rag})

            # Genera la respuesta del chatbot utilizando el modelo LLaMA 3 y el historial de la conversación
            chat_completion = client.chat.completions.create(
                messages=st.session_state.conversation_history,
                model="llama3-8b-8192",
            )

            system_prompt = f"""
                Eres un asistente experto que utiliza información específica proporcionada por el usuario para responder preguntas de manera precisa y contextual.

                A continuación, se te proporcionará un fragmento de información relevante y una pregunta relacionada con esta información. Debes responder únicamente basándote en los datos proporcionados, sin inventar ni asumir información adicional. Si no encuentras suficiente información en el fragmento proporcionado para responder la pregunta, indica claramente que no puedes responder con los datos disponibles.

                ### Información proporcionada:
                {rag}

                """

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": f"{st.session_state.conversation_history}",
                    }
                ],
                model="llama3-8b-8192",
                temperature=0.5,
            )

            response = chat_completion.choices[0].message.content

            # Agrega la respuesta del chatbot al historial de conversación
            st.session_state.conversation_history.append({"role": "assistant", "content": response})
            
            st.write("**Respuesta:**")
            st.write(response)

if __name__ == "__main__":
    main()