package byog.Core;

//import byog.TileEngine.TERenderer;

import byog.TileEngine.TETile;

import java.io.Serializable;

public class SaveGame implements Serializable {
    Test object;
    TETile[][] randomstuff;
    String name;
    boolean backmove;
    int difficulty;

    public SaveGame(Test x, TETile[][] y, String random, Boolean stuff, int diff) {
        object = x;
        randomstuff = y;
        name = random;
        backmove = stuff;
        difficulty = diff;
    }
}
