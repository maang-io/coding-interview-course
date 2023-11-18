public class Solution {
    private int[,] dirns = new int[,] {{-1,0}, {1,0}, {0,1}, {0, -1}};
    public int NumEnclaves(int[][] grid) {
        int rowSz = grid.Length, colSz = grid[0].Length, result = 0;
        bool[,] visited = new bool[rowSz, colSz];
        for(int c = 0; c < colSz; ++c) {
            //First Row
            Visit(grid, 0, c, visited);

            //Last Row
            Visit(grid, rowSz-1, c, visited);
        }

        for(int r = 0; r < rowSz; ++r) {
            //First COl
            Visit(grid, r, 0, visited);

            //Last Col
            Visit(grid, r, colSz-1, visited);
        }

        for(int r = 0; r < rowSz; ++r) {
            for (int c = 0; c < colSz; ++c) {
                if(grid[r][c] == 1 && !visited[r,c])
                    ++result;
            }
        }
        return result;
    }

    private void Visit(int[][] grid, int row, int col, bool[,] visited) {
        if(grid[row][col] == 0 || visited[row,col])
            return;
        visited[row,col] = true;
        int rowSz = grid.Length, colSz = grid[0].Length;
        for(int d = 0; d < 4; ++d) {
            int nr = row +dirns[d,0];
            int nc = col + dirns[d,1];
            if(nr < 0 || nc < 0 || nr >= rowSz || nc >= colSz || visited[nr,nc] || grid[nr][nc] == 0)
                continue;
            Visit(grid, nr,nc, visited);
            
        }
    }
}