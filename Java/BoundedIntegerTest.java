import org.junit.Assert;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;


public class BoundedIntegerTest 
{
   private BoundedInteger bi1;

   
   @Before public void setUp() 
   {
      bi1 = new BoundedInteger(0,12,4);
   }


   
   @Test public void addTest() 
   {
      bi1.add(-4);
      assertEquals(0, bi1.getValue());
      bi1.setValue(4);
      assertEquals(4, bi1.getValue());
      bi1.add(9);
      assertEquals(0, bi1.getValue());
      bi1.setValue(4);
      bi1.add(-4);
      assertEquals(0, bi1.getValue());
      
     
   }
   
   @Test public void subtractTest() 
   {
      bi1.subtract(3);
      assertEquals(1, bi1.getValue());
      
   }
}
