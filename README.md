PatternScript Compiler 🎨

A custom domain-specific language (DSL) and compiler designed for algorithmic pattern generation, string manipulation, and logical control flow.

📖 Overview

PatternScript is a scripting language built from scratch using Python. It demonstrates the complete 6-phase compiler construction process, from Lexical Analysis to Code Generation.

Unlike general-purpose languages, PatternScript features a unique syntax optimized for visual patterns and flow control, including a custom IDE with syntax highlighting.

Key Features

🧵 The Stitch Operator (~): Seamlessly joins strings and numbers without type casting.

🏹 Unique Syntax: Uses note> for comments, : as a terminator, and -> for switch cases.

⚡ Built-in Optimization: Features a Constant Folding optimizer (Phase 5) to pre-calculate math operations.

🖥️ Custom GUI IDE: A dark-mode IDE with syntax highlighting, line numbers, and live output redirection.

📜 6-Phase Architecture: Implements Lexer, Recursive Descent Parser, Semantic Analysis, ICG (Three-Address Code), Optimizer, and Interpreter.

📸 Screenshots

The Custom IDE (GUI)

(Add a screenshot of your GUI here running the Triangle Pattern)

Intermediate Code Generation (TAC)

(Add a screenshot of the console showing the Yellow TAC output)

📂 Project Structure

PatternScript/
├── src/                # Source Code
│   ├── lexer.py        # Tokenizer (Regex-based)
│   ├── parser.py       # Recursive Descent Parser (AST Generation)
│   ├── icg.py          # Intermediate Code Generator (TAC)
│   ├── optimizer.py    # Constant Folding Optimizer
│   ├── interpreter.py  # Runtime Execution Engine
│   └── gui_pro.py      # Custom IDE (Tkinter)
│
├── tests/              # PatternScript Test Files (.ps)
│   ├── final_demo.ps   # Complex showcase script
│   └── ...
│
└── docs/               # Documentation & Artifacts
    └── Final_Report.pdf


🚀 Getting Started

Prerequisites

Python 3.x

Installation

Clone the repository:

git clone [https://github.com/YourUsername/PatternScript-Compiler.git](https://github.com/YourUsername/PatternScript-Compiler.git)


Navigate to the project folder:

cd PatternScript-Compiler


How to Run

Option 1: The GUI IDE (Recommended)

This launches the full IDE with syntax highlighting and file loading.

python src/gui_pro.py


Option 2: Command Line Interpreter

You can run .ps files directly from the terminal.

python src/interpreter.py tests/final_demo.ps


📝 Syntax Guide

1. Variables & Output

note> This is a comment
x = 10:
plot "The value is " ~ x:   note> Stitch operator joins them


2. Input

ask name:
plot "Hello " ~ name:


3. Loops (Range)

loop i in 1..5 {
    plot "*" * i:   note> 'Multiply' string to repeat it
}


4. Control Flow (Check & Choose)

check x > 5 {
    plot "High":
} else {
    plot "Low":
}

choose x {
    1 -> plot "One":
    2 -> plot "Two":
    default -> plot "Other":
}


🏗️ Compiler Architecture

Lexical Analysis: Tokenizes input using Regex (distinguishes note> vs >).

Syntax Analysis: Recursive Descent Parser builds an Abstract Syntax Tree (AST).

Semantic Analysis: Checks type compatibility and manages Variable Scope (Symbol Table).

Intermediate Code Generation (ICG): Converts AST to Quadruples (Three-Address Code).

Optimization: Performs Constant Folding (e.g., 5 + 3 * 2 -> 11 at compile time).

Code Generation: Interprets the optimized AST to execute logic.

👥 Authors

Taqwa Rasheed

Fatimah Ansari

Built for the Compiler Construction (CS-4031) Course Project.
