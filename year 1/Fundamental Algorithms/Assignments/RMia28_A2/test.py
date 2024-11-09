import functions
import utils
def test_add():
    assert functions.add([1,2,3],4) == [1,2,3,4] 
    assert functions.add([3,2,1],0) == [3,2,1,0] 
    assert functions.add([0,1],5) == [0,1,5]

test_add()

def test_insert():
    assert functions.insert([1,2],3,2) == [1,2,3]
    assert functions.insert([1,3,4],2,1) == [1,2,3,4]
    assert functions.insert([2,3,4],1,0) == [1,2,3,4]

test_insert()

def test_remove():
    assert functions.remove([1,2,3],0) == [2,3]
    assert functions.remove([5,6,7],1) == [5,7]
    assert functions.remove([10,11,12,13],2) == [10,11,13]

test_remove()

def test_remove_sequence():
    assert functions.remove_sequence([1,2,3,4],2,3) == [1,2]
    assert functions.remove_sequence([1,2,3],0,2) == []
    assert functions.remove_sequence([1,2,3],0,1) == [3]

test_remove_sequence()

def test_replace():
    assert functions.replace([1,2,1,2],[1,2],[3]) == [3,3]
    assert functions.replace([5,5,6,6],[5],[1,2]) == [1,2,1,2,6,6]
    assert functions.replace([1,2,3],[2],[5,6]) == [1,5,6,3]

test_replace()

def test_prime():
    assert functions.prime([1,2,3,4,5],0,4) == [2,3,5]
    assert functions.prime([25,3,7],1,2) == [3,7]
    assert functions.prime([5,2,4,10],0,2) == [5,2]

test_prime()

def test_odd():
    assert functions.odd([1,2,3,4],0,3) == [1,3]
    assert functions.odd([0,2,4,8],0,3) == []
    assert functions.odd([3,5,7],0,2) == [3,5,7]

test_odd()

def test_suma():
    assert functions.suma([1,1,1],1,2) == 2
    assert functions.suma([2,2,2],0,1) == 4
    assert functions.suma([1,1],0,0) == 1

test_suma()

def test_gcd():
    assert functions.gcd([2,4,6],0,2) == 2
    assert functions.gcd([1,5,3,9],2,3) == 3
    assert functions.gcd([0,0,10],1,2) == 10

test_gcd()

def test_max():
    assert functions.max([100,5,2],0,2) == 100
    assert functions.max([25,0,1],1,2) == 1
    assert functions.max([2,3,0],0,1) == 3

test_max()

def test_filter_prime():
    assert functions.filter_prime([25,7,1,2]) == [7,2]
    assert functions.filter_prime([2,4,6]) == [2]
    assert functions.filter_prime([1,2,3,4]) == [2,3]

test_filter_prime()

def test_filter_negative():
    assert functions.filter_negative([-1,-2,3]) == [-1,-2]
    assert functions.filter_negative([1,2,3]) == []
    assert functions.filter_negative([2,-3,4]) == [-3]

test_filter_negative()

def test_is_prime():
    assert utils.is_prime(10) == False
    assert utils.is_prime(25) == False
    assert utils.is_prime(3) == True

test_is_prime()

def test_gcd2():
    assert utils.gcd2(25,5) == 5
    assert utils.gcd2(10,20) == 10
    assert utils.gcd2(5,3) == 1

test_gcd2()







