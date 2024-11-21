import tkinter as tk
from tkinter import ttk

class BlockchainVisualizer(tk.Tk):
    def __init__(self, blockchain):
        super().__init__()
        self.blockchain = blockchain
        self.title("Blockchain Visualizer")
        self.geometry("800x600")

        # Create a Treeview to display the blocks and their data
        self.tree = ttk.Treeview(self, columns=("Index", "Timestamp", "Data", "Hash"), show="headings")
        self.tree.heading("Index", text="Index")
        self.tree.heading("Timestamp", text="Timestamp")
        self.tree.heading("Data", text="Data")
        self.tree.heading("Hash", text="Hash")
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Add blocks to the Treeview
        self.display_blocks()

        # Button to add new block
        self.add_button = tk.Button(self, text="Add Block", command=self.add_new_block)
        self.add_button.grid(row=1, column=0, pady=20)

    def display_blocks(self):
        for block in self.blockchain.get_chain():
            self.tree.insert("", "end", values=(block["index"], block["timestamp"], block["data"], block["hash"]))

    def add_new_block(self):
        # Get new data and add a new block to the blockchain
        data = f"Block {len(self.blockchain.chain)}"
        self.blockchain.add_block(data)
        # Clear the tree and display updated chain
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.display_blocks()

if __name__ == "__main__":
    # Create and populate the blockchain
    blockchain = Blockchain()
    blockchain.add_block("First Block Data")
    blockchain.add_block("Second Block Data")

    # Initialize and start the visualizer
    app = BlockchainVisualizer(blockchain)
    app.mainloop()
