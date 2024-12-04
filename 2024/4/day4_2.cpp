#include <fstream>
#include <vector>
#include <string>
#include <iostream>

int search(const std::vector<std::string>& grid, const int& r, const int& c) {
    if (r <= 0 || c <= 0 || r >= grid.size() - 1 || c >= grid[r].size() - 1) return 0;
    if (grid[r-1][c-1] == 'M' && grid[r+1][c+1] == 'S' || grid[r-1][c-1] == 'S' && grid[r+1][c+1] == 'M') { //LMAO
        if (grid[r+1][c-1] == 'M' && grid[r-1][c+1] == 'S' || grid[r+1][c-1] == 'S' && grid[r-1][c+1] == 'M') return 1;
    }
    return 0;
}

int main() {
    std::ifstream file{"input.txt"};
    std::string line{};
    std::vector<std::string> grid{};
    int res{};
    while(std::getline(file, line)) {
        grid.push_back(line);
    }

    for (int r{0}; r < grid.size(); ++r) {
        for (int c{0}; c < grid[r].size(); ++c) {
            if (grid[r][c] == 'A') res += search(grid, r, c);
        }
    }
    std::cout << res << std::endl;
}