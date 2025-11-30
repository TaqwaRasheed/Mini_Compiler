import tkinter as tk
from tkinter import scrolledtext, simpledialog, filedialog
import sys
import io
import re

# Import your compiler logic
from Parser import parse
from optimizer import Optimizer
from interpreter import Interpreter
from icg import TACGenerator

# ==========================================
# 1. SYNTAX HIGHLIGHTING CONFIG
# ==========================================
# Colors inspired by VS Code Dark+
COLORS = {
    "bg": "#1e1e1e",
    "fg": "#d4d4d4",
    "keyword": "#569cd6",    # Blue
    "string": "#ce9178",     # Orange/Brown
    "number": "#b5cea8",     # Light Green
    "comment": "#6a9955",    # Dark Green
    "operator": "#d4d4d4",   # White
    "function": "#dcdcaa"    # Yellow
}

# Regex patterns for highlighting
PATTERNS = [
    (r'\b(loop|check|else|choose|default|in)\b', "keyword"),
    (r'\b(plot|ask)\b', "function"),
    (r'".*?"', "string"),
    (r'\b\d+\b', "number"),
    (r'note>.*', "comment"),
    (r'->|~', "operator")
]

# ==========================================
# 2. CUSTOM INTERPRETER (POPUP INPUT)
# ==========================================
class GuiInterpreter(Interpreter):
    def visit_Ask(self, node):
        value = simpledialog.askstring("Input Request", f"Script is asking for: '{node.name}'")
        if value is None: value = "" 
        try:
            self.variables[node.name] = int(value)
        except ValueError:
            self.variables[node.name] = value

# ==========================================
# 3. THE PRO IDE APPLICATION
# ==========================================
class PatternScriptIDE:
    def __init__(self, root):
        self.root = root
        self.root.title("PatternScript Studio")
        self.root.geometry("1100x700")
        self.root.configure(bg="#333333")

        # --- Toolbar ---
        toolbar = tk.Frame(root, bg="#252526", height=40)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.create_button(toolbar, "📂 LOAD", self.load_file, "#007acc")
        self.create_button(toolbar, "▶ RUN", self.run_code, "#4CAF50")
        self.create_button(toolbar, "🧹 CLEAR", self.clear_output, "#e51400")

        # --- Main Layout ---
        # PanedWindow allows dragging the divider between Code and Output
        paned = tk.PanedWindow(root, orient=tk.HORIZONTAL, bg="#333333", sashwidth=5)
        paned.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # 1. Editor Area (Left)
        editor_frame = tk.Frame(paned, bg=COLORS["bg"])
        
        self.line_numbers = tk.Text(editor_frame, width=4, padx=5, takefocus=0, border=0,
                                    bg="#1e1e1e", fg="#858585", state='disabled', font=("Consolas", 12))
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        self.editor = scrolledtext.ScrolledText(editor_frame, wrap=tk.NONE, border=0,
                                                bg=COLORS["bg"], fg=COLORS["fg"], 
                                                font=("Consolas", 12), insertbackground="white")
        self.editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Bind typing events to update line numbers and highlighting
        self.editor.bind("<<Change>>", self.on_content_changed)
        self.editor.bind("<KeyRelease>", self.on_key_release)
        
        paned.add(editor_frame, width=600)

        # 2. Console Area (Right)
        console_frame = tk.Frame(paned, bg="black")
        self.console = scrolledtext.ScrolledText(console_frame, wrap=tk.WORD, border=0,
                                                 bg="#1e1e1e", fg="#cccccc", 
                                                 font=("Consolas", 11), state='disabled')
        self.console.pack(fill=tk.BOTH, expand=True)
        paned.add(console_frame)

        # Define Colors Tags
        for tag, color in COLORS.items():
            self.editor.tag_config(tag, foreground=color)

        self.console.tag_config("info", foreground="#569cd6")     # Blue
        self.console.tag_config("success", foreground="#6a9955")  # Green
        self.console.tag_config("error", foreground="#f44747")    # Red
        self.console.tag_config("tac", foreground="#dcdcaa")      # Yellow

        # Load Default Code
        self.editor.insert(tk.END, """note> PatternScript Demo
ask name:
plot "Hello " ~ name:

loop i in 1..5 {
    check i > 2 {
        plot "Number " ~ i:
    }
}
""")
        self.update_line_numbers()
        self.highlight_syntax()

    def create_button(self, parent, text, cmd, color):
        btn = tk.Button(parent, text=text, command=cmd, bg=color, fg="white", 
                        font=("Segoe UI", 9, "bold"), relief=tk.FLAT, padx=15, pady=5)
        btn.pack(side=tk.LEFT, padx=5, pady=5)

    def load_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("PatternScript Files", "*.ps"), ("All Files", "*.*")])
        if not filepath: return
        with open(filepath, "r") as f:
            code = f.read()
        self.editor.delete(1.0, tk.END)
        self.editor.insert(tk.END, code)
        self.highlight_syntax()
        self.update_line_numbers()

    def on_key_release(self, event=None):
        self.update_line_numbers()
        self.highlight_syntax()

    def on_content_changed(self, event=None):
        self.update_line_numbers()

    def update_line_numbers(self):
        code = self.editor.get(1.0, tk.END)
        lines = code.count("\n") 
        if lines == 0: lines = 1
        
        line_num_content = "\n".join(str(i) for i in range(1, lines + 1))
        
        self.line_numbers.config(state='normal')
        self.line_numbers.delete(1.0, tk.END)
        self.line_numbers.insert(1.0, line_num_content)
        self.line_numbers.config(state='disabled')
        
        # Sync scrolling
        # (Basic sync, for advanced sync we need YView hooking)

    def highlight_syntax(self):
        code = self.editor.get(1.0, tk.END)
        
        # Remove old tags
        for tag in COLORS.keys():
            self.editor.tag_remove(tag, 1.0, tk.END)
            
        # Apply new tags
        for pattern, tag in PATTERNS:
            for match in re.finditer(pattern, code):
                start = f"1.0 + {match.start()} chars"
                end = f"1.0 + {match.end()} chars"
                self.editor.tag_add(tag, start, end)

    def clear_output(self):
        self.console.config(state='normal')
        self.console.delete(1.0, tk.END)
        self.console.config(state='disabled')

    def run_code(self):
        code = self.editor.get(1.0, tk.END)
        self.clear_output()
        self.console.config(state='normal')
        
        old_stdout = sys.stdout
        redirected_output = io.StringIO()
        sys.stdout = redirected_output

        try:
            self.console.insert(tk.END, "[Compiling...]\n", "info")
            
            # Phase 1 & 2
            ast = parse(code)

            # Phase 4 (Display TAC)
            self.console.insert(tk.END, "[Phase 4: Intermediate Code]\n", "tac")
            icg = TACGenerator()
            tac = icg.generate(ast)
            for line in tac:
                self.console.insert(tk.END, f"  {line}\n", "tac")
            self.console.insert(tk.END, "-"*30 + "\n", "info")

            # Phase 5
            optimizer = Optimizer()
            ast = optimizer.optimize(ast)

            # Phase 6
            interpreter = GuiInterpreter()
            for stmt in ast:
                interpreter.visit(stmt)
            
            output_text = redirected_output.getvalue()
            self.console.insert(tk.END, output_text)
            self.console.insert(tk.END, "\n[Finished]", "success")

        except Exception as e:
            self.console.insert(tk.END, f"\nError: {e}", "error")
        
        finally:
            sys.stdout = old_stdout
            self.console.see(tk.END)
            self.console.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = PatternScriptIDE(root)
    root.mainloop()