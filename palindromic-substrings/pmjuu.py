class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]  # dp[i][j]는 s[i:j+1]이 팰린드롬인지 나타냄
        count = 0

        for length in range(1, n + 1): # 부분 문자열 길이
            for i in range(n - length + 1): # 시작 인덱스
                j = i + length - 1 # 끝 인덱스

                if length == 1:                 # 길이 1: 항상 팰린드롬
                    dp[i][j] = True
                elif length == 2:               # 길이 2: 두 문자가 같으면 팰린드롬
                    dp[i][j] = (s[i] == s[j])
                else:                           # 그 외의 경우: 양 끝이 같고 내부가 팰린드롬이면 참
                    dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
                
                if dp[i][j]:
                    count += 1

        return count


# 시간 복잡도:
# - 이중 반복문으로 모든 부분 문자열을 확인하므로 O(n^2)
# - 각 확인은 O(1)이므로 최종적으로 O(n^2)

# 공간 복잡도:
# - DP 테이블(dp)은 O(n^2)의 공간을 사용
# - 추가 변수는 O(1)이므로 전체 공간 복잡도는 O(n^2)
