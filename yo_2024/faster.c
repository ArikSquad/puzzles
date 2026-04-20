#include <stdio.h>

int main() {
  int n = 8;
  int a = 2;
  while (n > 1) {
    if (n % a == 0) {
      printf("%i\n", a);
      n = n / a;
    } else {
      a = a + 1;
    }
  }
}
