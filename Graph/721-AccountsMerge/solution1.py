from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def DFS(email: str) -> None:
            visited_emails.add(email)
            merged_emails.append(email)

            for new_email in emails_map[email]:
                if new_email not in visited_emails:
                    DFS(new_email)

        emails_map = defaultdict(list)
        for account in accounts:
            first_email = account[1]
            for i in range(2, len(account)):
                email = account[i]
                emails_map[first_email].append(email)
                emails_map[email].append(first_email)

        merged_accounts, visited_emails = [], set()
        for account in accounts:
            name, first_email = account[0], account[1]
            if first_email not in visited_emails:
                merged_emails = []
                DFS(first_email)
                merged_accounts.append([name] + sorted(merged_emails))

        return merged_accounts
