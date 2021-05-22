def swap():
    filename1=input('Pls enter the name for file 1')
    filename2=input('Pls enter the name for file to be swapped')

    with open(filename1, 'r') as a:
      data_a=a.read()
        
    with open(filename2, 'r') as b:
      data_b=b.read()


    with open(filename1,'w') as a:
        a.write(data_b)
    with open(filename2,'w') as b:
        b.write(data_a)
    

swap()
