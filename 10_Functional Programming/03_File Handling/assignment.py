file_path = "C:\\Users\\martimar012\\POC_Sem2_Assignments\\10_Functional Programming\\03_File Handling\\newfile.txt"

try:
    stream = open(file_path)
    print(stream.read())
    stream.close()
except Exception as e:
    print('an error occured: ', e)