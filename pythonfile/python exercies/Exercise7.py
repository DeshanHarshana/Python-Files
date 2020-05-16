ls = [4, 7, 9, 10, 12, 32, 21, 33] # no error this code work fine


ls1 = [ i, for i in range(5)]   # we have an error we can't put a comma after i
                                # correct way is ls1 = [ i for i in range(5)]

ls2 = [ i for i in ls: if ls%3] # we can't put colon and we can't mod ls because it is list type
                                # correct way is ls2 = [ i for i in ls if i % 3]

ls3 = [ [i, i**2] for i in range[10]]   # we can't [] for range
                                        # correct way is ls3 = [ [i, i**2] for i in range(10)]
                                        # get i and i**2 and put to ls3

ls4 = [ (i, i**2) for i range(5)]       # we should use in keyword after i
                                        # correct way ls4 = [ (i, i**2) for i in range(5)]