import os
import shutil

class file:

    def __init__(self, filename):
        if "." not in filename:
            print("Please choose a file with an extension (.txt, .html, etc.)")
        if "." in filename:
            self.filename = filename
            self.edit = self.edit(self)

    def exists(self):
        try:
            return os.path.isfile(self.filename):
        except Exception as e:
            print(f"An error occured checking if {self.filename} exists")


    def rename(self, new_filename):
        try:
            os.rename(filename, new_filename)
            self.filename = new_filename
            return self
        except FileNotFoundError:
            print(f"File {self.filename} does not exist at that directory")
        except PermissionError:
            print(f"Permission denied renaming {self.filename}")
        except Exception as e:
            print(f"An error occured while renaming {self.filename}")

    def delete(self):
        try:
            os.remove(self.filename)
            self.filename = None
            return self
        except FileNotFoundError:
            print(f"File {self.filename} does not exist at that directory")
        except PermissionError:
            print(f"Permission denied deleting {self.filename}")
        except Exception as e:
            print(f"An error occured while deleting {self.filename}")

    def remove(self):
        try:
            os.remove(self.filename)
            self.filename = None
            return self
        except FileNotFoundError:
            print(f"File {self.filename} does not exist at that directory")
        except PermissionError:
            print(f"Permission denied removing {self.filename}")
        except Exception as e:
            print(f"An error occured while removing {self.filename}")

    def make(self):
        try:
            if os.path.isfile(self.filename):
                print(f"File {self.filename} already exists...continuing...")
                return self
            f = open(self.filename, 'w')
            f.close()
            return self
        except PermissionError:
            print(f"Permission denied while making {self.filename}")
        except Exception as e:
            print(f"An error occured while making {self.filename}")

    def create(self):
        try:
            f = open(self.filename, 'w')
            f.close()
            return self
        except PermissionError:
            print(f"Permission denied while creating {self.filename}")
        except Exception as e:
            print(f"An error occured while creating {self.filename}")

    def copy(self, new_filename):
        try:
            shutil.copy2(self.filename, new_filename)
            return self
        except FileNotFoundError:
            print(f"File {self.filename} does not exist at that directory")
        except PermissionError:
            print(f"Permission denied while copying {self.filename}")
        except Exception as e:
            print(f"An error occured while copying {self.filename} to {new_filename}")
            print("Enter a new directory, including the new name")

    def read(self):
        try:
            with open(self.filename, 'r', encoding="utf8") as file:
                return str(file.read())
        except FileNotFoundError:
            print(f"File {self.filename} does not exist at that directory")
        except PermissionError:
            print(f"Permission denied while reading {self.filename}")  
        except Exception as e:
            print(f"An error occurred while reading {self.filename}")

    def print(self):
        try:
            print(self.read())
            return self
        except FileNotFoundError:
            print(f"File {self.filename} does not exist at that directory")
        except PermissionError:
            print(f"Permission denied while printing {self.filename}")  
        except Exception as e:
            print(f"An error occurred while printing {self.filename}")

    def append(self, append_string):
        try:
            with open(self.filename, 'a') as file:
                file.write(append_string)
            return self
        except FileNotFoundError:
            print(f"File {self.filename} does not exist at that directory")
        except PermissionError:
            print(f"Permission denied while writing {append_string} to {self.filename}")
        except Exception as e:
            print(f"An error occurred while writing {append_string} to {self.filename}")

    def move(self, new_location):
        try:
            shutil.move(self.filename, new_location)
            self.filename = new_location
            return self
        except FileNotFoundError:
            print(f"File {self.filename} does not exist at that directory")
        except PermissionError:
            print(f"Permission denied while moving {self.filename} to {new_location}")
        except Exception as e:
            print(f"An error occurred while writing {self.filename} to {new_location}")


    def write(self, write_string):
        try:
            self.edit.clear()
            self.edit.append(write_string)
            return self
        except FileNotFoundError:
            print(f"File {self.filename} does not exist at that directory")
        except PermissionError:
            print(f"Permission denied while writing {self.filename}")
        except Exception as e:
            print(f"An error occurred while writing {self.filename}")

    def replace(self, first_string, second_string, occurences=0):
            try:
                with open(self.filename, 'r') as file:
                    data = file.read()
                    if occurences != 0 or occurences < 0:
                        data = data.replace(first_string, second_string, occurences)
                    else:
                        while first_string in data:
                            data = data.replace(first_string, second_string)
                    with open(self.filename, 'w') as file:
                        file.write(data)
                return self
            except FileNotFoundError:
                print(f"File {self.filename} does not exist at that directory")
            except PermissionError:
                print(f"Permission denied while replacing {first_string} with {second_string} in {self.filename}")
            except Exception as e:
                print(f"An error occurred while replacing {first_string} with {second_string} in {self.filename}")

    def get_filename(self):
        return self.filename

    #def set_filename(self, new_filename):
    #    try:
    #        self.filename = new_filename
    #        return self
    #    except Exception as e:
    #        print(f"An error occured while setting filename to {new_filename}")")

    def copy_and_rename(self, new_file_name):
        shutil.copyfile(self.filename, new_file_name)
        return self

    def copyAndRename(self, newFileName):
        shutil.copyfile(self.filename, newFileName)
        return self


    class edit:
        def __init__(self, outer_instance):
            self.outer_instance = outer_instance

        def replace(self, first_string, second_string, occurences=0):
            try:
                with open(self.outer_instance.filename, 'r') as file:
                    data = file.read()
                    if occurences != 0 or occurences < 0:
                        data = data.replace(first_string, second_string, occurences)
                    else:
                        while first_string in data:
                            data = data.replace(first_string, second_string)
                    with open(self.outer_instance.filename, 'w') as file:
                        file.write(data)
                return self.outer_instance
            except FileNotFoundError:
                print(f"File {self.outer_instance.filename} does not exist at that directory")
            except PermissionError:
                print(f"Permission denied while replacing {first_string} with {second_string} in {self.outer_instance.filename}")
            except Exception as e:
                print(f"An error occurred while replacing {first_string} with {second_string} in {self.outer_instance.filename}")

        def append(self, append_string):
            try:
                with open(self.outer_instance.filename, 'a') as file:
                    file.write(append_string)
                return self.outer_instance
            except FileNotFoundError:
                print(f"File {self.outer_instance.filename} does not exist at that directory")
            except PermissionError:
                print(f"Permission denied while writing {append_string} to {self.outer_instance.filename}")
            except Exception as e:
                print(f"An error occurred while writing {append_string} to {self.outer_instance.filename}")

        def clear(self):
            try:
                open(self.outer_instance.filename, 'w').close()
                return self.outer_instance
            except FileNotFoundError:
                print(f"File {self.outer_instance.filename} does not exist at that directory")
            except PermissionError:
                print(f"Permission denied while clearing {self.outer_instance.filename}")
            except Exception as e:
                print(f"An error occurred while clearing {self.outer_instance.filename}")

        def write(self, write_string):
            try:
                self.clear()
                self.append(write_string)
                return self.outer_instance
            except FileNotFoundError:
                print(f"File {self.outer_instance.filename} does not exist at that directory")
            except PermissionError:
                print(f"Permission denied while writing {self.outer_instance.filename}")
            except Exception as e:
                print(f"An error occurred while writing {self.outer_instance.filename}")

        def copy_and_rename(self, new_file_name):
            shutil.copyfile(self.outerinstance.filename, new_file_name)
            return self.outer_instance

        def copyAndRename(self, newFileName):
            shutil.copyfile(self.outerinstance.filename, newFileName)
            return self.outer_instance

            
            


    