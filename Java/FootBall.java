/**
 * @author  Alec Arcand
 * @version (December 03 2018)
 */

import java.awt.Graphics;
import java.awt.Color;

public class FootBall extends CannonBall
{
   public static final double GRAVITY_EFFECT = 0.02;

   public FootBall(int fx, int fy, int r , double dx, double dy)
   {
      super(fx,fy,r,dx,dy);
   }

   public void move()
   {
      setMotion( xMotion(), yMotion() + GRAVITY_EFFECT );
      super.move();
   }
   
   public void paint( Graphics g, int change )
   {
      g.setColor(new Color(175,100,0));
      g.fillOval( region().x+7+change,     region().y+20,
                 region().width, region().height/2);
   }
}