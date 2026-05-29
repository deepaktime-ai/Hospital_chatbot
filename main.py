from agent import Agent

agent = Agent()

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    response = agent.run(user_input)
    print("\n🤖:", response)