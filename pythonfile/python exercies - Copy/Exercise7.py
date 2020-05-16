ls = [4, 7, 9, 10, 12, 32, 21, 33] # no error 

ls1 = [ i, for i in range(5)]   
                                # correct one is ls1 = [ i for i in range(5)]

ls2 = [ i for i in ls: if ls%3] 
                                # correct one is ls2 = [ i for i in ls if i % 3]

ls3 = [ [i, i**2] for i in range[10]]   
                                        # correct one is ls3 = [ [i, i**2] for i in range(10)]
                                        
ls4 = [ (i, i**2) for i range(5)]       
                                        # correct one ls4 = [ (i, i**2) for i in range(5)]