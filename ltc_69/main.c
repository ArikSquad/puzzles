#include "stdio.h"
int isqrt(int x) {
  if (x < 2)
    return x;

  int left = 1;
  int right = x / 2;
  int ans = 1;

  while (left <= right) {
    int mid = left + (right - left) / 2;

    if (mid <= x / mid) {
      ans = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return ans;
}

int main() {
  int ans = isqrt(8);
  printf("isqrt of 8 is %d\n", ans);
}
