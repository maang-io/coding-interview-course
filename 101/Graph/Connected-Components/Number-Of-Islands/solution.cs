public class Solution {
    private int rowSz = 0, colSz = 0;
    private bool[,] visited = null;
    private int[,] dirns = new int[,] {{-1,0}, {1,0}, {0,-1}, {0,1}};
    public int NumIslands(char[][] grid) {
        rowSz = grid.Length;
        colSz = grid[0].Length;
        int count = 0;
        visited = new bool[rowSz, colSz];
        for(int r = 0; r < rowSz; ++r) {
            for(int c = 0; c < colSz; ++c) {
                if(grid[r][c] == '0' || visited[r,c] == true)
                    continue;
                dfs(grid,r,c);
                ++count;
            }
        }
        return count;
    }

    private void dfs(char[][] grid, int row, int col) {
        visited[row,col] = true;
        for(int d = 0; d < 4; ++d) {
            int nextRow = row + dirns[d,0];
            int nextCol = col + dirns[d,1];
            if(nextRow < 0 || nextCol < 0 || nextRow >= rowSz || nextCol >= colSz )
                {
                    continue;
            }
            if(grid[nextRow][nextCol] == '0' || visited[nextRow,nextCol] == true) {
                continue;
            }
            
            dfs(grid, nextRow,nextCol);
        }
    }
}