package byog.Core;

import byog.TileEngine.TERenderer;
import byog.TileEngine.TETile;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

import byog.TileEngine.Tileset;
import edu.princeton.cs.introcs.StdDraw;
import java.awt.Color;
import java.awt.Font;

public class Game implements Serializable {
    /* Feel free to change the width and height. */
    public static final int WIDTH = 50;
    public static final int HEIGHT = 50;
    TERenderer ter = new TERenderer();
    Test object;
    TETile[][] temptiles;
    String name = "";
    int difficulty = 1;
    boolean backmove;


    /**
     * Method used for playing a fresh game. The game should start from the main menu.
     */
    public void playWithKeyboard() {
        StdDraw.enableDoubleBuffering();
        loadFrame();
        StdDraw.show();
        StdDraw.pause(1000);
        drawFrame("'N' to start game. "
               + "'L' to load game. 'Q' to quit");
        StdDraw.show();
        char test = getAnswer(1);
        if (test == 'N' || test == 'n') {
            drawFrame("Objective: REACH THE FLOWER WITHOUT TOUCHING THE SAND");
            StdDraw.show();
            StdDraw.pause(1500);
            drawFrame("Please enter a seed. "
                   + "Type S when finished the seed");
            StdDraw.show();
            long seed = getSeed();
            drawFrame("Please enter difficulty "
                   + "from 1(easiest) to 5(hardest). Default difficulty is 1.");
            StdDraw.show();
            char diff = getAnswer(1);
            if (diff == '1') {
                difficulty = 1;
            } else if (diff == '2') {
                difficulty = 2;
            } else if (diff == '3') {
                difficulty = 3;
            } else if (diff == '4') {
                difficulty = 4;
            } else if (diff == '5') {
                difficulty = 5;
            } else {
                difficulty = 1;
            }
            drawFrame("Do you want to play with Back Tracking? (Y) or (N)");
            StdDraw.show();
            char ans = getAnswer(1);
            if (ans == 'Y' || ans == 'y'){
                this.backmove = true;
            }
            else if (ans == 'N' || ans == 'n'){
                this.backmove = false;
            }
            drawFrame("Do you want to name the character? 'Y' for yes. Any other letter for no.");
            StdDraw.show();
            //this.backmove = true;
            char answer = getAnswer(1);
            if (answer == 'Y' || answer == 'y') {
                System.out.println("Changing Name");
                drawFrame("Please enter name. Type '.' when name is complete.");
                StdDraw.show();
                name = getName();
                ter.initialize(WIDTH, HEIGHT, 5, 5);
                temptiles = generateWorld(seed, difficulty);
                moveGuy(backmove);
            } else {
                ter.initialize(WIDTH, HEIGHT, 5, 5);
                temptiles = generateWorld(seed, difficulty);
                moveGuy(backmove);
            }
        } else if (test == 'Q' || test == 'q') {
            System.out.println("You quit the game");
            saveWorld(new SaveGame(object, temptiles, name, this.backmove, this.difficulty));
            System.exit(0);
        } else if (test == 'L' || test == 'l') {
            TETile[][] random = new TETile[50][50];
            //System.out.println("LOADING GAME");
            SaveGame A = loadWorld();
            StdDraw.clear();
            ter.initialize(A.randomstuff.length, A.randomstuff[0].length,5,5);
            drawFrame("Please chill");
            StdDraw.show();
            System.out.println(A.name);
            //  System.out.println(A.randomstuff[25][25].description());
            //System.out.println(A.randomstuff[0][0].description());
            this.temptiles = A.randomstuff;
            ter.renderFrame(this.temptiles);
            this.name = A.name;
            this.object = A.object;
            this.backmove = A.backmove;
            this.difficulty = A.difficulty;
            moveGuy(backmove);
        }
    }

