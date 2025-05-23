from core.persona import Persona
from core.interaction_engine import InteractionEngine
from summarizer.evolution_reporter import EvolutionReporter

if __name__ == "__main__":
    arin = Persona(name="Arin", age=25, interests=["space", "economics", "philosophy"])
    engine = InteractionEngine(arin)

    print("Hi! Type your messages to chat with Arin. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = engine.handle_input(user_input)
        print(f"Arin: {response}")

    EvolutionReporter().generate_weekly_summary(arin)