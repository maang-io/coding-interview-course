// https://leetcode.com/problems/number-of-provinces/
public class Solution {
    public int FindCircleNum(int[][] isConnected) {
        int N = isConnected.Length;
        int count = 0;
        HashSet<int> visited = new HashSet<int>();
        for(int i = 0; i < N; ++i) {
            if(visited.Contains(i)) 
                continue;
            dfs(i, visited, isConnected);
            ++count;
        }
        return count;
    }

    private void dfs(int src, HashSet<int> visited, int[][] isConnected) {
        visited.Add(src);
        for(int i = 0; i < isConnected.Length; ++i) {
            if(i == src || isConnected[i][src] == 0 || visited.Contains(i)) {
                continue;
            }
            dfs(i, visited, isConnected);
        }
    }
}