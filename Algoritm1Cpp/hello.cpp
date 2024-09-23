#include <iostream> 

int main() {
    register int x = 0;
    while (x < 1000000000) {
        x++;
    }
    std::cout << x << std::endl;
}