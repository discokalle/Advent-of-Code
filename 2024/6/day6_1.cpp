#include <fstream>
#include <vector>
#include <string>
#include <iostream>
#include <set>

int main() {
    std::ifstream file{"input.txt"};
    std::vector<std::string> grid{};
    std::string line{};
    
    while (std::getline(file, line)) {
        grid.push_back(line);
    }

    std::pair<int, int> curr{52, 36}; //Start pos: 6,4 for ex; 52,36 for input
    std::pair<int, int> next{};
    int dir{}; //0-N, 1-E, 2-S, 3-W
    std::set<std::pair<int, int>> visited{};
    
    while(1) {
        visited.insert(curr);

        next = {curr.first + (dir == 2) - (dir == 0),  //N: -1, S: +1
            curr.second + (dir == 1) - (dir == 3)}; //E: +1, W: -1

        if ((next.first == -1) || (next.first == grid.size()) //out of bounds; done.
            ||(next.second == -1) || (next.second == grid.size())) {
            break;
        }
        
        switch(grid[next.first][next.second]) {
            case '#':
                dir = (dir + 1) % 4; //rotate
                break;
            case '.':
            case '^':
                curr = next;
                break;
        }
    }
    
    std::cout << visited.size() << std::endl;
    return 0;
}