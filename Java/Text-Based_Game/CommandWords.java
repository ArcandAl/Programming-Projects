/**
 * This class is part of the "World of Zuul" application. 
 * "World of Zuul" is a very simple, text based adventure game.  
 * 
 * This class holds an enumeration of all command words known to the game.
 * It is used to recognise commands as they are typed in.
 *
 * @author  Alec Arcand
 * @version (October 16 2018)
 */

public class CommandWords
{
    // a constant array that holds all valid command words
   private static final String[] validCommands = {
        "go", "quit", "help", "look"
    };

    /**
     * Constructor - initialise the command words.
     */
   public CommandWords()
   {
        // nothing to do at the moment...
   }

    /**
     * Check whether a given String is a valid command word. 
     * Return true if it is, false if it isn't.
     */
   public boolean isCommand(String aString)
   {
      for(int i = 0; i < validCommands.length; i++) {
         if(validCommands[i].equals(aString))
            return true;
      }
        // if we get here, the string was not found in the commands
      return false;
   }
    
   public String showAll()
   {
      String all_cmds = "";
      for(int i = 0; i < validCommands.length; i++)
      {
         all_cmds = all_cmds + validCommands[i] + " ";
      }
      return all_cmds;
   }

}
