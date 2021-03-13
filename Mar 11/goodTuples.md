```
Given a list of integers, count the number of 'good tuples' that can be created. A 'good tuple' is defined as consecutive triplets having exactly 2 duplicate elements.
For eg.
nums = [4,4,6,1,2,2,2,3]
Here good tuples are: [4,4,6], [1,2,2], [2,2,3] becaue here in nums[i-1], nums[i], nums[i+1] eaxactly 2 nubers are equal, however [2,2,2] isn't a good tuple because nums[i-1]==num[i]==nums[i+1].
Count of good tuples is 3.

Another example:
nums = {4,6,4,1,3,4}
Here there is only one good tuple: [4,6,4]. Count of good tuples is 1.

```
