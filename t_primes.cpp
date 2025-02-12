#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iostream>

int main() {
  uint64_t n = 0;
  std::cin >> n;

  while (n--) {
    uint64_t x = 0;
    std::cin >> x;

    if (x == 1) {
        std::cout << "NO" << std::endl;
        continue;
    }

    uint64_t root = (uint64_t)sqrt(x);

    if (root * root < x) {
        std::cout << "NO" << std::endl;
    } else {
        uint64_t pd = 2;
        bool is_prime = true;
        while (pd * pd <= root) {
            if (root % pd == 0) {
                is_prime = false;
                break;
            }
            pd += 1;
        }
        if (is_prime) {
            std::cout << "YES" << std::endl;
        } else {
            std::cout << "NO" << std::endl;
        }
    }

    // uint64_t num_unique_divisors = 0;
    // for (uint64_t pd = 1; pd * pd <= x; pd++) {
    //   uint64_t xod = x / pd;
    //   uint64_t xmd = x - xod * pd;
    //   if (xmd == 0) {
    //     if (xod == pd) {
    //       num_unique_divisors += 1;
    //     } else {
    //       num_unique_divisors += 2;
    //     }
    //   }
    // }
    // if (num_unique_divisors == 3) {
    //   std::cout << "YES" << std::endl;
    // } else {
    //   std::cout << "NO" << std::endl;
    // }
  }
  return 0;
}
