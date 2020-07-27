// Pedro Tortello jul/2020

#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#ifdef _WIN32
    #define clearScreen system("cls")
    #define colorScreen system("color 06")
#else
    #define clearScreen system("clear")
    #define colorScreen NULL
#endif

// Game from 1 to 100 with 7 tries
#define MIN_RANGE 1
#define MAX_RANGE 100
#define MAX_TRIES 7

void verify(int n, int guess);
void game(void);

int main(void)
{
    char play;

    colorScreen;
    clearScreen;
    printf("###\tTortello's High-Low Game\t###\n");
    printf("###\tGuess a number from %d to %d\t###\n", MIN_RANGE, MAX_RANGE);

    do
    {
        game();
        getchar();
        printf("\nPlay again? (Y/N) ");
        scanf("%c", &play);
        clearScreen;
    } while (play == 'Y' || play == 'y');

    return 0;
}

// Verifies the user input against the answer
void verify(int n, int guess)
{
    if (n < guess)
    {
        printf("Too High!\n");
    }
    else if (n > guess)
    {
        printf("Too Low!\n");
    }
    else
    {
        printf("You Won!\n");
    }
}

// Main game loop
void game(void)
{
    int n, guess, tries;

    srand(time(0));
    n = rand() % MAX_RANGE + MIN_RANGE;
    tries = 0;
    do
    {
        if (tries == MAX_TRIES)
        {
            printf("You Lost! The answer was: %d\n", n);
            break;
        }
        tries++;
        printf("\nGuess the number: ");
        scanf("%d", &guess);
        verify(n, guess);
    } while (n != guess);
    printf("Number of tries: %d\n", tries);
}
