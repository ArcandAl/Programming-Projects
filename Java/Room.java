/*
 * Class Room - a room in an adventure game.
 *
 * This class is part of the "World of Zuul" application. 
 * "World of Zuul" is a very simple, text based adventure game.  
 *
 * A "Room" represents one location in the scenery of the game.  It is 
 * connected to other rooms via exits.  The exits are labelled north, 
 * east, south, west.  For each direction, the room stores a reference
 * to the neighboring room, or null if there is no exit in that direction.
 * 
 * @author  Alec Arcand
 * @version (October 16 2018)
 */
 
import java.util.HashMap;

public class Room 
{
   private String description;
   public HashMap< String,Room > exits;

    /**
     * Create a room described "description". Initially, it has
     * no exits. "description" is something like "a kitchen" or
     * "an open court yard".
     */
   public Room(String description) 
   {
      this.description = description;
      exits = new HashMap< String,Room >();
   }

    /**
     * Define the exits of this room.  Every direction either leads
     * to another room or is null (no exit there).
     */
   public void setExit(String room, Room loc) 
   {
      exits.put(room,loc);
   }

    /**
     * Return the description of the room (the one that was defined
     * in the constructor).
     */
   public String getDescription()
   {
      return description;
   }
    
   public Room getExit(String direction)
   {
         
      if(direction.equals("north"))
         return exits.get("north");
      if(direction.equals("east"))
         return exits.get("east");
      if(direction.equals("south"))
         return exits.get("south");
      if(direction.equals("west"))
         return exits.get("west");
      if(direction.equals("up"))
         return exits.get("up");
      if(direction.equals("down"))
         return exits.get("down");
      else
      {
         return null;
      }
   }
   
   public String getExitString()
   {
      String ways = "";
      if(exits.get("north") != null)
         ways = ways + "north ";
      if(exits.get("east") != null)
         ways = ways + "east ";
      if(exits.get("south") != null)
         ways = ways + "south ";
      if(exits.get("west") != null)
         ways = ways + "west ";
      if(exits.get("up") != null)
         ways = ways + "up ";
      if(exits.get("down") != null)
         ways = ways + "down ";
      return ways;
   }

}
