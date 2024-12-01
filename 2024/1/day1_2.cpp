#include <fstream>
#include <set>
#include <iostream>
#include <map>
int main() {
    std::ifstream file("input.txt");
    std::multiset<int> set_l{}; //multisets are oredered by default. They include repeats; sets do not.
    std::map<int, int> map_r{};
    int l{}, r{}, res{};

    while (file >> l >> r) //Read file and insert the numbers ordered.
    {
        set_l.insert(l); 
        map_r[r]++;
    }

    auto it_l{set_l.begin()}; //iterators, since multiset can't be accessed by index
    for (; it_l != set_l.end(); ++it_l) {
        res += *it_l * map_r[*it_l];
    }
    std::cout << res;

    return 0;
}