    public void moveGuy(boolean backmove) {
        char a = 'r';
        String quit = "";
        StdDraw.enableDoubleBuffering();
        while (! quit.equals(":Q")) {
            StdDraw.setPenColor(Color.BLACK);
            StdDraw.filledRectangle(5, HEIGHT - 2, 7, 2);
            int mousex = (int) StdDraw.mouseX() - 5;
            int mousey = (int) StdDraw.mouseY() - 5;
            String b = "";
            if (mousex < 0 || mousey < 0) {
                if (mousex < 0) {
                    mousex = 0;
                }
                if (mousey < 0) {
                    mousey = 0;
                }
            }
            if (temptiles[mousex][mousey].equals(Tileset.WALL)) {
                System.out.println("YOU HIT A WALL");
                b = "WALL";
                flashMouse(b);
                b = "";
                drawMouseHeader(b);
            } else if (temptiles[mousex][mousey].equals(Tileset.FLOWER)) {
                System.out.println("DANGER FLOWERS ARE BAD");
                b = "FLOWER";
                flashMouse(b);
                b = "";
                drawMouseHeader(b);
            } else if (temptiles[mousex][mousey].equals(Tileset.GRASS)) {
                System.out.println("GO GRASS");
                b = "GRASS";
                flashMouse(b);
                b = "";
                drawMouseHeader(b);
            } else if (temptiles[mousex][mousey].equals(Tileset.FLOOR)) {
                System.out.println("YOU HIT A FLOOR");
                b = "FLOOR";
                //  System.out.println(a);
                flashMouse(b);
                b = "";
                drawMouseHeader(b);
            } else if (temptiles[mousex][mousey].equals(Tileset.SAND)){
                System.out.println("YOU HIT SAND");
                b = "SAND";
                flashMouse(b);
                b = "";
                drawMouseHeader(b);
            }
            else if (temptiles[mousex][mousey].equals(Tileset.WATER)){
                System.out.println("YO HIT WATER");
                b = "WATER";
                flashMouse(b);
                b = "";
                drawMouseHeader(b);
            }
            else if (temptiles[mousex][mousey].equals(Tileset.PLAYER)){
                System.out.println("PLAYER PLAYER PLAYER");
                b = "PLAYER";
                flashMouse(b);
                b = "";
                drawMouseHeader(b);
            }
            else if (temptiles[mousex][mousey].equals(Tileset.NOTHING)) {
                System.out.println("YOU GOT NOTHING");
                b = "NOTHING";
                flashMouse(b);
                b = "";
                drawMouseHeader(b);
            } else {
                System.out.println("ABSOUTELY DO NOTHING");
            }
            if ((StdDraw.hasNextKeyTyped())) {
                int win;
                a = StdDraw.nextKeyTyped();
                if (a == ':'){
                    quit += a;
                }
                if (a != 'Q') {
                    win = object.move(a, temptiles, backmove);

                    System.out.println(win);
                    if (win == 2) {
                        StdDraw.clear();
                        drawResult("YOU WON THE GAME!!! TO PLAY AGAIN PRESS 'N'. TO QUIT PRESS ANY OTHER KEY");
                        StdDraw.show();
                        char answer = getAnswer(1);
                        if (answer == 'N') {
                            drawResult("Please enter a seed. Type S when finished the seed");
                            StdDraw.show();
                            long seed = getRepeatSeed();
                            temptiles = generateWorld(seed, difficulty);
                            moveGuy(backmove);
                        } else {
                            System.exit(0);
                        }
                        System.out.println("I WONN!!!!");
                    } else if (win == 1) {
                        StdDraw.clear();
                        drawResult("YOU LOST THE GAME!!! TO PLAY AGAIN PRESS 'N'. TO QUIT PRESS ANY OTHER KEY");
                        StdDraw.show();
                        char answer = getAnswer(1);
                        if (answer == 'N') {
                            drawResult("Please enter a seed. Type S when finished the seed");
                            StdDraw.show();
                            long seed = getRepeatSeed();
                            temptiles = generateWorld(seed, difficulty);
                            moveGuy(backmove);
                        } else {
                            System.exit(0);
                        }
                        System.out.println("I LOSTTTT!!!!");
                    }
                }
                if (a == 'q') {
                    a = 'Q';
                }
                if (a == 'Q'){
                    quit  = quit + a;
                    System.out.println(quit);
                }

                System.out.println("RANDOM");
                ter.renderFrame(temptiles);

            }
            if (name.length() > 0) {
                drawNameHeader(name);
            }
            drawDiffHeader("Level: " + difficulty);
        }
        saveWorld(new SaveGame(object, temptiles, name, this.backmove, this.difficulty));
        System.out.println("WORLD BE SAVED");
        System.exit(0);
    }
    public void mover(char a) {
        object.move(a, temptiles, backmove);

    }





    public TETile[][] generateWorld(long seed, int difficulty) {
        TETile[][] randomTiles = new TETile[WIDTH][HEIGHT];
        object = new Test("n" + seed + "s");
        TETile[][] tiles = object.fillWithEmptyTiles(randomTiles);
        while (object.area() < 0.4) {
            object.activate(tiles);

        }
        object.wallmaker(tiles);
        object.wallmaker(tiles);
        object.wallmaker(tiles);
        object.createCharacter(tiles);
        object.createLoot(tiles);
        object.smoothing(tiles, difficulty);
        // object.smoothing(tiles);
        //drawNameHeader(name);
        //StdDraw.show();
        ter.renderFrame(randomTiles);
        return tiles;
    }

