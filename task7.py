try:
    fo=open('sample.txt','r')
  
    # lines= fo.readlines()
    # for i,line in enumerate(lines,start=1):
    #     print(f"Line {i}:{line}")
    lines=fo.read()
    print("Reading file content:")
    for line in lines.splitlines(True):
         print(line)
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except IOError:
    print("Error: Could not read the file.")
finally:
      fo.close()
