import json
from rag import load_rag, rag_search

db = load_rag()

def rag_tool(query):
    return rag_search(query, db)

with open("hospital_data.json") as f:
    data = json.load(f)




def hospital_tool(query):
    query = query.lower()

    # Doctor info
    for doc in data["doctors"]:
        if doc["name"].lower() in query:
            return f"{doc['name']} ({doc['specialization']}) - OPD: {doc['opd_time']}, Fee: ₹{doc['fee']}"

    # Admission
    if "admission" in query:
        return f"Admission charge is ₹{data['admission_charge']}"

    # Room
    if "room" in query:
        return str(data["rooms"])

    # Surgery
    if "surgery" in query or "operation" in query:
        return str(data["surgeries"])

    return "No data found"