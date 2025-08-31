
import subprocess

class GeminiCLI:
    """
    A class to interact with the Gemini CLI.
    """

    def __init__(self):
        """
        Initializes the GeminiCLI class.
        """
        pass

    def execute_prompt(self, prompt):
        """
        Executes a prompt using the Gemini CLI.

        :param prompt: The prompt to execute.
        :return: The output from the Gemini CLI.
        """
        try:
            # Execute the gemini command with the given prompt
            result = subprocess.run(
                ["gemini", "-p", prompt],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except FileNotFoundError:
            return "Error: 'gemini' command not found. Please ensure it is installed and in your PATH."
        except subprocess.CalledProcessError as e:
            return f"Error executing Gemini CLI: {e.stderr}"

