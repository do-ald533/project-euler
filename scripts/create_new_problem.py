import os

def generate_directory(directory_name):
  """Generates a new directory with one Python file in it and a Markdown file.

  Args:
    directory_name: The name of the new directory.
  """

  # Create the new directory
  os.mkdir(directory_name)

  # Create the Python file
  with open(os.path.join(directory_name, "main.py"), "w") as f:
    f.write("print('Hello, world!')")

  # Create the Markdown file
  with open(os.path.join(directory_name, "README.md"), "w") as f:
    f.write("# A simple Python script")
    f.write("\n\nThis is a simple Python script that prints 'Hello, world!' to the console.")

if __name__ == "__main__":
  # Get the name of the new directory from the user
  directory_name = input("Enter the name of the new directory: ")

  # Generate the new directory
  generate_directory(directory_name)

  # Print a message to the user
  print("The new directory has been created.")