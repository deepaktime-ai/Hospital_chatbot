import ollama
from tools import hospital_tool,rag_tool
from memory import Memory
from config import MODEL


class Agent:
    def __init__(self):
        self.memory = Memory()

    def think(self, user_input):
        prompt = f"""
        You are a hospital assistant AI.

        Decide:
        - Use hospital_tool OR
        - Answer directly

        Format:
        ACTION: hospital_tool or NONE
        INPUT: user question

        User: {user_input}
        """

        response = ollama.chat(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]

    def act(self, decision):
        if "hospital_tool" in decision:
            query = decision.split("INPUT:")[-1].strip()
            return hospital_tool(query)

        return "No tool used"

    def respond(self, user_input, tool_result):
        prompt = f"""
        User: {user_input}
        Tool result: {tool_result}

        Give final helpful answer.
        """

        response = ollama.chat(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]

    def run(self, user_input):
        decision = self.think(user_input)
        print("\n🧠 Decision:", decision)

        tool_result = self.act(decision)
        print("\n🛠 Tool Output:", tool_result)

        final_answer = self.respond(user_input, tool_result)

        return final_answer