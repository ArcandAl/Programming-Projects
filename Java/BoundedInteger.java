/**
* This is first try at BoundedInteger
* @author Alec Arcand (arcanda)
* @version 2018-10-03
*/

public class BoundedInteger
{
   private int lowerBound;
   private int upperBound;
   private int currentValue;


   public BoundedInteger(int lower, int upper)
   {
      lowerBound = lower;
      upperBound = upper;
      currentValue = lower;
   }
   
   public BoundedInteger(int lower, int upper, int start)
   {
      lowerBound = lower;
      upperBound = upper;
      currentValue = start;
   }
   
   public void add(int value)
   {
      if (value < 0)
      {
         if (isLegal(currentValue - Math.abs(value)))
         {
            currentValue = currentValue - Math.abs(value);
         }
         else
         {
            int temp = currentValue;
            temp = temp - Math.abs(value);
            int length = (upperBound + 1) - lowerBound;
            while (temp < lowerBound)
            {
               temp = temp + length;
            }
            currentValue = temp;
         }
      }
      else 
      {
         if (isLegal(currentValue + value))
         {
            currentValue = currentValue+value;
         }
         else
         {
            int temp = currentValue;
            temp = temp + value;
            int length = (upperBound + 1) - lowerBound;
            while (temp > upperBound)
            {
               temp = temp - length;
            }
            currentValue = temp;
         }
      }
   }
   
   public void subtract(int value)
   {
      if (value < 0)
      {
         if (isLegal(currentValue + Math.abs(value)))
         {
            currentValue = currentValue + Math.abs(value);
         }
         else
         {
            int temp = currentValue;
            temp = temp + Math.abs(value);
            int length = (upperBound + 1) - lowerBound;
            while (temp > upperBound)
            {
               temp = temp - length;
            }
            currentValue = temp;
         }
      }
      else
      {
         if(isLegal(currentValue - value))
         {
            currentValue = currentValue-value;
         }
         else
         {
            int temp = currentValue;
            temp = temp - value;
            int length = (upperBound + 1) - lowerBound;
            while (temp < lowerBound)
            {
               temp = temp + length;
            }
            currentValue = temp;
         }
      }
   }
   
   public void increment()
   {
      add(1);
   }
   
   public void decrement()
   {
      subtract(1);
   }
   
   public int getValue()
   {
      return currentValue;
   }
   
   public int getLowerLimit()
   {
      return lowerBound;
   }
   
   public int getUpperLimit()
   {
      return upperBound;
   }
   
   public boolean setValue(int value)
   {
      if (isLegal(value))
      {
         currentValue = value;
         return true;
      }
      else
      {
         return false;
      }
   }
   
   public String toString()
   {
      return "BoundedInteger [lower="+lowerBound+","+"upper="+upperBound+","+"value"+currentValue+"]";
   }
   
   public boolean equals(BoundedInteger newBoundedInteger)
   {
      if (this.lowerBound == newBoundedInteger.lowerBound &
      this.upperBound == newBoundedInteger.upperBound & 
      this.currentValue == newBoundedInteger.currentValue)
      {
         return true;
      }
      else
      {
         return false;
      }
   }
   
   public boolean equivalentValue(BoundedInteger newBoundedInteger)
   {
      if (this.currentValue == newBoundedInteger.currentValue)
      {
         return true;
      }
      else
      {
         return false;
      }
   }
   
   public boolean equivalentLowerLimit(BoundedInteger newBoundedInteger)
   {
      if (this.lowerBound == newBoundedInteger.lowerBound)
      {
         return true;
      }
      else
      {
         return false;
      }
   }
   
   public boolean equivalentUpperLimit(BoundedInteger newBoundedInteger)
   {
      if (this.upperBound == newBoundedInteger.upperBound)
      {
         return true;
      }
      else
      {
         return false;
      }
   }
   
   public boolean isLegal(int value)
   {
      if (value <= upperBound & value >= lowerBound)
      {
         return true;
      }
      else
      {
         return false;
      }
   }
}