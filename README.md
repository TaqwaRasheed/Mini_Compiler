

# 🌟 **PatternScript Compiler — A Custom DSL for Patterns & Logic**

A fully hand-built **Domain-Specific Language (DSL)** and compiler pipeline written in Python, designed for algorithmic pattern generation, string manipulation, and control flow. Includes a custom GUI IDE with syntax highlighting.


## 🚀 **Overview**

**PatternScript** is a scripting language built from scratch using Python. It demonstrates the complete 6-phase compiler construction process, from Lexical Analysis to Code Generation.

Unlike general-purpose languages, **PatternScript** features a unique syntax optimized for visual patterns and flow control, including a custom IDE with syntax highlighting.


## ✨ **Key Features**

### 🧵 **Stitch Operator (`~`)**

Seamlessly joins strings and numbers **without casting**.
Example:

```
plot "Value: " ~ 5:
```

### 🎯 **Unique Syntax**

* `note>` → Comments
* `:` → Statement terminator
* `->` → Case arrow
* `loop i in 1..5 { ... }` → Clean, Python-like looping

### ⚡ **Built-in Optimizer**

* Constant folding for mathematical simplification
* Example: `3 * 5 + 2` compiles directly to `17`

### 🖥️ **Custom Dark-Mode IDE**

Featuring:

* Syntax highlighting
* Line numbers
* Run button
* Auto output redirection

### 🧩 **Complete Compiler Design**

Implements the full compiler pipeline the way real compilers do it.


## 📂 **Project Structure**

```
PatternScript/
├── src/                
│   ├── lexer.py        # Regex-based tokenizer
│   ├── parser.py       # Recursive Descent parser → AST
│   ├── icg.py          # TAC (Three-Address Code) generator
│   ├── optimizer.py    # Constant Folding
│   ├── interpreter.py  # Final code execution engine
│   └── gui_pro.py      # Custom IDE (Tkinter)
│
├── tests/
│   ├── test1.ps   
│   └── ...
│
└── docs/
    └── Final_Report.pdf
```

---

## 🧁 **Getting Started**

### **Prerequisites**

* Python 3.x


## 📥 **Installation**

Clone the repo:

```bash
git clone https://github.com/YourUsername/PatternScript-Compiler.git
cd PatternScript-Compiler
```


## ▶️ **How to Run**

### **Option 1 — GUI IDE (Recommended)**

```bash
python src/gui_pro.py
```

### **Option 2 — Run a PatternScript File**

```bash
python src/interpreter.py tests/test1.ps
```


## 📝 **PatternScript Syntax Guide**

### 1. **Variables & Output**

```text
note> This is a comment
x = 10:
plot "Value: " ~ x:
```

### 2. **Input**

```text
ask name:
plot "Hello " ~ name:
```

### 3. **Loops**

```text
loop i in 1..5 {
    plot "*" * i:
}
```

### 4. **Control Flow**

#### `check` (if/else)

```text
check x > 5 {
    plot "High":
} else {
    plot "Low":
}
```

#### `choose` (switch)

```text
choose x {
    1 -> plot "One":
    2 -> plot "Two":
    default -> plot "Other":
}
```


## 🧠 **Compiler Architecture**

### Phase 1: **Lexical Analysis**

Regex-based scanner with priority matching to handle `>` vs `note>`.

### Phase 2: **Syntax Analysis**

Recursive Descent Parser builds a clean Abstract Syntax Tree (AST).

### Phase 3: **Semantic Analysis**

* Type checking rules
* String/Number coercions
* Symbol table for scopes

### Phase 4: **ICG (Intermediate Code Generation)**

Produces **quadruples** like:

```
t1 = 3 * 5
t2 = t1 + 2
x = t2
```

### Phase 5: **Optimization**

Constant folding: pre-evaluates expressions during compilation.

### Phase 6: **Code Generation**

Final interpreter executes optimized TAC.


## 👥 **Authors**

* **Taqwa Rasheed**
* **Fatimah Ansari**

Built for the **Compiler Construction (CS-4031)** course project.



