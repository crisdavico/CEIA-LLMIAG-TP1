**README.md**  

# 📄 Chatbot de Consulta de Currículum Vitae (CV)  

Este proyecto es un **chatbot interactivo** desarrollado con **Streamlit** que permite cargar un Currículum Vitae (CV) desde un directorio local, almacenarlo en una base de datos vectorial en **Pinecone**, y realizar consultas de forma dinámica utilizando un **Large Language Model (LLM)**, en este caso, **Llama 3 8B de Groq**.  

El objetivo principal es permitir una interacción ágil y eficiente con la información del CV, proporcionando respuestas precisas a partir de preguntas en lenguaje natural.  

---

## 🚀 **Funcionalidades Principales**  

- **Carga de CV**: El usuario puede subir un archivo de CV desde un directorio local.  
- **Vectorización del CV**: El CV se convierte en un vector y se almacena en **Pinecone**, una base de datos vectorial escalable.  
- **Consultas sobre el CV**: El usuario puede realizar preguntas personalizadas sobre el contenido del CV, como:  
  - _"¿En qué proyectos ha trabajado esta persona?"_  
  - _"¿Cuántos años de experiencia tiene en Python?"_  
  - _"¿Qué certificaciones posee?"_  
- **IA para Consultas**: Utiliza una **LLM de Groq (Llama 3 8B)** para interpretar las preguntas y buscar la respuesta relevante en la base vectorial.  

---

## 🛠️ **Tecnologías Utilizadas**  

| **Tecnología**    | **Uso**                         |
|-------------------|---------------------------------|
| **Streamlit**     | Interfaz gráfica (UI) del chatbot |
| **Pinecone**      | Base de datos vectorial para almacenar el CV |
| **Groq (Llama 3 8B)** | LLM para procesamiento y comprensión de texto |
| **Python**        | Lenguaje principal del proyecto |

---

## 📦 **Instalación**  

1️⃣ **Clonar el repositorio**  
```bash
git clone https://github.com/crisdavico/CEIA-LLMIAG-TP1.git
cd CEIA-LLMIAG-TP1
```

2️⃣ **Crear un entorno virtual**  
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate
```

3️⃣ **Instalar las dependencias**  
```bash
pip install -r requirements.txt
```

4️⃣ **Configurar las claves de acceso**  
- **Pinecone API Key**: Necesitas crear una cuenta en [Pinecone.io](https://www.pinecone.io/) y obtener la clave API.  
- **Groq API Key**: Configura la clave para utilizar la LLM **Llama 3 8B**.  

Para facilitar la configuración, puedes crear un archivo `.env` en la raíz del proyecto:  
```
PINECONE_API_KEY=tu_api_key_aqui
GROQ_API_KEY=tu_api_key_aqui
```

Asegúrate de que tu entorno de desarrollo pueda leer variables de entorno.  

---

## ▶️ **Ejecución de la Aplicación**  

Para iniciar la aplicación, ejecuta:  
```bash
streamlit run main.py
```

Accede a la aplicación desde tu navegador en la URL **http://localhost:8501**.  

---

## 📚 **Uso de la Aplicación**  

**Realizar consultas**  
- Escribe preguntas relacionadas con el CV en la interfaz.  
- Las respuestas se generarán en tiempo real mediante la LLM **Llama 3 8B**.  

Ejemplos de preguntas:  
- _"¿Cuáles son las habilidades técnicas más destacadas?"_  
- _"¿Cuánto tiempo trabajó en su último empleo?"_  
- _"¿Qué tipo de certificaciones posee?"_  

---

## ⚙️ **Configuración Adicional**  

- **Personalización de la LLM**: Puedes cambiar el tamaño del modelo o modificar el prompt que se envía a la LLM.  
- **Almacenamiento en Pinecone**: Puedes ajustar la configuración de la base vectorial para almacenar más de un CV o controlar el espacio de nombres (namespaces) para organizar la información.  

---

## 📜 **Requisitos Técnicos**  

- **Python 3.8 o superior**  
- **Acceso a Internet** (para la conexión con Pinecone y Groq)  
- **Claves API** de Pinecone y Groq  

---

## 🧠 **Conceptos Clave**  

### 🧮 **Vectorización**  
El CV se convierte en un vector para almacenarse en **Pinecone**, una base de datos vectorial. Cada oración, palabra o sección del CV se transforma en una representación numérica que permite realizar búsquedas de similitud de manera eficiente.  

### 🤖 **Modelo de Lenguaje Llama 3 8B (LLM)**  
El modelo Llama 3 8B es una red neuronal preentrenada que puede interpretar el lenguaje natural y generar respuestas. Usamos este modelo para comprender la pregunta del usuario y buscar la respuesta adecuada en la base vectorial.  

### 📡 **Pinecone**  
Pinecone es una base de datos vectorial que permite realizar búsquedas de similitud de alta velocidad. Este sistema se utiliza para almacenar y recuperar representaciones vectoriales del CV.  

---

## 🛠️ **Personalización**  

- **Customización de Pinecone**: Cambiar la cantidad de dimensiones en la vectorización.  
- **Cambio de LLM**: Sustitución de la LLM de Groq por otra, como OpenAI o modelos open-source.  
- **Prompt Tuning**: Modificación del prompt de la LLM para personalizar las respuestas.  

---

## 💡 **Problemas Frecuentes**  

**1️⃣ Error de conexión con Pinecone**  
- Verifica la API Key de Pinecone.  
- Asegúrate de que el namespace esté configurado correctamente.  

**2️⃣ La LLM no responde correctamente**  
- Revisa la configuración del prompt.  
- Verifica la clave de API de Groq y su límite de uso.  

---

## ✉️ **Contacto**  

Si tienes preguntas o deseas colaborar, no dudes en contactarme a través de [crisdavico95@gmail.com](https://github.com/crisdavico).  

---

¡Gracias por usar el Chatbot de Consulta de CV! 🚀