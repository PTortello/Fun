#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main() {

    int a, b, d1, d2, d3, d4, round = 0;
    char pass[5], guess[5], buffer[12];

    srand(time(NULL));
    d1 = rand() % 10;
    d2 = rand() % 9;
    if (d2 == d1) {
        d2++;
    }
    d3 = rand() % 8;
    if ((d3 == d1) || (d3 == d2)) {
        d3++;
        if ((d3 == d1) || (d3 == d2)) {
            d3++;
        }
    }
    d4 = rand() % 7;
    if ((d4 == d1) || (d4 == d2) || (d4 == d3)) {
        d4++;
        if ((d4 == d1) || (d4 == d2) || (d4 == d3)) {
            d4++;
            if ((d4 == d1) || (d4 == d2) || (d4 == d3)) {
                d4++;
            }
        }
    }

    sprintf(buffer, "%i", d1);
    strcpy(pass, buffer);
    sprintf(buffer, "%i", d2);
    strcat(pass, buffer);
    sprintf(buffer, "%i", d3);
    strcat(pass, buffer);
    sprintf(buffer, "%i", d4);
    strcat(pass, buffer);

    while (a < 4) {
        a = 0;
        b = 0;
        printf("\n### Round %i ###\nGuess: ", ++round);
        scanf("%s", guess);
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (pass[i] == guess[j]) {
                    (i == j) ? a++ : b++;
                }
            }
        }
        printf("Result: %iA%iB\n", a, b);
    }
    printf("\n### You win! ###\n\n");

    return 0;
}
