import os

def demonstrate_os_functions():
    outputs = {}

    # Get the current working directory
    current_directory = os.getcwd()
    print(f"Current Directory: {current_directory}")

    # List all files and directories in the current directory
    outputs['files_and_directories'] = os.listdir(current_directory)
    print("\nFiles and Directories:")
    for item in outputs['files_and_directories']:
        print(item)

    # Get the PATH environment variable
    outputs['path_value'] = os.environ.get('PATH')
    print("\nPATH Environment Variable:")
    print(outputs['path_value'])

if __name__ == "__main__":
    demonstrate_os_functions()