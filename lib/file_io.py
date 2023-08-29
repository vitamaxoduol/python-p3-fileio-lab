def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w") as f: # Open the file in write mode
        f.write(file_content) # Write the content to the file


def append_file(file_name, append_content):
    with open(f"{file_name}.txt", "a") as f:
        f.write(append_content)  # Write the new content at the end of the file
        
    

def read_file(file_name):
    with open(f"{file_name}.txt", "r") as f:
        content = f.read()
    return content



write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

read_file(file_name="logfile")