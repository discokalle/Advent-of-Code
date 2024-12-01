#include <fstream>
#include <set>
#include <iostream>
int main() {
    std::ifstream file("input.txt");
    std::multiset<int> set_l{}, set_r{}; //multisets are oredered by default. They include repeats; sets do not.
    int l{}, r{}, res{};

    while (file >> l >> r) //Read file and insert the numbers ordered.
    {
        set_l.insert(l); 
        set_r.insert(r);
    }

    auto it_l{set_l.begin()}, it_r{set_r.begin()}; //iterators, since multiset can't be accessed by index
    for (; it_l != set_l.end(); ++it_l, ++it_r) {
        res += abs(*it_l - *it_r);
    }
    std::cout << res;

    return 0;
}