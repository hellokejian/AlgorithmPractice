# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def add_two_numbers(l1, l2):
    l3 = [] * (max(len(l1), len(l2)) + 1)
    index1 = 0
    index2 = 0
    extra = 0
    while (index1 < len(l1)) or (index2 < len(l2)):
        add = int(l1[index1]) + int(l2[index2]) + extra
        extra = 0
        l3[index1] += abs(add-10)
        if add >= 10:
            l3[index1+1] = 1
            extra = 1
        # l3.append(add)
        index1 += 1
        index2 += 1
    if index1 == len(l1):
        l3.extend(l2[index2:])
    else:
        l3.extend(l1[index1:])
    return l3


a = [2, 4, 3]
b = [5, 6, 4]
c = add_two_numbers(a, b)
print(c)
