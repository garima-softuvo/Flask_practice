import os
#Read files from the folder
path = r"/home/softuvo/Garima/Flask Practice/Flask_practice/files"
files =os.listdir(path)
print(files)

for f in files:
    filename=os.path.join(path, f)
    print(filename)

# def convertToBinaryData(filename):
    # Convert digital data to binary format
for p in path2:
    with open(path2, 'rb') as file:
        binaryData = file.read()
    # return binaryData

    

# #join paths 
# path_joined = os.path.join("path", "SampleCSVFile_119kb.csv") 
# # print(path_joined)
# # print(path)

# #reading the file data after joining the path

# # with open("path_joined", "r") as f:
# #     read = f.read()
# #     print(read)


# for file in files:
#     print(file)
    
#     with open(file, "rb") as file1:
#         binary = file1.read()
#         print(binary)

# with open("/home/softuvo/Garima/Flask Practice/Flask_practice/files/SampleCSVFile_119kb.csv", "rb") as file:
#     binary = file.read()



    
