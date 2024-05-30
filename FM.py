import os
import logging
import datetime
from pathlib import Path
import pyfiglet
import shutil

# Configure logging
logging.basicConfig(filename='filemanager.log', level=logging.INFO)



def organize(directory):
    f_types = {
        'Python Script': '.py',
        'Text Files': '.txt',
        'CSV Files': '.csv',
        'JSON Files': '.json',
        'XML Files': '.xml',
        'YAML Files': '.yaml',
        'Excel Files': ['.xlsx', '.xls'],
        'SQLite Databases': '.db',
        'HDF5 Files': '.h5',
        'Pickle Files': '.pkl',
        'Parquet Files': '.parquet',
        'Avro Files': '.avro',
        'Feather Files': '.feather',
        'Protobuf Files': '.proto',
        'Msgpack Files': '.msgpack',
        'Binary Files': '.bin',
        'Image Files': ['.png', '.jpg','jpeg', '.gif'],
        'Audio Files': ['.wav', '.mp3', '.ogg'],
        'Video Files': ['.mp4', '.avi', '.mov'],
        'PDF Files': '.pdf',
        'Word Files': '.docx',
        'PowerPoint Files': '.pptx',
        'HTML Files': '.html',
        'Markdown Files': '.md',
        'Configuration Files': ['.ini', '.cfg', '.conf'],
        'C and C++ Files': ['.c', '.cpp'],
        'MSWORD Files': '.docx',
        'Executable Files': '.exe',
        'Log Files': '.log',
        'CSS Files':'.css'


    }#when you organize your files you will create folder using the keys from this dictionary 
    try:
        directory_files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
        logging.info(f'Reading directory {directory} files')
        extensions = list(set([file.split('.')[-1] for file in directory_files  ]))
        for file_extension in extensions:
            if '.' + file_extension in f_types.values() or any('.' + file_extension in value for value in f_types.values() if isinstance(value, list)):
                foldernames = [key for key, value in f_types.items() if '.' + file_extension == value or ('.' + file_extension in value and isinstance(value, list))]
                for folder in foldernames:
                    folder_path = os.path.join(directory, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                        logging.info(f'Created folder: {folder_path}')
                    else:
                        logging.info(f'Folder {folder} already exists in {directory}')
        
        for file in directory_files:
            file_extension = file.split('.')[-1]
            if any(f'.{file_extension}' in ext for ext in f_types.values()):
                folder_names = [key for key, value in f_types.items() if f'.{file_extension}' == value or (isinstance(value, list) and f'.{file_extension}' in value)]
                for folder in folder_names:
                    folder_path = os.path.join(directory, folder)
                    src_path = Path(os.path.join(directory, file))
                    dest_path = Path(os.path.join(folder_path, file))
                    try:
                        src_path.rename(dest_path)
                        logging.info(f'Moved {file} to {folder_path}')
                        print(f'\nMoved {file} to {folder_path}\n')
                    except Exception as e:
                        logging.error(f'Error moving file {file}: {e}')
                        print(f'\nError moving file {file}: {e}\n')
                        continue
    except PermissionError as e:
        logging.error(f'Permission error: {e}. File is in use and cannot be moved.')
    except FileNotFoundError as e:
        logging.error(f'File not found error: {e}.')
    except Exception as e:
        logging.error(f'Error: {e}')


def display(directory):
    try: 
        while True:
            folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]
            
            for index in range(len(folders)): 
                print(f"{index}. {folders[index]}")
            print(f"{len(folders)}. exit")
            f = input("select the folder \n=>")
            
            for i in range(len(folders)): 
                if f == str(i):
                    folder_path = os.path.join(directory, folders[i])
                    if len(os.listdir(folder_path)) != 0:
                        print(f"\n{os.listdir(folder_path)}\n")
                    else:
                        print(f"{folders[i]} is empty\n")
                        logging.info(f"{folders[i]} is empty")
                        
            if f == str(len(folders)): 
                print("exiting\n")
                break
            
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e: 
        print(f"Exception: {e}")
def F_create():
    try : 
        while True: 
            print("1. Create\n2. exit\n")
            ans = int(input("enter number\n=>"))
            if ans == 1: 
                filename = input("enter a name for file (example: main.py or file.txt.. write extension too)\n=>")
                f =  open(filename,"x")
                print(f"\n{filename} has been created\n")
                logging.info(f"{filename} has been created\n")
            elif ans == 2: 
                print(f"exiting\n")
                break
            else : 
                print("enter proper value\n")
    except ValueError as e :
        print(f"{e}")
    except FileExistsError as e: 
        print(f"{e}")
    except Exception as e: 
        print(f"{e}")
def F_delete(directory):
    try: 
        files = [file for file in os.listdir(directory) if os.path.isfile(file) ]
        for index in range(len(files)): 
            print(f"{index}. {files[index]}")
        print(f"{len(files)}. exit")
        while True:
            ans = input("enter which file you want to delete(index)\n=>")
            for i in range(len(files)):
                if ans == str(i):
                    print(f"\n{files[i]} has been deleted\n")
                    os.remove(os.path.join(directory,files[i]))   
                    logging.info(f"{files[i]} has been deleted\n")      
            if ans == str(len(files)): 
                print("exiting\n")
                break
            else : 
                print(f"index {ans} not found")
    except ValueError as e :
        print(f"{e}")
    except Exception as e: 
        print(f"{e}")
