import tkinter as tk
from tkinter import scrolledtext
from agent1_research import research
from agent2_answer_drafter import draft_answer

def run_workflow():
    query = input_box.get()
    if not query.strip():
        return
    output_box.delete(1.0, tk.END)  # clear previous output
    output_box.insert(tk.END, "Researching...\n")
    
    # Step 1: Research
    research_text = research(query)
    
    # Step 2: Draft answer
    answer = draft_answer(research_text)
    
    output_box.insert(tk.END, answer)

# Setup main window
root = tk.Tk()
root.title("Deep Research AI")

# Input box
tk.Label(root, text="Enter your query:").pack()
input_box = tk.Entry(root, width=50)
input_box.pack(pady=5)

# Button
run_button = tk.Button(root, text="Run", command=run_workflow)
run_button.pack(pady=5)

# Output box
tk.Label(root, text="AI Answer:").pack()
output_box = scrolledtext.ScrolledText(root, width=60, height=20)
output_box.pack(pady=5)

root.mainloop()
