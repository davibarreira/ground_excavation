import string
import os
import sys

# Insert file name from the terminal - it's necessary to have the file at the current folder #
for index in range(1,len(sys.argv)):
    
    
    if len(sys.argv) > 1: filename = sys.argv[index]
    else: sys.exit("Input Error, no filename given")
    loc = os.getcwd()
    filename = loc + r'/' + filename
    file = open('%s' %filename)
    
    # Creating files names #
    
    name = string.replace(file.name,'.obj','')
    nameV = name + '_verts.mesh'
    nameC = name + '_faces.mesh'
    
    
    l= []   #List of file lines
    v =[]   #Vertices coordinates
    c =[]   #Connectivity
    
    k =0    #Auxiliary variable
    
    
    for line in file.readlines():
        l.append(string.split(line))
    
    
    for i in range(len(l)):
        if l[i][0]=='v':
            l[i].pop(0)
            v.append(string.join(l[i]," "))
    
            k+=1
        if l[i][0]=='f':
            l[i].pop(0)
            l[i].append('2')
            c.append(string.join(l[i]," "))
    file.close()
    
    #Write the new files
    
    file = open('%s' %nameV,'w+')
    for i in range(len(v)):
        file.seek(0,2)
        file.write(v[i])
        file.write('\n')
    file.seek(0,0)
    file.close()
    
    file = open('%s' %nameC,'w+')
    for i in range(len(c)):
        file.seek(0,2)
        file.write(c[i])
        file.write('\n')
    file.seek(0,0)
    file.close()
