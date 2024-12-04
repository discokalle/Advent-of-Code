#include <fstream>
#include <vector>
#include <string>
#include <iostream>

int search(const std::vector<std::string>& grid, const int& r, const int& c) { //Look in each direction for the next letters.
    int matches{};
    for (int dir_r{-1}; dir_r <= 1; ++dir_r) {
        for (int dir_c{-1}; dir_c <= 1; ++dir_c) {
            if (dir_r == 0 && dir_c == 0) continue; //This is X
            int row{r}, col{c}; //tmp r and c
            bool match{true};
            for (char ch : std::string{"XMAS"}) { 
                if (row < 0 || col < 0 
                || row >= grid.size() || col >= grid[row].size()
                || grid[row][col] != ch) {
                    match = false; //Nuh-uh!
                    break;
                } 
                row += dir_r;
                col += dir_c;
            }
            if(match) ++matches;
        }
    }
    return matches;
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
            if (grid[r][c] == 'X') res += search(grid, r, c);
        }
    }
    std::cout << res << std::endl;
}