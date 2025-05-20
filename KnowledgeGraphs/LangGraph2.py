import langgraph
from langgraph.graph import StateGraph,END, START
from typing import TypedDict, List, Dict, Any, Optional

from transformers import pipeline
from dataclasses import dataclass

# Load Hugging Face spam detection model

classifier = pipeline("text-classification", model="facebook/bart-large-mnli")
#classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
#classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")




# Define structured state
#@dataclass
class MessageState(TypedDict):
    message: str
    classification: str = "Unknown"



# Define nodes
def classify_message(state: MessageState) -> MessageState:

    print(f"Received state: {state}")
    labels = ["spam", "ham"]
    if 'message' not in state:
        raise KeyError("The 'message' key is missing from the state.")
    result = classifier(state['message'])[0]
    state['classification'] = result["label"]
    print(f"After classification: {state}")
    return state


'''
def classify_message(state: MessageState) -> MessageState:
    """Determine if message is spam or ham."""
    result = classifier(state['message'])[0]
    state['classification'] = result["label"]
    return state



def classify_message(state: MessageState) -> MessageState:
    print(f"Before classification: {state}")
    result = classifier(state['message'])[0]
    state['classification'] = result["label"]
    print(f"After classification: {state}")
    return state
'''
def spam_alert(state: MessageState) -> MessageState:
    """Handles spam classification."""
    print(f"🚨 ALERT: The message is classified as SPAM! 🚨")
    return state

def ham_confirmation(state: MessageState) -> MessageState:
    """Handles ham classification."""
    print(f"✅ The message is classified as HAM (safe).")
    return state

def final_result(state: MessageState) -> MessageState:
    """Final state that completes processing."""
    print(f"Processing finished for message: '{state.message}'")
    return state

def spam_or_ham(state: MessageState) -> str:
    """Decision function to determine the next node based on classification."""
    return "spam" if state.classification == "spam" else "ham"


#initial_state = MessageState(message="Congratulations! You won a prize. Click here!", 
                           #  classification= "Unknown")
initial_state = MessageState(message="USA has 50 states.", 
                             classification= "Unknown")


graph = StateGraph(MessageState)
graph.add_node("Spam Detection", classify_message)
graph.add_edge(START, "Spam Detection")
compiled_graph = graph.compile()
compiled_graph.invoke(START, initial_state)
'''
# Create a StateGraph instance
graph = StateGraph(MessageState)
# Add nodes to StateGraph

graph.add_node("Spam Detection", classify_message)
graph.add_node("Spam Alert", spam_alert)
graph.add_node("Ham Confirmation", ham_confirmation)

# Define edges with conditional transitions

graph.add_edge(START, "Spam Detection")  # Entry point added

graph.add_conditional_edges("Spam Detection", 
                            spam_or_ham,
                            {
                                "spam":"Spam Alert",
                                 "ham":"Ham Confirmation"
                                 })
graph.add_edge("Spam Alert", END)

graph.add_edge("Ham Confirmation", END)

compiled_graph = graph.compile()  # Display graph structure
# Compile and execute the graph


initial_state = MessageState(message="Congratulations! You won a prize. Click here!")



compiled_graph.invoke(START, initial_state)  # Execute processing

'''