    public TETile[][] generateInputWorld(long seed, int difficulty) {
        TETile[][] randomTiles = new TETile[WIDTH][HEIGHT];
        object = new Test("n" + seed + "s");
        TETile[][] tiles = object.fillWithEmptyTiles(randomTiles);
        while (object.area() < 0.4) {
            object.activate(tiles);

        }
        object.wallmaker(tiles);
        object.wallmaker(tiles);
        object.wallmaker(tiles);
        object.createCharacter(tiles);
        //object.createLoot(tiles);
        // object.smoothing(tiles, difficulty);
        // object.smoothing(tiles);
        //drawNameHeader(name);
        //StdDraw.show();
        // ter.renderFrame(randomTiles);
        return tiles;
    }


    public void drawFrame(String s) {
        StdDraw.enableDoubleBuffering();
        StdDraw.clear();
        StdDraw.setPenColor(StdDraw.BLACK);
        Font font = new Font("Arial", Font.BOLD, 15);
        StdDraw.setFont(font);
        StdDraw.text(0.5, 0.5, s);
        StdDraw.show();
    }

    public void drawResult(String s) {
        StdDraw.enableDoubleBuffering();
        StdDraw.clear();
        StdDraw.setPenColor(StdDraw.BLACK);
        Font font = new Font("Arial", Font.BOLD, 15);
        StdDraw.setFont(font);
        StdDraw.text(25, 25, s);
        StdDraw.show();
    }

    public long getSeed() {
        String seed = "";
        char samp = 'N';
        while (samp != 's') {
            if (StdDraw.hasNextKeyTyped()) {
                samp = StdDraw.nextKeyTyped();
                seed += samp;
                if (samp == 'S'){
                    samp = 's';
                }
                drawFrame(seed);
            }

        }
        String string = seed.substring(0, seed.length() - 1);
        return Long.parseLong(string);
    }

    public long getRepeatSeed() {
        String seed = "";
        char samp = 'N';
        while (samp != 'S') {
            if (StdDraw.hasNextKeyTyped()) {
                samp = StdDraw.nextKeyTyped();
                seed += samp;
                drawResult(seed);
            }

        }
        String string = seed.substring(0, seed.length() - 1);
        return Long.parseLong(string);
    }

    public String getName() {
        String name = "";
        char samp = 'N';
        while (samp != '.') {
            if (StdDraw.hasNextKeyTyped()) {
                samp = StdDraw.nextKeyTyped();
                name += samp;
                drawFrame(name);
            }
        }
        String string = name.substring(0, name.length() - 1);
        return string;
    }

    public char getAnswer(int n) {
        char a = 'N';
        while (n > 0) {
            if (StdDraw.hasNextKeyTyped()) {

                a = StdDraw.nextKeyTyped();
                n = n - 1;
                drawFrame("" + a);
            }
        }
        return a;
    }


    public void loadFrame() {
        StdDraw.setPenColor(StdDraw.BLACK);
        Font font = new Font("Arial", Font.BOLD, 30);
        StdDraw.setFont(font);
        StdDraw.text(0.5, 0.75, "CS61B: THE GAME");
        Font titleStuff = new Font("Arial", Font.BOLD, 15);
        StdDraw.setFont(titleStuff);
        StdDraw.text(0.5, 0.5, "NEW GAME (N)");
        StdDraw.text(0.5, 0.4, "LOAD GAME (L)");
        StdDraw.text(0.5, 0.3, "QUIT (Q)");
        // StdDraw.text(0.5, 0.2, "NAME THE CHARACTER AND START GAME (P)");
    }

    public void drawMouseHeader(String s) {
        StdDraw.setPenColor(StdDraw.WHITE);
        Font font = new Font("Arial", Font.BOLD, 10);
        StdDraw.setFont(font);
        StdDraw.text(2, 48, s);
        StdDraw.show();
    }

    public void drawNameHeader(String s) {
        StdDraw.setPenColor(StdDraw.WHITE);
        Font font = new Font("Arial", Font.BOLD, 15);
        StdDraw.setFont(font);
        StdDraw.text(48, 48, s);
        StdDraw.show();
    }

    public void drawDiffHeader(String s) {
        StdDraw.setPenColor(StdDraw.WHITE);
        Font font = new Font("Arial", Font.BOLD, 15);
        StdDraw.setFont(font);
        StdDraw.text(25, 48, s);
        StdDraw.show();
    }

