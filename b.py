

# def calculate_max_degree(keys):
#     frequency_dict = {}
#     for key in keys:
#         if key in frequency_dict:
#             frequency_dict[key] += 1
#         else:
#             frequency_dict = 1
#     # degree_dict = {}
#     max_degree = 0
#     for key,value in frequency_dict.items():
#         # if key in degree_dict:
#         #     degree = degree_dict[key]
#         # else:
#         degree = 0
#         for i,j in frequency_dict.items():
#             if key%i == 0:
#                 degree += j
#         # degree_dict[key] = degree
#         if degree>max_degree:
#             max_degree = degree
#
#     return max_degree
    # dict_keys = {}
    # max_degree = 0
    # for k in keys:
    #     if k in dict_keys:
    #         degree = dict_keys[k]
    #     else:
    #         degree = 0
    #         for j in keys:
    #             if k%j == 0:
    #                 degree = degree + 1
    #         dict_keys[k] = degree
    #     if degree>max_degree:
    #         max_degree = degree
    # return max_degree


# def calculate_max_degree(keys):
#     degree_dict = {}
#     max_degree = 0
#     for k in keys:
#         if k in degree_dict:
#             degree = degree_dict[k]
#         else:
#             degree = 0
#             for j in keys:
#                 if k%j == 0:
#                     degree = degree + 1
#             degree_dict[k] = degree
#         if degree>max_degree:
#             max_degree = degree
#     return max_degree

def calculate_max_degree(keys):
    max_ = max(keys)
    freq = [0 for i in range(max_+1)]

    for i in range(0,len(keys)):
        freq[keys[i]] += 1

    res = [0 for i in range(max_+1)]

    for i in range(1,max_ + 1,1):
        for j in range(i,max_+1,i):
            res[j] += freq[i]

    max_degree = 0
    for i in range(len(keys)):
        if res[keys[i]]>max_degree:
            max_degree = res[keys[i]]

    return max_degree

def encryptionValidity(instructionCount, validityPeriod, keys):
    # Write your code here
    max_degree = calculate_max_degree(keys)
    strength = max_degree*100000
    given_strength = instructionCount*validityPeriod
    if strength>given_strength:
        res = 0
    else:
        res = 1
    return [res,int(strength)]

print(encryptionValidity(100,1000,[2,4,8,2]))