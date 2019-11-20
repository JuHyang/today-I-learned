#include <stdio.h>

int main (void) {
    int T = 0;
    scanf ("%d", &T);

    for (int i = 0; i < T; i ++) {
        char str[31];
        int result = 0;
        scanf ("%s", str);
        for (int j = 1; j < 11; j++) {
            int status = 1;
            for (int o = 0; o < j; o ++) {
                if (str[o] != str[o + j]) {
                    status = 0;
                    break;
                }
                result = j;
            }
            if (status == 1) {
                printf ("#%d %d\n", i+1, result);
                break;
            }
        }
    }

    return 0;
}