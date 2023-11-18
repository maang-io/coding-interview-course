public class Solution {
    public int MaxAreaOfIsland(int[][] grid) {
        int rowSz = grid.Length, colSz = grid[0].Length;
        int result = 0;
        bool[,] visited = new bool[rowSz, colSz];
        for(int r = 0; r < rowSz; ++r) {
            for(int c = 0; c < colSz; ++c) {
                if(grid[r][c] == 0 || visited[r,c] == true) {
                    continue;
                }
                int area = Explore(grid, r,c, visited);
                result = Math.Max(area, result);
            }
        }
        return result;
    }

    private int[,] dirns = new int[,] { {-1,0}, {1,0}, {0, 1}, {0, -1}};

    private int Explore(int[][] grid, int row, int col, bool[,] visited) {
        int rowSz = grid.Length, colSz = grid[0].Length;
        int area = 1;
        visited[row,col] = true;
        for(int d = 0; d <dirns.GetLength(0); ++d) {
            int nr = row + dirns[d,0];
            int nc = col + dirns[d,1];
            if(nr < 0 || nr >= rowSz || nc < 0 || nc >= colSz || 
                grid[nr][nc] == 0 || visited[nr,nc]) {
                    continue;
            }
            area += Explore(grid, nr, nc, visited);
        }
        return area;
    }
}