import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;
import java.awt.image.BufferStrategy;
import java.awt.Color;

public class DomeWorld extends JFrame
{
   public static final int FRAME_WIDTH = 600;
   public static final int FRAME_HEIGHT = 400;

   private int        angle;
   private String     message;
   private String     scoreLabel;
   private FootBall   footBall;
   private JScrollBar  angleSlider,DistanceSlider,HeightSlider;
   private BufferStrategy myStrategy;
   private int distance;
   private int goalHeight;
   private int score;
   private boolean goal;
   
   public static void main ( String[] args )
   {
      DomeWorld world = new DomeWorld( );
      world.setVisible(true);
   }

   public DomeWorld()
   {
      super();
      setSize ( FRAME_WIDTH, FRAME_HEIGHT );
      setTitle( "Football Game" );
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
   
      distance = 0;
      goalHeight = 0;
      score = 0;
      angle = 45;
      scoreLabel = "Score ";
      message = "Angle: " + angle;
      footBall = null;   
         
      angleSlider = new JScrollBar( JScrollBar.VERTICAL, angle, 5, 0, 95 );
      angleSlider.addAdjustmentListener( new AngleScrollBarListener() );
      getContentPane().add( "West", angleSlider );
      
      DistanceSlider = new JScrollBar( JScrollBar.HORIZONTAL, distance, 5, 0, 305);
      DistanceSlider.addAdjustmentListener( new CloserScrollBarListener() );
      getContentPane().add( "South", DistanceSlider );
      
      HeightSlider = new JScrollBar( JScrollBar.VERTICAL, goalHeight, 5, 0, 245 );
      HeightSlider.addAdjustmentListener( new HeightScrollBarListener() );
      getContentPane().add( "East", HeightSlider );
      
      JPanel buttonPanel = new JPanel();
      buttonPanel.setLayout(new GridLayout(1,1) );
      
      JButton fire = new JButton( "kick" );
      fire.addActionListener( new FireButtonListener() );
      buttonPanel.add( fire );
      
   
      add( "North", buttonPanel );
      this.setVisible(true);
      this.createBufferStrategy(2);
   }

   public static int dy( int y )
   {
      return FRAME_HEIGHT - y;
   }

   public void paint( Graphics g )
   {
      while (myStrategy==null)
      {
         myStrategy=this.getBufferStrategy();
         try{
            Thread.sleep(25);
         } 
         catch(Exception e) {}
      }
      g = myStrategy.getDrawGraphics();
      
      super.paint(g);
      drawKicker    ( g,distance );
      drawTarget    ( g, goalHeight );
      drawFootBall( g, distance, goalHeight );
      writeMessage  ( g );
      writeScore(g);
      
      g.dispose();
      myStrategy.show();
      Toolkit.getDefaultToolkit().sync();
   }

/* -------------- helper methods -------------- */
      
   protected void drawKicker(Graphics g, int change)
   {
      int x = 20;
      int y = 15;
   
      double radianAngle = angle * Math.PI / 180.0;
   
      int lv = (int) (30 * Math.sin(radianAngle)); 
      int lh = (int) (30 * Math.cos(radianAngle));  
      int sv = (int) (10 * Math.sin(radianAngle + Math.PI/2)); 
      int sh = (int) (10 * Math.cos(radianAngle + Math.PI/2));
      
      g.drawLine(x+lh+sh+change, dy(y+lv+sv), x+lh+sv+change, dy(y+sv));
      g.drawLine(x+lh+sh+change, dy(y+lv+sv), x+lh+sh+change, dy(lv*3));
      g.drawLine(x+lh+sh+change, dy(y+lv+sv), x+sh+change, dy(y+sv));
      g.drawLine(x+lh+sv+change,(dy(lv*3)+dy(y+lv+sv))/2,x+sh+change,(dy(lv*3)+dy(y+lv+sv))/2);
      g.drawOval(x+lh+sh-12/2+change, dy(lv*3)-12, 12, 12);
   }

   protected void drawTarget( Graphics g, int change )
   {
      g.setColor(Color.red);
      g.fillRoundRect( FRAME_WIDTH-100, dy(50)-change, 50, 10, 6, 6 ); // lower bar
      g.drawLine(FRAME_WIDTH-73, dy(50)-change,FRAME_WIDTH-73, dy(12));
      g.drawLine(FRAME_WIDTH-100,dy(50)-change,FRAME_WIDTH-100,dy(90)-change);  // left bar
      g.drawLine(FRAME_WIDTH-50, dy(50)-change,FRAME_WIDTH-50, dy(90)-change);  // right bar
   }

   protected void drawFootBall( Graphics g, int dChange, int gChange )
   {
      int targetX = FRAME_WIDTH-100; //bounds of left bar
      int targetY = dy(50)-gChange; //bounds of lower bar
      int targetH = targetY-40; //bounds of top bar
   
      if ( footBall != null )
      { 
         footBall.move();
         footBall.paint( g, dChange );
         
         try
         {
            Thread.sleep(30);
         }
         catch (InterruptedException e) {}
         
         if(dy(footBall.y()) > 0)
         {
            if ( (footBall.x()+dChange > targetX) && 
            (footBall.y() < targetY) && 
            (footBall.y() > targetH)) 
            {
               goal = true;
            }
            
            repaint();
         }
         else
         {
            
            if(goal)
            {
               message = "You made it and earned 3 points!";
               score = score +3;
               System.out.println("Here"); 
            }
            else
            {
             
            
               message = "Missed!";
            
            }
            footBall = null;
         
         }
        
      }
   }

   protected void writeMessage( Graphics g )
   {
      g.drawString( message, FRAME_WIDTH/2, FRAME_HEIGHT/2 );
   }
   
   protected void writeScore(Graphics g)
   {
      g.drawString(scoreLabel+score, FRAME_WIDTH/2, FRAME_HEIGHT/3);
   }

/* -------------- inner classes -------------- */

   private class FireButtonListener implements ActionListener
   {
      public void actionPerformed( ActionEvent e )
      {
         double radianAngle = angle * Math.PI / 180.0;
         double sinAngle    = Math.sin( radianAngle );
         double cosAngle    = Math.cos( radianAngle );
      
         footBall = new FootBall (
            10 + (int) (30 * cosAngle),
            dy(10+(int) (30 * sinAngle)),
            5, 12 * cosAngle, -12 * sinAngle );
         repaint();
         goal = false;
      
      }
   }

   private class AngleScrollBarListener implements AdjustmentListener
   {
      public void adjustmentValueChanged (AdjustmentEvent e)
      {
         angle   = angleSlider.getValue();
         message = "Angle: " + angle;
         repaint();
      }
   }
   
   private class CloserScrollBarListener implements AdjustmentListener
   {
      public void adjustmentValueChanged (AdjustmentEvent e)
      {
         distance = DistanceSlider.getValue();
         message = "Distance: " + distance;
         repaint();
      }
   }
   
   private class HeightScrollBarListener implements AdjustmentListener
   {
      public void adjustmentValueChanged (AdjustmentEvent e)
      {
         goalHeight = HeightSlider.getValue();
         message = "Height: " + goalHeight;
         repaint();
      }
   }
}
