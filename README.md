<a name="readme-top"></a>


<br />
<div align="center">

  <h3 align="center">PyBetterFileIO</h3>

  <p align="center">A faster, more efficient Python file input and output framework</p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
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
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<p>PyBetterFileIO is the most intuitive, efficient, and accessible way to perform file input and output functions in python.
Designed to improve the syntax of Python's included libraries, PyBetterFileIO is an effective tool.
Create and edit files and folders, copy and move files and directories, and more.
Treat your files and directories like objects in Python.</p>




### Installation

1. pip install PyBetterFileIO


## Usage

from PyBetterFileIO import *

## Functions and Implementation

<h2>File Commands</h2>

new_file = file("new_file.txt") # Instantiate a file object (required!)

new_file.make() # Make the file in the defined directory\
new_file.create() # Create the file in the defined directory

new_file.write("Hello World!") # Clears and writes to file's content

new_file.append(" It's a beautiful day.") # Adds onto file's existing content

new_file.replace("Hello World!", "Goodbye World!") # Finds and replaces file's content

new_file.move_to("folder_to_move_to") # Moves file to specified folder

new_file.rename("folder_to_move_to/old_file.txt") # Rename the file

new_file.delete() # Delete the file\
new_file.remove() # Remove the file

new_file.copy("test_folder/fun_file.txt") # Copy file to parameter's location\
new_file.copy_and_rename("test_folder/fun_file.txt") # Copy file to parameter's location
new_file.copy_to("test_folder/fun_file.txt") # Copy file to parameter's location

new_file.read() # Returns file text content

new_file.print() # Prints file text content

new_file.exists() # Returns boolean if file exists

new_file.get_filename() # Returns file's path


<h2>Folder Commands</h2>

new_folder = folder("new_folder") # Instantiate a folder object (required!)

new_folder.make() # Make the file in the defined directory\
new_folder.create() # Create the file in the defined directory

new_folder.replace("not_needed_folder") # Replaces content of parameter's folder with object's content

new_folder.rename("folder_to_move_to/old_file.txt") # Rename the file

new_folder.delete() # Delete the file\
new_folder.remove() # Remove the file

new_folder.create_file("name_of_file.txt") # Create a file inside folder\
new_folder.make_file("name_of_file.txt") # Make a file inside folder

new_folder.copy_to("test_folder/fun_file.txt") # Copy file to parameter's location\
new_folder.copy_contents_to("test_folder") # Copy contents to parameter's location

new_folder.move_to("test_folder) # Moves to parameter's location without keeping original directory

new_folder.list() # Returns a list of all files in folder object

new_folder.read() # Returns file text content

new_folder.print() # Prints file text content

new_folder.exists() # Returns boolean if folder exists

new_folder.clear() # Clears folder content

new_folder.get_foldername() # Returns file's path

<h5>Static Method</h5>
Folder.clear_at("directory") # Clears specified directory



