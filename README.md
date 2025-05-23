# cognida
Evolving Persona AI

An offline, open-source AI agent that simulates a persistent, evolving digital persona named Arin. This virtual character has memory, beliefs, and the ability to adapt its worldview over time based on conversation history and new information.

🚀 Features

Stateful memory system using FAISS for vector storage

Local LLM inference with TinyLLaMA via llama-cpp-python

Belief tracking and evolution across sessions

Weekly summaries of how the persona has changed

🧠 System Architecture

User Input → Interaction Engine → LLM + Embedding Model
           ↘                     ↘
          Memory Update       FAISS Index Update
           ↘                     ↘
        Belief Update       Journal Log Update


Interaction Engine: Handles input, generates response using TinyLLaMA, and updates memory.

Memory Manager: Encodes inputs into vector space (MiniLM), stores using FAISS.

Belief Tracker: Updates structured beliefs (e.g., "Mars: Interested in colonization").

Evolution Reporter: Summarizes memory and belief drift.

🧩 Installation

1. Clone the Repository

git clone https://github.com/Teju23022003/cognida.git
cd cognida

2. Set Up Environment

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Download LLM Model

git lfs install
git clone https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF
cd TinyLlama-1.1B-Chat-v1.0-GGUF
git lfs pull --include "TinyLlama-1.1B-Chat-v1.0.Q4_0.gguf"
cp TinyLlama-1.1B-Chat-v1.0.Q4_0.gguf ../models/

💬 How It Works

Each user message is embedded and logged.

Important terms (e.g., "Mars", "philosophy") cause belief updates.

Embeddings are stored in FAISS vector DB.

Weekly evolution is printed based on changes in beliefs and recent memory entries.

📄 Usage

python main.py

Then interact with Arin:

You: Hello!
Arin: That's a fascinating topic! I recently read something new about it.

You: What do you think about Mars?
Arin: Mars colonization is an exciting frontier for humanity...

To exit, type:

You: exit

