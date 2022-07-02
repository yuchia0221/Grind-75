# Accounts Merge

Problem can be found in [here](https://leetcode.com/problems/accounts-merge)!

### [Solution 1](/Graph/721-AccountsMerge/solution1.py): Depth-First Search + Hash Table

```python
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def DFS(email: str) -> None:
            visited_emails.add(email)
            merged_emails.append(email)

            for new_email in emails_map[email]:
                if new_email not in visited_emails:
                    DFS(new_email)

        # Construct emails map for constant look-up speed
        emails_map = defaultdict(list)
        for account in accounts:
            first_email = account[1]
            for i in range(2, len(account)):
                email = account[i]
                emails_map[first_email].append(email)
                emails_map[email].append(first_email)

        # Perform DFS to merge accounts
        merged_accounts, visited_emails = [], set()
        for account in accounts:
            name, first_email = account[0], account[1]
            if first_email not in visited_emails:
                merged_emails = []
                DFS(first_email)
                merged_accounts.append([name] + sorted(merged_emails))

        return merged_accounts
```

Explanation: To merge multiple accounts, the most simple solution is to iterate for every email in each account and check if there is another account having the same email. This solution will work; however, this will result in poor time complexity. To improve the algorithm, we can first build an email map that helps us to look-up for its account in constant time (the first email are used for key in this problem). Each email in the same account are paired with the first email. In other words, we will connect emails in an account in a [star](<https://en.wikipedia.org/wiki/Star_(graph_theory)>) manner with the first email as the internal node of the star and all other emails as the leaves. After constructing the map, we can run DFS for every email we have not been vistied yet. In each iteration of DFS, we mark this email as visited so that we will not need to visit it again. In addition, we will reach back to the iternal node of that star with the email map we built earlier. By knowing the internal node, we can run DFS again for every unvisited email for that internal node.

Time Complexity: ![O(NMlogNM)](<https://latex.codecogs.com/svg.image?O(NMlogNM)>).

-   Denote ![N](https://latex.codecogs.com/svg.image?N) as the number of accounts and ![M](https://latex.codecogs.com/svg.image?M) as the maximum number of emails in one account. In worst case, all emails belong to one person. Therefore, sorting ![N*M](https://latex.codecogs.com/svg.image?N\cdot&space;M) emails will need ![O(NMlogNM)](<https://latex.codecogs.com/svg.image?O(NMlogNM)>) time, while building emails map and running DFS both will cost ![O(NM)](<https://latex.codecogs.com/svg.image?O(NM)>) time as no email will be traversed more than once. These procedures result in ![O(NMlogNM)](<https://latex.codecogs.com/svg.image?O(NMlogNM)>) time complexity.

Space Complexity: ![O(NM)](<https://latex.codecogs.com/svg.image?O(NM)>) for emails map.

### [Solution 2](/Graph/721-AccountsMerge/solution2.py): Disjoint Set

Time Complexity: ![O(NMlogNM)](<https://latex.codecogs.com/svg.image?O(NMlogNM)>).

-   Denote ![N](https://latex.codecogs.com/svg.image?N) as the number of accounts and ![M](https://latex.codecogs.com/svg.image?M) as the maximum number of emails in one account. In worst case, all emails belong to one person. Therefore, sorting ![N*M](https://latex.codecogs.com/svg.image?N\cdot&space;M) emails will need ![O(NMlogNM)](<https://latex.codecogs.com/svg.image?O(NMlogNM)>) time, while building emails map and running union-find operations will cost ![O(NM)](<https://latex.codecogs.com/svg.image?O(NM)>) time and ![a(N)](<https://latex.codecogs.com/svg.image?\alpha&space;(N)>) time, respectivey. Notice that ![a(N)](<https://latex.codecogs.com/svg.image?\alpha&space;(N)>) is the inverse Ackermann function.

Space Complexity: ![O(NM)](<https://latex.codecogs.com/svg.image?O(NM)>) for emails map.
