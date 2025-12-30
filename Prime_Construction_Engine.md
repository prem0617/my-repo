# Prime Construction Engine

- Overview:

  - The Prime Construction Engine (PCE) is a constrained combinatorial problem designed to test a developer’s ability to think algorithmically, not just write syntax that compiles.

  - At its core, the problem asks the developer to generate prime numbers from the digits of a given integer. However, unlike trivial permutation-based problems, PCE introduces real-world constraints such as pruning, duplicate elimination, pattern restrictions, and performance boundaries.

  - The goal is to simulate how production-grade logic is built:

    - Managing exponential search spaces
    - Applying early rejection strategies
    - Designing reusable validation pipelines
    - Making trade-offs between time and memory

  - This problem is language-independent and focuses purely on problem-solving skill, not library knowledge.
  - If brute force is your strategy - congratulations, you’ve already failed.

## Problem

- You are given a non-negative integer `N` (up to 18 digits).
- Using any subset of its digits, in any order, construct numbers under the following constraints and identify all unique prime numbers that can be formed.

## Rules & Constraints

- Digit Usage Rules

  - You may use 1 to all digits of `N`
  - Each digit can be used at most as many times as it appears in `N`
  - Leading zeros are NOT allowed
  - Digits cannot be skipped silently
  - Usage must be explicit

- Prime Validation Rules

  - A number is considered valid only if:
    - It is prime
    - It is greater than a configurable threshold `T`
    - It does not contain forbidden digit patterns
    - It does not exceed a configurable limit `L`

- Forbidden Patterns

  - The number must NOT:
    - Contain consecutive repeating digits (e.g., `11`, `2333`)
    - Contain palindromic substrings of length ≥ 3
    - Be divisible by any digit present in the original number
    - Contain more than K even digits

- Duplicate Elimination Rules

  - Different permutations producing the same number count once
  - Results must be sorted:
    - By number of digits
    - Then by numeric value

- Performance Constraints

  - N can have up to 18 digits
  - Brute force permutations will TLE
  - You must:
    - Use pruning
    - Apply early prime rejection
    - Cache sub-results
    - Avoid redundant permutations

- Required Output
  - Print:
    - The list of valid primes
    - Total count of valid primes
    - Time complexity analysis
    - Memory optimization explanation

## Example

### Input

```bash
n = 325
l = 10
t = 1000
k = 2
```

### Output

```bash
Primes: [23, 53, 523]
Count: 3
```

Note: (Yes, `2`, `3`, `5` got kicked out - rules are rules)

---

## Bonus Challenges (Optional)

- Return results streamed, not stored fully
- Add a flag to allow/disallow reuse of digits
- Parallelize permutation generation
- Implement a bitmask-based digit state
- Make it language-agnostic (no BigInt)
