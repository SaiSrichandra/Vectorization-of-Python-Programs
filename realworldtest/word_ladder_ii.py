#!/usr/bin/env python
#
# description: Word Ladder II
# difficulty: Hard
# leetcode_num: 126
# leetcode_url: https://leetcode.com/problems/word-ladder-ii/
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such that:
#
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# Note:
#
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: []
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.


from collections import deque


ALPHABET = [chr(i) for i in range(ord('a'), ord('z')+1)]


# Uses BFS to store the character transformatations
def WordLadderLength(begin_word, end_word, word_list):
    word_list = set(word_list)
    if end_word not in word_list:
        return 0

    level = 1
    q = deque()
    q.append(begin_word)

    while len(q) != 0:
        qsize = len(q)
        for i in range(qsize):
            word = list(q.popleft())

            for i in range(len(word)):
                original_char = word[i]

                for c in ALPHABET:
                    if c == word[i]:
                        continue

                    word[i] = c
                    new_word = ''.join(word)
                    if new_word == end_word:
                        return level + 1

                    if new_word in word_list:
                        q.append(new_word)
                        word_list.remove(new_word)

                word[i] = original_char
        level += 1

    return 0


if __name__ == '__main__':
    test_cases = [
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5),
        (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0),
    ]

    for inp, res in test_cases:
        assert WordLadderLength(inp[0], inp[1], inp[2]) == res, 'Test Failed'
