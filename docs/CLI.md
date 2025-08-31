
# Gemini CLI Program Documentation

This document provides instructions on how to use the Gemini CLI program.

## Overview

The Gemini CLI program allows you to interact with the Gemini CLI in two ways:

1.  **Execute a pre-defined prompt:** You can choose from a list of pre-defined prompts located in the `src/domain/models` directory.
2.  **Execute a new prompt:** You can pass a new prompt as a command-line argument.

## Usage

To run the program, execute the `main.py` file from the root directory of the project:

```bash
python main.py
```

### Choosing a Pre-defined Prompt

If you run the program without any arguments, it will scan the `src/domain/models` directory for prompt files (ending with `.md`) and present you with a list of choices.

Example:

```
Please choose a prompt to execute:
1: etf_research.md
2: portfolio_dynamic_etf_blueprint.md
...
Enter the number of the prompt:
```

Enter the number corresponding to the prompt you want to execute, and the program will send the content of the file to the Gemini CLI.

### Passing a New Prompt

To execute a new prompt, use the `--prompt` argument followed by the prompt string.

Example:

```bash
python main.py --prompt "What is the capital of France?"
```

The program will then execute the provided prompt using the Gemini CLI.
