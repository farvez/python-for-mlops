with open("C:\\Users\\Admin\\Downloads\\Python for MLOps\\Day-1\\data.txt", "r") as f:
    data = f.read()

print(data)

with open("result.txt", "w") as fi:
    fi.write("Model training successful")

with open("C:\\Users\\Admin\\Downloads\\Python for MLOps\\result.txt", "r") as fil:
    datas = fil.read()    

print(datas)
