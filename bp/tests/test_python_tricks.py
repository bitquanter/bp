from collections import Counter

def test_swap_values():
    '''
    swapping values
    '''
    a,b=5,10
    print(a,b)
    a,b=b,a
    print(a,b)
    pass


def test_create_str():
    '''
    create a single string from all the elements in list
    '''
    a = ['python','is','awesome']
    print("".join(a))
    pass


def test_most_freq():
    '''
    find the most frequent value in a list
    '''
    a = [1,2,3,1,2,3,2,2,4,5,1]
    print(max(set(a),key = a.count))
    cnt = Counter(a)
    print(cnt.most_common(3))
    pass


def test_check_anagrams():
    str1 = 'helloworld'
    str2 = 'helloworld'
    str3 = 'abccba'
    print(Counter(str1) == Counter(str2))
    print(Counter(str1) == Counter(str3))
    pass


def test_reverse_str():
    a = 'afasfvjaido[hvdafjbanbalkdg'
    print(a[::-1])
    for char in reversed(a):
        print(char)
    num = 123456789
    print(int(str(num)[::-1]))
    pass


def test_reverse_list():
    a = [5,4,3,2,1]
    print(a[::-1])
    for ele in reversed(a):
        print(ele)
    pass


def test_transpose_2d_array():
    original = [['a','b'],['c','d'],['e','f']]
    transposed = zip(*original)
    print(transposed)
    print(list(transposed))
    pass


def test_chained_comparison():
    b=6
    print(4<b<7)
    print(1==b<20)
    pass


def test_chained_func_call():
    def product(a,b):
        return a*b
    
    def add(a,b):
        return a + b
    
    b = True
    print((product if b else add)(5,7))
    pass


def test_copy_list():
    a = [1,2,3,4,5]
    '''fast way to make a shallow copy of a list'''
    b = a
    b[0]=10
    print(a,b)
    b= a[:]
    b[0] = 10
    print(a, b)
    a = [1,2,3,4,5]
    print(list(a))
    print(a.copy())
    from copy import deepcopy
    l = [[1,2],[3,4]]
    l2 = deepcopy(l)
    print(l2)
    pass


def test_dic_get():
    d = {'a':1,'b':2}
    print(d.get('c',3))
    pass


def test_sort_dic_value():
    d = {'apple':10,'orange':20,'banana':5,'tomato':1}
    print(sorted(d.items(),key=lambda x:x[1]))
    from operator import itemgetter
    print(sorted(d.items(),key=itemgetter(1)))
    print(sorted(d,key=d.get))
    pass


def test_for_else():
    a = [1,2,3,4,5]
    for el in a:
        if el == 0:
            break
    else:
        print('did not break out of for loop')
    pass


def test_convert_list_comma_sep():
    item = ['foo', 'bar', 'xyz']
    print(','.join(item))
    numbers = [2,3,5,10]
    print(','.join(map(str,numbers)))
    data = [2,'hello', 3,3.4]
    print(','.join(map(str,data)))
    pass


def test_merge_dic():
	d1 = {'a':1}
	d2 = {'b':2}
	print({**d1,**d2})
	print(dict(d1.items()|d2.items()))
	d1.update(d2)
	print(d1)
	pass


def test_min_max_in_list():
	lst = [40,10,20,30]
	min_index = min(range(len(lst)),key=lst.__getitem__)
	max_index = max(range(len(lst)),key=lst.__getitem__)
	print(min_index)
	print(max_index)
	pass


def test_remove_dup_from_list():
	items = [2,2,3,3,1]
	print(list(set(items)))
	from collections import OrderedDict
	items = ['foo','bar','bar','foo']
	print(list(OrderedDict.fromkeys(items).keys()))
	pass



if __name__ == '__main__':
    test_swap_values()
    test_create_str()
    test_most_freq()
    test_check_anagrams()
    test_reverse_str()
    test_reverse_list()
    test_transpose_2d_array()
    test_chained_comparison()
    test_chained_func_call()
    test_copy_list()
    test_dic_get()
    test_sort_dic_value()
    test_for_else()
    test_convert_list_comma_sep()
    test_merge_dic()
    test_min_max_in_list()
    test_remove_dup_from_list()

