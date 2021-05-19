public class MovableBall extends Ball
{
    private double dx;
    private double dy;

    public MovableBall( int x, int y, int r, double dx, double dy )
    {
        super( x, y, r );
        this.dx = dx;
        this.dy = dy;
    }

    public void move()
    {
        region().translate( (int) dx, (int) dy );
    }

    protected void setMotion( double ndx, double ndy )
    {
        dx = ndx;
        dy = ndy;
    }

    protected double xMotion()
    {
        return dx;
    }

    protected double yMotion()
    {
        return dy;
    }
}
