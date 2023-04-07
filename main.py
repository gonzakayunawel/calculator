import tkinter as tk
from math import sqrt

def run():

    # Main Window
    main_window = tk.Tk()
    main_window.geometry("460x435")
    main_window.title("My Own Calculator")
    main_window.resizable(width=False, height=False)
    main_window.iconbitmap("calculator.ico")

    # Background
    bg = tk.Label(bg="#84C7D0")
    bg.pack(fill = tk.BOTH, expand = True)

    # Expression Entry
    expression_entry = tk.Label(bg, width=24, height=2, font = "Helvetica 14", bg="#F3C677")
    expression_entry.grid(column=0, row = 0, columnspan=3, padx=1.5, pady=1.5)

    # Function to calculate
    def calculate():
        expression = expression_entry["text"]
        try:
            result = eval(expression)
            expression_entry["text"] = result
            expression_entry["bg"] = "#D0FE00"
        except:
            expression_entry["text"] = "Math Error or Syntax Error"
            expression_entry["bg"] = "#D0FE00"

    # Button "Equal to"
    equal_to_button = tk.Button(bg, text = "=", padx=0, height=2, width=7, font="bold", bg="#F9564F", fg="#FFF", command=calculate)
    equal_to_button.grid(column=3, row = 0)

    # add the symbols from buttons to the expressions entry
    def add_symbol(symbol_value):
        value = expression_entry["text"]
        expression_entry["text"] = value+str(symbol_value)

    # Clear screen
    def clear_button():
        expression_entry["text"] = ""
        expression_entry["bg"] = "#F3C677"

    # It Stores current value in the memory and prints it in the screen
    def memory_store():
        memory = expression_entry["text"]
        clear_button()
        expression_entry["text"] = str(memory)

    # Numbers Buttons
    one = tk.Button(bg, text = "1", width=7, height=3, cursor="hand2", command=lambda:add_symbol("1"), bg="#B33F62", font="bold")
    one.grid(column = 0, row = 1, padx=1.5, pady=1.5)
    two = tk.Button(bg, text = "2", width=7, height=3, cursor="hand2", command=lambda:add_symbol("2"), bg="#B33F62", font="bold")
    two.grid(column = 1, row = 1, padx=1.5, pady=1.5)
    three = tk.Button(bg, text = "3", width=7, height=3, cursor="hand2", command=lambda:add_symbol("3"), bg="#B33F62", font="bold")
    three.grid(column = 2, row = 1, padx=1.5, pady=1.5)

    four = tk.Button(bg, text = "4", width=7, height=3, cursor="hand2", command=lambda:add_symbol("4"), bg="#B33F62", font="bold")
    four.grid(column = 0, row = 2, padx=1.5, pady=1.5)
    five = tk.Button(bg, text = "5", width=7, height=3, cursor="hand2", command=lambda:add_symbol("5"), bg="#B33F62", font="bold")
    five.grid(column = 1, row = 2, padx=1.5, pady=1.5)
    six = tk.Button(bg, text = "6", width=7, height=3, cursor="hand2", command=lambda:add_symbol("6"), bg="#B33F62", font="bold")
    six.grid(column = 2, row = 2, padx=1.5, pady=1.5)

    seven = tk.Button(bg, text = "7", width=7, height=3, cursor="hand2", command=lambda:add_symbol("7"), bg="#B33F62", font="bold")
    seven.grid(column = 0, row = 3, padx=1.5, pady=1.5)
    eight = tk.Button(bg, text = "8", width=7, height=3, cursor="hand2", command=lambda:add_symbol("8"), bg="#B33F62", font="bold")
    eight.grid(column = 1, row = 3, padx=1.5, pady=1.5)
    nine = tk.Button(bg, text = "9", width=7, height=3, cursor="hand2", command=lambda:add_symbol("9"), bg="#B33F62", font="bold")
    nine.grid(column = 2, row = 3, padx=1.5, pady=1.5)

    zero = tk.Button(bg, text = "0", width=7, height=3, cursor="hand2", command=lambda:add_symbol("0"), bg="#B33F62", font="bold")
    zero.grid(column = 0, row = 4, padx=1.5, pady=1.5)

    # Operations Buttons
    add = tk.Button(bg, text = "+", width=7, height=3, cursor="hand2", command=lambda:add_symbol("+"), bg="#7B1E7A", font="bold")
    add.grid(column = 3, row = 1, padx=1.5, pady=1.5)

    sust = tk.Button(bg, text = "-", width=7, height=3, cursor="hand2", command=lambda:add_symbol("-"), bg="#7B1E7A", font="bold")
    sust.grid(column = 3, row = 2, padx=1.5, pady=1.5)

    mult = tk.Button(bg, text = "*", width=7, height=3, cursor="hand2", command=lambda:add_symbol("*"), bg="#7B1E7A", font="bold")
    mult.grid(column = 3, row = 3, padx=1.5, pady=1.5)

    div = tk.Button(bg, text = "/", width=7, height=3, cursor="hand2", command=lambda:add_symbol("/"), bg="#7B1E7A", font="bold")
    div.grid(column = 3, row = 4, padx=1.5, pady=1.5)
    
    point = tk.Button(bg, text = ".", width=7, height=3, cursor="hand2", command=lambda:add_symbol("."), bg="#7B1E7A", font="bold")
    point.grid(column = 1, row = 4, padx=1.5, pady=1.5)
    
    left_parent = tk.Button(bg, text = "(", width=7, height=3, cursor="hand2", command=lambda:add_symbol("("), bg="#7B1E7A", font="bold")
    left_parent.grid(column = 4, row = 1, padx=1.5, pady=1.5)
    
    right_parent = tk.Button(bg, text = ")", width=7, height=3, cursor="hand2", command=lambda:add_symbol(")"), bg="#7B1E7A", font="bold")
    right_parent.grid(column = 4, row = 2, padx=1.5, pady=1.5)
    
    power = tk.Button(bg, text = "^", width=7, height=3, cursor="hand2", command=lambda:add_symbol("**"), bg="#7B1E7A", font="bold")
    power.grid(column = 4, row = 3, padx=1.5, pady=1.5)
    
    sqrt = tk.Button(bg, text = "sqrt", width=7, height=3, cursor="hand2", command=lambda:add_symbol("sqrt("), bg="#7B1E7A", font="bold")
    sqrt.grid(column = 4, row = 4, padx=1.5, pady=1.5)

    # Functions Buttons
    clear = tk.Button(bg, text = "CLR", width=7, height=2, cursor="hand2", command=clear_button, bg="#F3C677", fg="#F00", font="bold")
    clear.grid(column = 4, row = 0, padx=1.5, pady=1.5)

    memory_button = tk.Button(bg, text = "ME", width=7, height=3, cursor="hand2", command=memory_store, bg="#F3C677", fg="#FFF", font="bold")
    memory_button.grid(column = 2, row = 4, padx=1.5, pady=1.5)

    # Execution Loop
    tk.mainloop()

if __name__ == '__main__':
    run()