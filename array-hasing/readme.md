https://chatgpt.com/g/g-p-6acfdb55e04481919ccbeac630266de1-array-hasing/c/6acfdc90-d5d0-83ee-b804-57eeed21a4e6

Pattern 1 — Arrays and sets
Learn membership checking, duplicates, and array traversal.
Problems: Contains Duplicate, Intersection of Two Arrays
Key idea: set, iteration, membership testing.

Pattern 2 — Hash maps and frequency counting
Store values and count how often they occur.
Problems: Two Sum, Valid Anagram, Majority Element
Key idea: dict, Counter, lookup in O(1) average time.

Pattern 3 — Grouping and canonical representations
Convert items into a common key so related items match.
Problems: Group Anagrams, Find All Anagrams in a String (as a later bridge to sliding window)
Key idea: frequency tuple, sorted string, dictionary of lists.



Pattern 4 — Index mapping and in-place arrays
Use indices, array properties, and swaps instead of extra storage.
Problems: Missing Number, First Missing Positive
Key idea: index-value relationships, cyclic placement.



Pattern 5 — Prefix sums + hash maps
Track cumulative sums to find subarrays efficiently.
Problems: Subarray Sum Equals K, Continuous Subarray Sum
Key idea: prefix sum, difference lookup, count of previous sums.



Pattern 6 — Combining patterns
Recognize when two or more techniques work together.
Problems: Top K Frequent Elements, Longest Consecutive Sequence
Key idea: frequency map + bucket/heap, set + sequence starts.