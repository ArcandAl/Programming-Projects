#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <time.h>
#include <unistd.h>
#include "PID.h"

double getTemp()
{
  /* Need to get current temp from temperature sensor instead*/
  /* This is for testing purposes*/
  
  printf("Enter a temperature: ");
  double currentTemp;
  scanf("%lf", &currentTemp);
  return currentTemp;
}