    public void flashMouse(String s) {
        StdDraw.enableDoubleBuffering();
        drawMouseHeader(s);
        StdDraw.pause(50);
        drawMouseHeader("");
        StdDraw.pause(100);
        StdDraw.show();
    }

    private SaveGame loadWorld() {
        File f = new File("./world.txt");
        if (f.exists()) {
            try {
                FileInputStream fs = new FileInputStream(f);
                ObjectInputStream os = new ObjectInputStream(fs);
                SaveGame loadWorld = (SaveGame) os.readObject();
                os.close();
                return loadWorld;
            } catch (FileNotFoundException e) {
                // System.out.println("file not found");
                System.exit(0);
            } catch (IOException e) {
                //System.out.println(e);
                System.exit(0);
            } catch (ClassNotFoundException e) {
                // System.out.println("class not found");
                System.exit(0);
            }
        }

        /* In the case no World has been saved yet, we return a new one. */
        return new SaveGame(object, temptiles, name, this.backmove, this.difficulty);
    }

    private void saveWorld(SaveGame w) {
        File f = new File("./world.txt");
        try {
            if (!f.exists()) {
                f.createNewFile();
            }
            FileOutputStream fs = new FileOutputStream(f);
            ObjectOutputStream os = new ObjectOutputStream(fs);
            os.writeObject(w);
            os.close();
        } catch (FileNotFoundException e) {
            //   System.out.println("file not found");
            System.exit(0);
        } catch (IOException e) {
            // System.out.println(e);
            System.exit(0);
        }
    }

    /**
     * Method used for autograding and testing the game code. The input string will be a series
     * of characters (for example, "n123sswwdasdassadwas", "n123sss:q", "lwww". The game should
     * behave exactly as if the user typed these characters into the game after playing
     * playWithKeyboard. If the string ends in ":q", the same world should be returned as if the
     * string did not end with q. For example "n123sss" and "n123sss:q" should return the same
     * world. However, the behavior is slightly different. After playing with "n123sss:q", the game
     * should save, and thus if we then called playWithInputString with the string "l", we'd expect
     * to get the exact same world back again, since this corresponds to loading the saved game.
     *
     * @param input the input string to feed to your progrls
     *              am
     * @return the 2D TETile[][] representing the state of the world
     */
    public TETile[][] playWithInputString(String input) {

        // and return a 2D tile representation of the world that would have been
        // drawn if the same inputs had been given to playWithKeyboard().

        int newIndex = 0;
        if (input.charAt(0) == 'N' || input.charAt(0) == 'n') {
            newIndex += 1;
            char test = 'a';
            char alpha = 'b';
            String seeds = "";
            int length1 = input.length();
            int i = 1;
            while (test != 's') {
                test = input.charAt(i);
                if (test == 'S') {
                    test = 's';
                }
                seeds += test;
                newIndex += 1;
                i += 1;
                if (i == input.length()) {
                    break;
                }

            }
            //  }
            long seed = Long.parseLong(seeds.substring(0, seeds.length() - 1));
            this.backmove = false;
            int temp = newIndex;
            temptiles = generateInputWorld(seed, difficulty);
            if (i == input.length()) {
                return temptiles;
            }
            int j = newIndex;
            while (alpha != ':') {
                alpha = input.charAt(j);
                mover(alpha);
                newIndex += 1;
                j += 1;
                if (j == input.length()) {
                    return temptiles;
                }
            }
        }
        // System.out.println("HiiiiELLO");
        if (input.charAt(newIndex) == 'Q' || input.charAt(newIndex) == 'q') {
            saveWorld(new SaveGame(object, temptiles, name, this.backmove, this.difficulty));
            return temptiles;
        } else if (input.charAt(0) == 'L' || input.charAt(0) == 'l') {
            newIndex += 1;
            SaveGame A = loadWorld();
            this.temptiles = A.randomstuff;
            this.name = A.name;
            this.object = A.object;
            this.backmove = A.backmove;
            this.difficulty = A.difficulty;
            char alpha = 'b';
            int temp = newIndex;
            int j = newIndex;
            while (alpha != ':') {
                alpha = input.charAt(j);
                mover(alpha);
                j += 1;
                newIndex += 1;
                if (j == input.length()) {
                    return temptiles;
                }
            }

            if (input.charAt(newIndex) == 'Q' || input.charAt(newIndex) == 'q') {
                saveWorld(new SaveGame(object, temptiles, name,
                        this.backmove, this.difficulty));
                return temptiles;
            }

        }
        //   System.out.println(temptiles);
        return temptiles;
    }

}
