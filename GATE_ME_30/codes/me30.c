#include <stdio.h>
#include<math.h>
#include<time.h> 

float x(float t);

float k = 2000 ; // Equivalent spring constant 
float m = 20 ; // Mass of the block
float a = 1 ;// Plug amplitude as 1


int main() 
{
    FILE *file = fopen("values.dat", "w"); //open values.dat to print the data in it
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    float t_0 = 0.7; //approximately one time period
    float t = 0 ; //current time
    while(t < 0.7)
    {
        fprintf(file ,"%f \t %e\n", t , x((float)(t)));
        t+= 0.001 ;
    }   
    return 0 ;
}
float x(float t)
{
    return cos(sqrt(k/m)*t);  // function of x(t)
}
