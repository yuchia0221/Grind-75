from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def DFS(row: int, column: int, word_index: int) -> None:
            nonlocal is_word_exist
            if is_word_exist:
                return
            if word_index == len(word):
                is_word_exist = True
                return
            if row == -1 or row == row_number or column == -1 or column == column_number:
                return

            data = board[row][column]
            board[row][column] = ""
            if data == word[word_index]:
                DFS(row+1, column, word_index+1)
                DFS(row-1, column, word_index+1)
                DFS(row, column+1, word_index+1)
                DFS(row, column-1, word_index+1)
            board[row][column] = data

        is_word_exist = False
        row_number, column_number = len(board), len(board[0])
        for row in range(row_number):
            for column in range(column_number):
                if board[row][column] == word[0]:
                    DFS(row, column, 0)
                if is_word_exist:
                    break

        return is_word_exist
