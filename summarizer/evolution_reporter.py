class EvolutionReporter:
    def generate_weekly_summary(self, persona):
        print("\n\n--- Weekly Evolution Summary ---")
        print(f"Beliefs:")
        for k, v in persona.beliefs.items():
            print(f"- {k}: {v}")
        print("\nMemories:")
        for m in persona.memory[-5:]:
            print(f"- [{m['timestamp']}] {m['event']}")
        print("--------------------------------\n")
