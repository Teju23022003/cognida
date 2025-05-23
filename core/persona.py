import json
from datetime import datetime
import faiss
import numpy as np
import os

class Persona:
    def __init__(self, name, age, interests):
        self.name = name
        self.age = age
        self.interests = interests
        self.memory = []
        self.beliefs = {}
        
        # Ensure logs directory exists
        os.makedirs("logs", exist_ok=True)
        
        self.log_file = f"logs/{self.name}_journal.json"
        self.index_file = f"logs/{self.name}_vector.index"
        self._load_memory()
        self._init_vector_store()


    def _load_memory(self):
        try:
            with open(self.log_file, "r") as f:
                data = json.load(f)
                self.memory = data.get("memory", [])
                self.beliefs = data.get("beliefs", {})
        except FileNotFoundError:
            pass

    def _save_memory(self):
        with open(self.log_file, "w") as f:
            json.dump({"memory": self.memory, "beliefs": self.beliefs}, f, indent=2)

    def update_memory(self, event, embedding=None):
        timestamp = datetime.now().isoformat()
        entry = {"timestamp": timestamp, "event": event}
        self.memory.append(entry)
        if embedding is not None:
            self.index.add(np.array([embedding]).astype("float32"))
            faiss.write_index(self.index, self.index_file)
        self._save_memory()

    def update_belief(self, key, value):
        self.beliefs[key] = value
        self._save_memory()

    def _init_vector_store(self):
        dim = 384  # Embedding size for MiniLM
        if os.path.exists(self.index_file):
            self.index = faiss.read_index(self.index_file)
        else:
            self.index = faiss.IndexFlatL2(dim)

    def reflect(self):
        return self.beliefs