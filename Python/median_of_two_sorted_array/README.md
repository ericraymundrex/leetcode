Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the **two sorted arrays**.

The overall run time complexity should be O(log (m+n))

**_Solution:_**

- When we merge two arrays together then it is O(m+n) not O(log(m+n)).
- When we need a log algorithm we use the binary search.

```
nums1=[1,2,3,4,5,6,7,8]
nums2=[1,2,3,4,5]

merge=[1,1,2,2,3,3,4,4,5,5,6,7,8]
```

- Median means middle value.
- Partitioning the arrau into two equal halfs roughly.

- For example, forget the last element, then 
```
merge=[1,1,2,2,3,3,   4,4,5,5,6,7]

- Here the left partition has 6 elements and the right partition have 6 elements.
```

- :point_up: In this case, the right most element in the left partition and left most element in the right partition and find the average.

- Average =3+4/2=3.5

