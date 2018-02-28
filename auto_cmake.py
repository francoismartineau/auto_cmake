import os, sys, subprocess

"""
    Ce script permet de créer un projet cmake rapidement.
    Il doit être appelé avec en argument n'importe quel fichier source d'un projet.
    Par projet, je veux dire l'ensemble des fichiers sources contenus dans le même dossier.
"""







"""
    brief : Trouve tous les fichiers sources qui accompagnent le fichier fourni
            en argument. Les note dans variables.
"""
def get_source_files():
    try:
        global PROJ_DIR, variables
        PROJ_DIR = os.path.dirname(os.path.realpath(sys.argv[1:][0]))
        variables["project_name"] = os.path.basename(PROJ_DIR)
        source_files = []
        for f in os.listdir(PROJ_DIR):
            if f.endswith(".cpp") and f != "main.cpp":
                source_files.append(f)
        return source_files
    except Exception as e:
        print("A source file must be provided as an argument.\n\n\n")
        raise e


"""
    arg   : liste des fichiers sources du projet
    brief : Crée les commandes SET(SOURCE_FILES ... )
            et ADD_LIBRARY(...) dans le CMakelists et les inclut dans variables
"""
def include_source_files(source_files):
    global variables
    variables["add_library"] = ""
    variables["source_files"] = ""
    if len(source_files) > 0:
        formated = ""
        for f in source_files:
            formated += f + " "
        variables["source_files"] = "SET(SOURCE_FILES {0})".format(formated)
        variables["add_library"] = "ADD_LIBRARY({0} STATIC ${{SOURCE_FILES}})".format(variables["library_name"])



"""
    brief : Crée le fichier cmakelists à partir du fichier template fourni avec ce script
            ainsi que des données recueillies dans variables. 
"""
def create_cmakelists():
    global PROJ_DIR, variables
    cmakelists_path = os.path.join(PROJ_DIR, "cmakelists.txt") 
    cmakelists = open(cmakelists_path, 'w')
    
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
    cmakelists_template = open(os.path.join(SCRIPT_DIR, "cmakelists_template.txt"), 'r')
    cmakelists.write(cmakelists_template.read().format( variables["cmake_version"],
                                                        variables["project_name"],
                                                        variables["c++_version"],
                                                        variables["source_files"],
                                                        variables["add_library"],
                                                        variables["library_name"]))
    cmakelists.close()
    cmakelists_template.close()


def make():
    global PROJ_DIR, variables
    os.chdir(PROJ_DIR)
    if not os.path.exists("build"):
        os.mkdir("build")
    os.chdir("build")
    subprocess.call(["cmake", "..", "-G", "MinGW Makefiles"])
    subprocess.call(["make"])
    



if __name__ == "__main__":
    PROJ_DIR = ""
    variables = {"cmake_version"    :   "3.3",
                 "c++_version"      :   "-std=c++11",
                 "library_name"     :   "Malib"}

    source_files = get_source_files()
    include_source_files(source_files)
    create_cmakelists()
    make() 

    
