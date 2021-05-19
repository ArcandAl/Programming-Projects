import java.awt.Color;

public class CannonBall extends MovableBall
{
   public CannonBall (int sx, int sy, int r, double dx, double dy)
   {
      super(sx, sy, r, dx, dy);
   }

   public void move ()
   {
      setMotion( xMotion(), yMotion() + 0.3 );
      super.move();
     }
}
