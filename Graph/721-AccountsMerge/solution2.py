from collections import defaultdict
from typing import List


class DisjointSet:
    def __init__(self, length: int):
        self.rank = [1] * length
        self.parent = [i for i in range(length)]

    def union(self, u: int, v: int) -> None:
        # Find their root nodes of two respective nodes
        u_root, v_root = self.find(u), self.find(v)
        if u_root == v_root:
            return

        # Union by rank
        if self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        elif self.rank[u_root] < self.rank[v_root]:
            self.parent[u_root] = v_root
        else:
            self.parent[v_root] = u_root
            self.rank[u_root] += 1

    def find(self, element: int) -> int:
        # Perfrom path compression when finding its root node
        if element != self.parent[element]:
            self.parent[element] = self.find(self.parent[element])

        return self.parent[element]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails_ownership = {}
        disjoint_set = DisjointSet(len(accounts))

        for id, account in enumerate(accounts):
            for i in range(1, len(account)):
                email = accounts[id][i]
                # If email have been already seen, then union this account with the one in the hash table
                if email in emails_ownership:
                    disjoint_set.union(id, emails_ownership[email])
                emails_ownership[email] = id

        # Merge emails based on their root node in the disjoint set
        merged_accounts = defaultdict(list)
        for email, account in emails_ownership.items():
            merged_accounts[disjoint_set.find(account)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in merged_accounts.items()]
