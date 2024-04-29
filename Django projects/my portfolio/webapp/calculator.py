import tkinter as tk
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcilator")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Helvetica", 18), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, width=5, height=2, font=("Helvetica",14),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, text):
        current_text = self.result_var.get()

        if text == "=":
            try:
                result = eval(current_text)
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
        else:
            if current_text == "0":
                self.result_var.set(text)
            else:
                self.result_var.set(current_text + text)

# Create the main application window
root = tk.Tk()
app = CalculatorApp(root)

# Run the Tkinter event loop
root.mainloop()