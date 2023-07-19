# Problem

You are given two integer arrays, $A$ and $B$ of dimensions $N$ X $M$.
Your task is to perform the following operations:

1. Add ( + )
2. Subtract ( - )
3. Multiply ( * )
4. Integer Division ( / )
5. Mod ( % )
6. Power ( ** )

**Note**
There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

**Input Format**

The first line contains two space separated integers, $N$ and $M$.
The next $N$ lines contains $M$ space separated integers of array $A$.
The following $N$ lines contains $M$ space separated integers of array $B$.

**Output Format**

Print the result of each operation in the given order under **Problem**.

---

**Sample Input**

```
1 4
1 2 3 4
5 6 7 8
```

**Sample Output**

```
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 
```