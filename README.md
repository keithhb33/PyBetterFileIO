<a name="readme-top"></a>


<br />
<div align="center">

  <h3 align="center">PyBetterFileIO</h3>

  <p align="center">A faster, more efficient Python file input and output framework</p>
</div>


<!-- TABLE OF CONTENTS -->

<h3>Table of Contents</h3>
<ol>
  <li>
    <a href="#about-the-project">About The Project</a>
  </li>
  <li>
    <a href="#installation">Installation</a></li>
  </li>
  <li>
    <a href="#usage">Usage</a>
  </li>
  <li>
    <a href="#making-a-file">Default Python vs. PyBetterFileIO</a>
  </li>
</ol>




<!-- ABOUT THE PROJECT -->
## About The Project

<p>PyBetterFileIO is the most intuitive, efficient, and accessible way to perform file input and output functions in python.
Designed to improve the syntax of Python's included libraries, PyBetterFileIO is an effective tool.
Create and edit files and folders, copy and move files and directories, and more.
Treat your files and directories like objects in Python.</p>




### Installation
```bash
pip install PyBetterFileIO
```

## Usage
```python
from PyBetterFileIO import *
```
## Functions and Implementation

<h2>File Commands</h2>

```python
new_file = file("new_file.txt") # Instantiate a file object (required!)
```
```python
new_file.make() # Make the file in the defined directory
new_file.create() # Create the file in the defined directory
```
```python
new_file.write("Hello World!") # Clears and writes to file's content
```
```python
new_file.append(" It's a beautiful day.") # Adds onto file's existing content
```
```python
new_file.replace("Hello World!", "Goodbye World!") # Finds and replaces file's content
```
```python
new_file.move_to("folder_or_path_to_move_to.optional") # Moves file to specified location
```
```python
new_file.rename("folder_to_move_to/old_file.txt") # Rename the file
```
```python
new_file.delete() # Delete the file
new_file.remove() # Remove the file
```
```python
new_file.copy("test_folder/fun_file.txt") # Copy file to parameter's location
new_file.copy_and_rename("test_folder/fun_file.txt") # Copy file to parameter's location
new_file.copy_to("test_folder/fun_file.txt") # Copy file to parameter's location
```
```python
new_file.read() # Returns file text content
```
```python
new_file.print() # Prints file text content
```
```python
new_file.exists() # Returns boolean if file exists
```
```python
new_file.get_filename() # Returns file's path
```
```python
new_file.get_default_file_object() # Returns a default file object allowing new_file to act as: with open(...) as new_file:
```
```python
new_file.get_custom_file_object() # Returns a PyBetterFileIO file object from a default object where default is from: with open(...) as new_file
```

<h2>Folder Commands</h2>

```python
new_folder = folder("new_folder") # Instantiate a folder object (required!)
```
```python
new_folder.make() # Make the file in the defined directory
new_folder.create() # Create the file in the defined directory
```
```python
new_folder.replace("not_needed_folder") # Replaces content of parameter's folder with object's content
```
```python
new_folder.rename("folder_to_move_to/old_file.txt") # Rename the file
```
```python
new_folder.delete() # Delete the file
new_folder.remove() # Remove the file
```
```python
new_folder.create_file("name_of_file.txt") # Create a file inside folder
new_folder.make_file("name_of_file.txt") # Make a file inside folder
```
```python
new_folder.copy_to("test_folder") # Copy folder to parameter's location
new_folder.copy_contents_to("test_folder") # Copy contents to parameter's location
```
```python
new_folder.move_to("test_folder") # Moves to parameter's location without keeping original directory
```
```python
new_folder.list() # Returns a list of all files in folder object
```
```python
new_folder.read() # Returns file text content
```
```python
new_folder.print() # Prints file text content
```
```python
new_folder.exists() # Returns boolean if folder exists
```
```python
new_folder.clear() # Clears folder content
```
```python
new_folder.get_foldername() # Returns file's path
```

<h4>Static Method</h4>

```python
Folder.clear_at("directory") # Clears specified directory
```

## Default Python vs. PyBetterFileIO
<h2 id="making-a-file">Making a File</h2>

<h3>Default Python</h3>

```python
with open("file.txt", 'w') as file:
  file.write()
```

<h3>PyBetterFileIO</h3>

```python
file("file.txt").make()
```

<h2>Writing to a file</h2>

<h3>Default Python</h3>

```python
with open("file.txt", "w") as file:
  file.write("Hello World!")
```

<h3>PyBetterFileIO</h3>

```python
file("file.txt").write("Hello World!")
```

<h2>Replacing text in a file</h2>

<h3>Default Python</h3>

```python
# Assume already existing file
with open('file.txt', 'r') as file:
  filedata = file.read()

filedata = filedata.replace('abcd', 'ram')

with open('file.txt', 'w') as file:
  file.write(filedata)
```

<h3>PyBetterFileIO</h3>

```python
file("file.txt").replace("abcd", "ram")
```

<h2>Copy Contents of a Folder</h2>

<h3>Default Python</h3>

```python
files = os.listdir("contents")
for file in files:
  shutil.copy(os.path.join("contents", file), os.path.join("other_content", "test_folder", file))
```

<h3>PyBetterFileIO</h3>

```python
folder("contents").copy_contents_to("other_content/test_folder")
```
