import time

def answer(g):
    start = time.time()
    a = [((True,False),(False,False)), ((False,True),(False,False)), ((False,False),(True,False)), ((False,False),(False,True))]

    b = [((False,False),(False,False)),((True,True),(True,True))]
    b.extend((((True,True),(False,False)),((False,False),(True,True)),((True,False),(True,False)),((False,True),(False,True))))
    b.extend((((True,True),(True,False)),((True,False),(True,True)),((False,True),(True,True)),((True,True),(False,True))))
    b.extend((((True,False),(False,True)),((False,True),(True,False))))
    
    agraph = {(False, True): [(False, False)], (True, False): [(False, False)], (False, False): [(True, False), (False, True)]}
    bgraph = {(False, True): [(False, True), (True, True), (True, False)], (True, False): [(True, False), (True, True), (False, True)], (False, False): [(False, False), (True, True)], (True, True): [(True, True), (False, False), (True, False), (False, True)]}
    
    
    for i in xrange(0,len(g[0])):
        for j in xrange(0,len(g)-1):
            
            if g[j][i] == True:
                x = agraph
            else:
                x = bgraph
            if g[j+1][i]==True:
                y = agraph
            else:
                y = bgraph
            
            column1 = {}
            for key in y:
                column1[key]=y[key]
            
            todel = []
            
            for botkey in column1:
                newmat = []
                for (ind,elem) in enumerate(column1[botkey]):
                    if j == 0:
                        if j== len(g)-2:
                            if elem in x:
                                for k in x[elem]:
                                    newmat.append([k,elem,botkey])
                        else:
                            if elem in x:
                                for k in x[elem]:
                                    newmat.append([k,elem])
                    elif j==len(g)-2:
                        
                        if elem in column2:
                            for k in column2[elem]:
                                kk = []
                                for ind in k:
                                    kk.append(ind)
                                kk.append(elem)
                                kk.append(botkey)
                                newmat.append(kk)
                    else:
                        if elem in column2:
                            for k in column2[elem]:
                                kk = []
                                for ind in k:
                                    kk.append(ind)
                                kk.append(elem)
                                newmat.append(kk)
                            
                if newmat == []:
                    todel.append(botkey)
                else:
                    column1[botkey] = newmat

            for key in todel:
                column1.pop(key, None)
            column2 =column1
            
        if i==0:
            major = {}
            
            for key in column2:
                for (ind,elem) in enumerate(column2[key]):
                    q = tuple([row[1] for row in elem[:]])
                
                    if q in major:
                        major[q] += 1
                    else:
                        major[q] = 1
            
        elif i==len(g[0])-1:
            leftside = []
            major2 = {}
            for key in column2:
                for (ind,elem) in enumerate(column2[key]):
                    p = tuple([row[0] for row in elem[:]])
                    q = tuple([row[1] for row in elem[:]])

                    leftside.append(p)
                    if q in major2:
                        major2[q].append(p)
                    else:
                        major2[q] = [p]
            k = 0 
            for key in major2:
                toadd = 0
                for (ind,elem) in enumerate(major2[key]):
                    if elem in major:
                        toadd += major[elem]
                        k+=major[elem]
                major2[key] = toadd
        else:
            leftside = []
            major2 = {}
            for key in column2:
                for (ind,elem) in enumerate(column2[key]):
                    p = tuple([row[0] for row in elem[:]])
                    q = tuple([row[1] for row in elem[:]])

                    leftside.append(p)
                    if q in major2:
                        major2[q].append(p)
                    else:
                        major2[q] = [p]
    
            for key in major2:
                toadd = 0
                for (ind,elem) in enumerate(major2[key]):
                    if elem in major:
                        toadd += major[elem]
                major2[key] = toadd
            major = major2
        
    
    end = time.time()
    print(end-start)
    return k

g = [[True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False]]
g.append([True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False])
g.append([True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False])
g.append([True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False])
g.append([True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False])
g.append([True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False])
g.append([True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False,True, True, False, True, False, True, False, True, True, False])

answer(g)