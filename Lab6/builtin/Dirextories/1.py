import os

def existance(path):
    if not os.path.exists(path):
        print(f"{path} doesnt exist")
        return


    print("Dir:\n")
    print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

    print("Files:\n")
    print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

    print("contents:")
    print(os.listdir(path))

existance("a")
