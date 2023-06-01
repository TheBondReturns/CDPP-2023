def permutation(action,object):

    action = list(action)
    object = list(object) 
    object2 = object.copy()

    for i in range(-1,len(action)-1):

        a = action[i] - 1
        b = action[i+1] - 1
        object2[b] = object[a]


    return object2

object = range(1,10)

action = range(1,6,2)

object = permutation(action,object)

print(object)


