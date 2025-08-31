
import argparse
import os
from cli.gemini_cli import GeminiCLI

def main():
    """
    Main function to run the Gemini CLI program.
    """
    parser = argparse.ArgumentParser(description="Gemini CLI Program")
    parser.add_argument("--prompt", type=str, help="A new prompt to execute.")
    args = parser.parse_args()

    gemini_cli = GeminiCLI()

    if args.prompt:
        # If a prompt is provided as an argument, execute it
        print("Executing the provided prompt...")
        output = gemini_cli.execute_prompt(args.prompt)
        print(output)
        return 0

    # If no prompt is provided, scan for existing prompts
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    prompts_dir = os.path.join(project_root, "src/domain/models")
    try:
        prompt_files = [f for f in os.listdir(prompts_dir) if f.endswith(".md")]
    except FileNotFoundError:
        print(f"Error: The directory '{prompts_dir}' was not found.")
        return 1

    if not prompt_files:
        print(f"No prompt files found in '{prompts_dir}'.")
        return 0

    print("Please choose a prompt to execute:")
    for i, file_name in enumerate(prompt_files):
        print(f"{i + 1}: {file_name}")

    try:
        choice = int(input("Enter the number of the prompt: ")) - 1
        if 0 <= choice < len(prompt_files):
            chosen_file = prompt_files[choice]
            with open(os.path.join(prompts_dir, chosen_file), "r") as f:
                prompt_content = f.read()
            print(f"Executing prompt from '{chosen_file}'...")
            output = gemini_cli.execute_prompt(prompt_content)
            print(output)
        else:
            print("Invalid choice.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number from the list.")
    
    return 0

if __name__ == "__main__":
    main()
