# Word Ladder

Problem can be found in [here](https://leetcode.com/problems/word-ladder)!

### [Solution](/Graph/127-WordLadder/solution.py): Breadth-First Search

```python
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    memo = set(wordList)
    queue = deque([(beginWord, 0)])

    while queue:
        word, counter = queue.popleft()
        if word == endWord:
            return counter+1
        for i in range(len(word)):
            for char in ascii_lowercase:
                new_word = word[:i] + char + word[i+1:]
                if new_word in memo:
                    memo.remove(new_word)
                    queue.append((new_word, counter+1))

    return 0
```

Time Complexity: ![O(N*M^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(N\cdot&space;M^2)>), Space Complexity: ![O(N)](<https://latex.codecogs.com/svg.image?\inline&space;O(N)>), where N is the length of wordList and M is the length of word.
