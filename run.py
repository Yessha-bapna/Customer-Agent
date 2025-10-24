from src.graph_agent import app

print("Product Return Support Agent ")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        break

    app.invoke({"user_input": user_input})
