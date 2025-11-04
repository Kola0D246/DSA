def topKFrequent(nums: list[int], k: int) -> list[int]:
    dict = {}
    for num in nums:
        if num in dict.keys():
            dict[num] += 1
        else:
            dict[num] = 1

    print(dict)

    largest = []
    keys = dict.keys()
    largest.extend(keys[k])
    print(largest)
    '''
    for key in dict.keys():
        for idx in range(k):
            largest.append()
            if largest[idx] == 0:
                continue
            if dict[num] > dict[largest[idx]]:
                largest.insert(idx, num)
                largest.pop()
            if num == largest[idx]:
                break

    return largest
    '''

topKFrequent([1,2,2,3,3,3],2)