#include <stdio.h>

int main (void) {
    int board[15][15] = {0,};
    int T;
    scanf ("%d", &T);
    for (int i = 0; i < T; i++ ) {
        int result = 0;
        int N, K;
        scanf ("%d %d", &N, &K);
        for (int j = 0; j < N ; j++) {
            for (int o = 0; o < N; o++) {
                scanf ("%d", &board[j][o]);
            }
        }

        for (int j = 0; j < N ; j++) {
            int count = 0;
            int status = 1;
            for (int o = 0; o < N; o++) {
                status = board[j][o];
                if (status == 1) {
                    count += 1;
                } else {
                    count = 0;
                }
                if (count == K) {
                    if (o == N - 1 || board[j][o + 1] == 0) {
                        result += 1;
                        count = 0;
                    }
                }
            }
            count = 0;
            for (int o = 0; o < N; o++) {
                status = board[o][j];
                if (status == 1) {
                    count += 1;
                } else {
                    count = 0;
                }
                if (count == K) {
                    if (o == N - 1 || board[o + 1][j] == 0) {
                        result += 1;
                    }
                }
            }
        }
        printf ("#%d %d\n", i+1, result);
    }
    return 0;
}