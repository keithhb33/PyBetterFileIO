import os
import shutil
from pathlib import Path

class folder:

    def __init__(self, foldername):
        if "." not in foldername:
            self.foldername = foldername
        if "." in foldername:
            print("Please choose a folder/directory instead of a file with an extension (.txt, .html, etc.)")

    def rename(self, new_foldername):
        try:
            if os.path.isdir(new_foldername):
                os.rmdir(new_foldername)
            os.rename(self.foldername, new_foldername)
            if os.path.isdir(self.foldername):
                path = Path(self.foldername)
                path.rename(new_foldername)
            print(f"Renamed {self.foldername} to {new_foldername}")
            self.foldername = new_foldername
            return self
        except FileNotFoundError:
            print(f"Folder/directory {self.foldername} does not exist at that location")
        except PermissionError:
            print(f"Permission denied renaming {self.foldername}")
        except Exception as e:
            print(f"An error occured while renaming {self.foldername}")

    def delete(self):
        try:
            if os.path.isdir(self.foldername):
                if len(self.foldername) > 0:
                    self.clear()
                os.rmdir(self.foldername)
            self.foldername = self.get_foldername()
            return self.foldername
        except FileNotFoundError:
            print(f"Folder/directory {self.foldername} does not exist at that location")
        except PermissionError:
            print(f"Permission denied deleting {self.foldername}")
        except Exception as e:
            print(f"An error occured while deleting {self.foldername}")

    def remove(self):
        try:
            if os.path.isdir(self.get_foldername()):
                if len(self.get_foldername()) > 0:
                    self.clear()
                os.rmdir(self.get_foldername())
            self.foldername = self.get_foldername()
            return self.foldername
        except FileNotFoundError:
            print(f"Folder/directory {self.foldername} does not exist at that location")
        except PermissionError:
            print(f"Permission denied removing {self.foldername}")
        except Exception as e:
            print(f"An error occured while removing {self.foldername}")

    def make(self):
        try:
            if os.path.isdir(self.foldername):
                print(f"Folder/directory {self.foldername} already exists...continuing...")
                return self
            os.makedirs(self.foldername)
            return self
        except PermissionError:
            print(f"Permission denied while making {self.foldername}")
        except Exception as e:
            print(f"An error occured while making {self.foldername}")

    def create(self):
        try:
            if os.path.isdir(self.foldername):
                print(f"Folder/directory {self.foldername} already exists...continuing...")
                return self
            os.makedirs(self.foldername)
            return self
        except PermissionError:
            print(f"Permission denied while creating {self.foldername}")
        except Exception as e:
            print(f"An error occured while creating {self.foldername}")

    def copy_to(self, new_foldername):
        try:
            if not os.path.isdir(new_foldername):
                print("That path does not exist. Create a folder/directory to that path before copying")
                return self
            print(new_foldername)
            src_files = os.listdir(self.foldername) 
            for file_name in src_files: 
                full_file_name = os.path.join(src, file_name) 
                if os.path.isfile(full_file_name): 
                    shutil.copy(full_file_name, dest) 
            return self
        except FileNotFoundError:
            print(f"Folder/directory {self.foldername} does not exist at that directory")
        except PermissionError:
            print(f"Permission denied while copying {self.foldername}")
        except Exception as e:
            print(f"An error occured while copying {self.foldername} to {new_foldername}")
            print("Enter a new directory, including the new name")

    def copyTo(self, new_foldername):
        try:
            if not os.path.isdir(new_foldername):
                print("That path does not exist. Create a folder/directory to that path before copying")
                return self
            shutil.copytree(self.foldername, new_foldername)
            return self
        except FileNotFoundError:
            print(f"Folder/directory {self.foldername} does not exist at that directory")
        except PermissionError:
            print(f"Permission denied while copying {self.foldername}")
        except Exception as e:
            print(f"An error occured while copying {self.foldername} to {new_foldername}")
            print("Enter a new directory, including the new name")

    def list(self):
        try:
            listed_files = os.listdir(self.foldername)
            for item in listed_files:
                print(item)
            return listed_files
        except FileNotFoundError:
            print(f"Folder/directory {self.foldername} does not exist at that location")
        except PermissionError:
            print(f"Permission denied while listing {self.foldername}")  
        except Exception as e:
            print(f"An error occurred while listing {self.foldername}")     

    def replace(self, folder_to_replace):
        try:
            folder(folder_to_replace).delete()
            self.copy(folder_to_replace)
            self.foldername = folder_to_replace
            return self
        except FileNotFoundError:
            print(f"Folder/directory {folder_to_replace} does not exist to replace at that location")
        except PermissionError:
            print(f"Permission denied while replacing {folder_to_replace} with {self.foldername}")
        except Exception as e:
            print(f"An error occurred while replacing {folder_to_replace} with {self.foldername}")

    def clear(self):
        try:
            clear_dir = self.foldername()
            if os.path.isdir(clear_dir):
                if len(os.listdir(clear_dir)) == 0:
                    return self

            files = os.listdir(clear_dir)
            for file in files:
                file_path = os.path.join(clear_dir, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                if os.path.isdir(file_path):
                    os.rmdir(file_path)
            return self
            

        except FileNotFoundError:
            print(f"Folder/directory {clear_dir} does not exist")
        except PermissionError:
            print(f"Permission denied while clearing {clear_dir}")
        except Exception as e:
            print(f"An error occurred while clearing {clear_dir}")
                
    @staticmethod
    def clear_at(clear_dir):
        try:
            if os.path.isdir(clear_dir):
                if len(os.listdir(clear_dir)) == 0:
                    return self

            files = os.listdir(clear_dir)
            for file in files:
                file_path = os.path.join(clear_dir, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                if os.path.isdir(file_path):
                    os.rmdir(file_path)
            
        except FileNotFoundError:
            print(f"Folder/directory {clear_dir} does not exist")
        except PermissionError:
            print(f"Permission denied while clearing {clear_dir}")
        except Exception as e:
            print(f"An error occurred while clearing {clear_dir}")
    

    def make_file(self, filename):
        try:
            f = open(f"{self.foldername}/{filename}", 'w')
            f.close()
            return self
        except FileNotFoundError:
            print(f"Folder/directory {self.foldername} does not exist")
        except PermissionError:
            print(f"Permission denied while making {filename}")
        except Exception as e:
            print(f"An error occurred while making {filename}")

    def create_file(self, filename):
        try:
            f = open(self.foldername + filename, 'w')
            f.close()
            return self
        except FileNotFoundError:
            print(f"Folder/directory {self.foldername} does not exist")
        except PermissionError:
            print(f"Permission denied while making {filename}")
        except Exception as e:
            print(f"An error occurred while making {filename}")

    def get_foldername(self):
        try:
            if os.path.isdir(self.foldername):
                return self.foldername
            else:
                if "/" in self.foldername:
                    folder = self.foldername.split("/")
                elif "\\" in self.foldername:
                    folder = self.foldername.split("\\")
                dir_str = ""
                for i, ele in enumerate(folder):
                    dir_str += folder[i]
                    if not os.path.isdir(dir_str):
                        dir_str = dir_str.replace(folder[i], "")
                        self.foldername = dir_str
                        break
                return self.foldername
        except Exception as e:
            print("An error occured when trying to retrieve folder name.")

    def set_foldername(self, new_foldername):
        try:
            self.foldername = new_foldername
        except Exception as e:
            print(f"An error occured while setting foldername to {new_foldername}")
            




            
            


    