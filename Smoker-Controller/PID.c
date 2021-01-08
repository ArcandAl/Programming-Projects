#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <time.h>
#include <unistd.h>
#include <errno.h>
#include <fcntl.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include "PID.h"

#define True 1

struct PID
{
  time_t lastTime;

  double targetTemp;
  double lastError;

  double propGain;
  double integGain;
  double derivGain;
  double integError;
  double lastTempOut;
}pid1;

double *pidAlgorithm(double input, double setpoint, time_t curTime)
{

    time_t elapsedTime = curTime - pid1.lastTime;

    double instanteneousError = setpoint - input;
    double propError = instanteneousError;
    pid1.integError = pid1.integError + (instanteneousError + pid1.lastError) * elapsedTime;
    double cumulativeError = pid1.integError;
    double rateOfError = (instanteneousError - pid1.lastError) / elapsedTime;

    double propOutput = pid1.propGain * propError;
    double integOutput = pid1.integGain * cumulativeError;
    double derivOutput = pid1.derivGain * rateOfError;

    pid1.lastError = instanteneousError;
    pid1.lastTime = curTime;

    static double OutputArray[3];
    OutputArray[0] = propOutput;
    OutputArray[1] = integOutput;
    OutputArray[2] = derivOutput;

    return OutputArray;

}

int changeGPIOPin(char gpioPin[], char value[])
{
    int fd = open(strcat(gpioPin, "/direction"), O_WRONLY);
     if(fd == -1) {
         perror(strcat("Unable to open pin ", gpioPin));
         close(fd);
         return 1;
     }
     
     if(write(fd, "out", 3) != 3) {
         perror(strcat("Unable to set output pin for ", gpioPin));
         close(fd);
         return 1;
     }
     
     if(write(fd, value, 1) != 1) {
         perror(strcat("Unable to turn on pin ", gpioPin));
         close(fd);
         return 1;
     }
     close(fd);
     
     return 0;
 }

int update(double tempOut)
{
    char fanGPIO[] = "/sys/class/gpio/gpio14";
    char augerGPIO[] = "/sys/class/gpio/gpio15";
    
   if (tempOut > pid1.lastTempOut)
   {
       changeGPIOPin(fanGPIO, "1");
       changeGPIOPin(augerGPIO, "1");
   }

   else if (tempOut < pid1.lastTempOut)
   {
       changeGPIOPin(fanGPIO, "0");
       changeGPIOPin(augerGPIO, "0");
   }
  return 0;
}

int main()
{
    pid1.lastTime = time(NULL);

    pid1.targetTemp = 350;
    pid1.lastError = 0.0;

    pid1.propGain = 0.75;   /* may need to adjust values*/
    pid1.integGain = 0.01;
    pid1.derivGain = 0.001;
    pid1.integError = 0.0;
    pid1.lastTempOut = 0.0;

    while (True)
    {
        double *p;
        double currTemp = getTemp(); /* need to get current temp here */
        while (currTemp < 170)
        {
            /* stay in smoke mode */
            sleep(30);
            double currTemp = getTemp();
            if (currTemp > 170)
            {
                break;
            }
        }


        printf("Current temp: %f \n", currTemp);

        sleep(1);

        p = pidAlgorithm(currTemp, pid1.targetTemp, time(0));
        double propOut = *(p + 0);
        double integOut = *(p + 1);
        double derivOut = *(p + 2);

        double tempOut = propOut + integOut + derivOut;


        printf("Temp out: %f \n", tempOut);
        printf("\n");


        update(tempOut);
        pid1.lastTempOut = tempOut;
        sleep(10);

    }

    return 0;
}
