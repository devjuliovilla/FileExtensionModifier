import os

def changeExtension(directory, currentExtension, newExtension):
    try:
        # list directory files
        files = os.listdir(directory)
        
        # iterate on every file
        for file in files:
            # validate if file has the current extension
            if file.endswith(currentExtension):
                # build full path
                fullPath = os.path.join(directory, file)
                
                # change file extension
                newName = os.path.splitext(fullPath)[0] + newExtension
                
                # rename file
                os.rename(fullPath, newName)
                print(f"Archivo renombrado: {newName}")
        
        print("La conversión ha sido completada.")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # files path
    directory= input("Ingrese la ruta del directorio en el que desea trabajar: ")
    currentExtension= input("Ingrese la extensión que desea modificar: : ")
    newExtension= input("Ingrese la nueva extensión: : ")
    changeExtension(directory, currentExtension, newExtension)
