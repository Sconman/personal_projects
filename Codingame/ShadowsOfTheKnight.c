#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
void batman_jump(int * x1, int * x2, int * y1, int * y2, char bomb_dir[4],int x, int y);
int main()
{
    // width of the building.
    int w;
    // height of the building.
    int h;
    scanf("%d%d", &w, &h);
    // maximum number of turns before game over.
    int n;
    
    scanf("%d", &n);
    int x0;
    int y0;
    scanf("%d%d", &x0, &y0);

    // game loop
    int left_bound = 0;
    int top_bound = 0;
    int right_bound = w-1;
    int bottom_bound = h-1;

    int x = x0; // x of batman
    int y = y0; // y of batman
    while (1) {
        // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
        char bomb_dir[4];  
        scanf("%s", bomb_dir);
        
        
        batman_jump(&left_bound, &right_bound , &top_bound , &bottom_bound , bomb_dir, x, y);
        x = (left_bound + right_bound) / 2;
        y =(top_bound + bottom_bound) / 2;
        printf("%d %d\n",x,y);

        // Write an action using printf(). DON'T FORGET THE TRAILING \n
        // To debug: fprintf(stderr, "Debug messages...\n");


        // the location of the next window Batman should jump to.
        //printf("0 0\n");
    }

    return 0;
}
void batman_jump(int * left_bound, int * right_bound, int * top_bound, int * bottom_bound, char bomb_dir[4], int x, int y) {
    fprintf(stderr, "Before jump: left = %d, right = %d, top = %d, bottom = %d, bomb_dir = %s\n",
            *left_bound, *right_bound, *top_bound, *bottom_bound, bomb_dir);
    
    
    if (strchr(bomb_dir,'U')) {
        *bottom_bound = y-1; // if the bomb is above batman the bottom bound is 1 above batman 
        
    }
    if (strchr(bomb_dir,'D')) {
        *top_bound = y+1; // if bomb is below batman top bound = 1 below batman
    }

    if (strchr(bomb_dir,'L')) {
        *right_bound = x-1; //
    }
    if (strchr(bomb_dir,'R')) {
        *left_bound = x+1;
    }

    
  
}
