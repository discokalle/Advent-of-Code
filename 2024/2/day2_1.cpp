#include <fstream>
#include <string>
#include <sstream>
#include <iostream>
int main() {
    std::ifstream file("input.txt");
    std::string line{};
    int res{};

    while (std::getline(file, line)) {
        std::istringstream str{line};
        int n1{}, n2{};
        bool increases{}, decreases{};
        str >> n1;
        while (str >> n2) {
            if (abs(n1 - n2) < 1 || abs(n1 - n2) > 3 || //diff outside accepted limits.
            (n1 < n2 && decreases) || (n1 > n2 && increases)) { //pattern has changed
                increases = decreases = false; //unsafe
                break; 
            }
            if (n1 < n2) increases = true;
            else if (n1 > n2) decreases = true;
            n1 = n2;
        }
        if (increases || decreases) res += 1; //safe
    }
    std::cout << res << std::endl;
    return 0;
}