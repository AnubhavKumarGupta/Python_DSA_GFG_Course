class Solution:
    def solve(self, N, A):
        def repeated_numbers(A):
            act_a = 0
            act_sum_sq = 0
            
            for num in A:
                act_a += num
                act_sum_sq += num * num
            
            exp_b = N * (N + 1) // 2
            exp_sum_sq = N * (N + 1) * (2 * N + 1) // 6



### Unsolved