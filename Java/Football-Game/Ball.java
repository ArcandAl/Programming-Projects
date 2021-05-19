import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;

public class Ball
{
    private Rectangle location;
    private Color     color;

    public Ball( int x, int y, int r )
    {
        location = new Rectangle( x-r, y-r, 2*r, 2*r );
        color    = Color.blue;
    }

    public void paint( Graphics g )
    {
        g.setColor( color );
        g.fillOval( location.x, location.y, location.width, location.height );
    }

    public void setColor( Color newColor )
    {
        color = newColor;
    }

    public Color color()
    {
        return color;
    }

    protected int radius()
    {
        return location.width / 2;
    }

    protected int x()
    {
        return location.x + radius();
    }

    protected int y()
    {
        return location.y + radius();
    }

    protected Rectangle region() 
    {
        return location;
    }

    public void moveTo( int x, int y )
    {
        region().setLocation( x, y );
    }
}