def F_remove(directory):
    try: 
        folders = [folder for folder in os.listdir(directory) if os.path.isdir(folder) ]
        for index in range(len(folders)): 
            print(f"{index}. {folders[index]}")
        print(f"{len(folders)}. exit")
        while True:
            ans = input("enter which folder you want to delete(index)\n=>")
            for i in range(len(folders)):
                if ans == str(i):
                    print(f"\n{folders[i]} has been deleted\n")
                    shutil.rmtree(os.path.join(directory,folders[i]))
                    logging.info(f"{folders[i]} has been deleted\n")         
            if ans == str(len(folders)): 
                print("exiting\n")
                break
            else : 
                print(f"index {ans} not found")
    except ValueError as e :
        print(f"{e}")
    except Exception as e: 
        print(f"{e}")
def F_display(directory):
    try :
        fanfol = [f for f in os.listdir(directory)]
        for i in range(len(fanfol)): 
            if os.path.isfile(fanfol[i]):
                print(f"{i}. {fanfol[i]} (file)")
            else : 
                print(f"{i}. {fanfol[i]} (folder)")
        print("\n")
    except FileNotFoundError as e : 
        print(f'{e}')
    except Exception as e : 
        print(f"{e}")
def F_rename(directory):
    try: 
        fanfol = [f for f in os.listdir(directory)]
        for i in range(len(fanfol)): 
            print(f"{i}. {fanfol[i]}")
        print(f"{len(fanfol)}. exit")
        ans = input("enter which file or folder you want to rename\n=>")
        for i in range(len(fanfol)): 
            if os.path.isfile(fanfol[i]):
                print(f"{i}. {fanfol[i]} (file)")
            else : 
                print(f"{i}. {fanfol[i]} (folder)")
        print("\n")
        for i in range(len(fanfol)): 
            if str(i) == ans: 
                name = input(f"Write new for name {fanfol[i]} with its extension\n=>")
                if not os.path.isfile(os.path.join(directory,name)):
                    os.rename(os.path.join(directory,fanfol[i]),os.path.join(directory,name))
                    print(f"\n{fanfol[i]} has been renamed to {name}\n")
                    logging.info(f"{fanfol[i]} has been renamed to {name}\n")
                else : 
                    print(f"\n{name} exits")
            elif ans == str(len(fanfol)): 
                print("exiting \n")
                break
            
    except FileNotFoundError as e : 
        print(f'{e}')        
    except Exception as e: 
        print(f"{e}")
def F_move(directory): 
    try: 
        files = [file for file in os.listdir(directory) if os.path.isfile(file) ]
        folders = [folder for folder in os.listdir(directory) if os.path.isdir(folder)]
        print(f"files of {directory}")
        for index in range(len(files)): 
            print(f"{index}. {files[index]}")
        print(f"{len(files)}. exit")
        ans = int(input("which file do you want move?\n=>"))
        for i in range(len(files)): 
            if ans == i: 
                for j in range(len(folders)): 
                    print(f'{j}. {folders[j]}')
            
                print(f"{len(folders)}. exit")
                s = int(input(f"where do you want to move the file to ?\n=>"))
                for k in range(len(folders)):
                    if s == k : 
                        source = os.path.join(directory,files[i])
                        target = os.path.join(os.path.join(directory,folders[j]),files[i])
                        shutil.move(source,target)
                        print(f"{files[i]} has been moved to {folders[k]}")
                        logging.info(f"{files[i]} has been moved to {folders[k]}")
                        break
                    elif s == len(folders): 
                        print("exiting \n")
                        break
                    else : 
                        print("enter proper index \n")
                break
            elif ans == len(files):
                print(f'exiting.. \n')
                break
            else : 
                print("enter proper value\n")

    except FileNotFoundError as e : 
        print(f'{e}')        
    except ValueError as e : 
        print(f'{e}')
    except Exception as e: 
        print(f"{e}")

def main():
    try:
        directory = os.getcwd()
        print("\nHello! Filemanager")
        print("-----------------------------------------------------------------------------------------------")
        print(pyfiglet.figlet_format("FILE MANAGER"))
        print(f"filemanager has been started {datetime.datetime.now()} for {directory}")
        print('-----------------------------------------------------------------------------------------------')
        while True:
            
            logging.info(f'filemanager has been started {datetime.datetime.now()} for {directory}')

            print("1. Organize file(this create folder according the extension and move the file to that directory)")
            print("2. display files inside of a folder")
            print("3. Create a new file")
            print("4. delete file ")
            print("5. remove folder")
            print("6. display the files  and folders of the current directory")
            print("7. rename a file")
            print("8. Move file")
            print("9. Exit ")
            ans = input("=>").strip().lower()
            if ans == '1':
                print("Reading all files from your current directory.")
                logging.info(f"file organization has been started  for {directory}\n")
                organize(directory)
            elif ans == '2':
                display(directory)
                logging.info(f"displaying files inside of {directory} \n")
            elif ans == '3':
                F_create()
            elif ans == '4':
                F_delete(directory)
            elif ans == '5':
                F_remove(directory)
            elif ans == '6':
                F_display(directory)
            elif ans == '7':
                F_rename(directory)
            elif ans == '8': 
                F_move(directory)
            elif ans == '9':
                print("You are now exiting.")
                logging.info('Exited\n')
                break
            else:
                print('Enter proper value. it should be in range of 1-8 ')

    except KeyboardInterrupt:
        print("\nExiting.")
        logging.info('Exited through keyboard interruption.\n')
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f"Error: {e}\n")

if __name__ == "__main__":
    main()
