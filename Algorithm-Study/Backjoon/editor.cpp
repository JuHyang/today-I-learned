#include <iostream>
#include <string.h>
using namespace std;

int L (int c) {
  if (c != 0) {
    return c - 1;
  } else {
    return c;
  }
}

int D (char * input, int c) {
  int temp = strlen(input);
  if (temp == c) {
    return c;
  } else if (c <= temp) {
    return c + 1;
  }
}

char * B (char * input, int c) {
  if (c == 0) {
    return input;
  } else {
    int temp = strlen(input);
    int i = 0;
    char * result = new char[100000];
    for (; i < c - 1; i ++) {
      result[i] = input[i];
    }
    for (; c < temp; c ++, i++) {
      result[i] = input[c];
    }
    memset (input, 0, 100000 * sizeof(char));

    for (int o = 0; o < temp - 1; o ++) {
      input[o] = result[o];
    }
    delete[] result;
    return input;
  }
}
char * P (char * input, char p, int c) {
  int temp = strlen(input);
  char * result = new char[100000];
  int i = 0;
  for (; i < c; i ++) {
    result[i] = input[i];
  }
  result[i] = p;
  i += 1;
  for (; i < temp + 1; i ++) {
    result[i] = input[i-1];
  }
  memset (input, 0, 100000 * sizeof(char));
  for (int o = 0; o < temp + 1; o ++) {
    input[o] = result[o];
  }
  delete[] result;
  return input;
}

int main (void) {
  char * input = new char[100000];
  char * result;
  char p;
  int T;
  int c;
  cin >> input;
  c = strlen(input);
  cin >> T;
  for (int i = 0; i < T; i ++) {
    char order;
    cin >> order;
    if (order == 'L') {
      c = L(c);
    } else if (order == 'D') {
      c = D(input, c);
    } else if (order == 'B') {
      if (c == 0) {
        continue;
      }
      input = B(input, c);
      c --;
    } else if (order == 'P') {
      char p;
      cin >> p;
      input = P(input, p ,c);
      c ++;
    }
  }
  cout << input << endl;
}
