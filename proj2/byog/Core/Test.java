package byog.Core;


import byog.TileEngine.TETile;
import byog.TileEngine.Tileset;

import java.io.Serializable;
import java.util.Random;
//@Source used some code from lab5

/**
 * Draws a world that contains RANDOM tiles.
 */
//00 is a good seed
//567 is a good seed
//1778 is a good seed
public class Test implements Serializable {
    private static final int WIDTH = 40;
    private static final int HEIGHT = 40;
    private double area = 0.0;
    private long SEED;
    private Random RANDOM;
    private int[] oldposition = new int[2];
    private int[] newposition = new int[2];

    public Test(String x) {
        long sum = 0;
        String string = x.substring(1, x.length() - 1);
        sum = Long.parseLong(string);
        SEED = sum;
        RANDOM = new Random(SEED);
    }

   /* public static void main(String[] args) {
        TERenderer ter = new TERenderer();
        ter.initialize(WIDTH, HEIGHT);

        TETile[][] randomTiles = new TETile[WIDTH][HEIGHT];
        Testingstuff object = new Testingstuff("n455857754086099036s");
        TETile[][] tiles = object.fillWithEmptyTiles(randomTiles);
        while (object.area < 0.3) {
            object.activate(tiles);

        }
        object.wallmaker(tiles);
        object.wallmaker(tiles);
        //runSmoothing(tiles);
        ter.renderFrame(randomTiles);
   */ // }

    public double area() {
        return this.area;
    }

    public boolean isFree(TETile[][] tiles, int xcoord, int ycoord, int xshift, int yshift) {
        if (ycoord + yshift > HEIGHT - 1 || xcoord + xshift > WIDTH - 1 || ycoord + yshift < 0
                || xcoord + xshift < 0) {
            return false;
        }
        if (ycoord < 0 || xcoord < 0) {
            return false;
        }
        for (int i = xcoord; i < xcoord + xshift; i++) {
            for (int j = ycoord; j < ycoord + yshift; j++) {
                if (!(tiles[i][j].equals(Tileset.NOTHING))) {
                    return false;
                }
            }
        }
        return true;
    }

    public void createCharacter(TETile[][] tiles) {
        tiles[oldposition[0]][oldposition[1]] = Tileset.PLAYER;
    }

    public void createLoot(TETile[][] tiles) {
        tiles[newposition[0]][newposition[1]] = Tileset.FLOWER;
    }

    public void wallmaker(TETile[][] tiles) {
        for (int i = 0; i < WIDTH; i++) {
            for (int j = 0; j < HEIGHT; j++) {
                if (i == 0 && j > 0 && i < WIDTH - 1 && j > 0 && j < HEIGHT - 1) {
                    if (tiles[i][j].equals(Tileset.FLOOR)) {
                        if (tiles[i + 1][j].equals(Tileset.NOTHING)) {
                            tiles[i + 1][j] = Tileset.WALL;
                        } else if (tiles[i][j + 1].equals(Tileset.NOTHING)) {
                            tiles[i][j + 1] = Tileset.WALL;
                        } else if (tiles[i][j - 1].equals(Tileset.NOTHING)) {
                            tiles[i][j - 1] = Tileset.WALL;
                        }
                    }
                } else if (j == 0 && i > 0 && i < WIDTH - 1 && j > 0 && j < HEIGHT - 1) {
                    if (tiles[i][j].equals(Tileset.FLOOR)) {
                        if (tiles[i + 1][j].equals(Tileset.NOTHING)) {
                            tiles[i + 1][j] = Tileset.WALL;
                        } else if (tiles[i - 1][j].equals(Tileset.NOTHING)) {
                            tiles[i - 1][j] = Tileset.WALL;
                        } else if (tiles[i][j + 1].equals(Tileset.NOTHING)) {
                            tiles[i][j + 1] = Tileset.WALL;
                        }
                    }
                } else if (j == HEIGHT - 1 && i > 0 && i < WIDTH - 1) {
                    if (tiles[i][j].equals(Tileset.FLOOR)) {
                        if (tiles[i + 1][j].equals(Tileset.NOTHING)) {
                            tiles[i + 1][j] = Tileset.WALL;
                        } else if (tiles[i - 1][j].equals(Tileset.NOTHING)) {
                            tiles[i - 1][j] = Tileset.WALL;
                        } else if (tiles[i][j - 1].equals(Tileset.NOTHING)) {
                            tiles[i][j - 1] = Tileset.WALL;
                        }
                    }
                } else if (i == WIDTH - 1 && j > 0 && j < HEIGHT - 1) {
                    if (tiles[i][j].equals(Tileset.FLOOR)) {
                        if (tiles[i][j + 1].equals(Tileset.NOTHING)) {
                            tiles[i][j + 1] = Tileset.WALL;
                        } else if (tiles[i - 1][j].equals(Tileset.NOTHING)) {
                            tiles[i - 1][j] = Tileset.WALL;
                        } else if (tiles[i][j - 1].equals(Tileset.NOTHING)) {
                            tiles[i][j - 1] = Tileset.WALL;
                        }

                    }
                } else if (i > 0 && i < WIDTH - 1 && j > 0 && j < HEIGHT - 1) {
                    if (tiles[i][j].equals(Tileset.FLOOR)) {
                        if (tiles[i + 1][j].equals(Tileset.NOTHING)) {
                            tiles[i + 1][j] = Tileset.WALL;
                        } else if (tiles[i - 1][j].equals(Tileset.NOTHING)) {
                            tiles[i - 1][j] = Tileset.WALL;
                        } else if (tiles[i][j + 1].equals(Tileset.NOTHING)) {
                            tiles[i][j + 1] = Tileset.WALL;
                        } else if (tiles[i][j - 1].equals(Tileset.NOTHING)) {
                            tiles[i][j - 1] = Tileset.WALL;
                        }
                    }
                }
            }
        }

    }

    public int move(char direction, TETile[][] random, boolean nobackmove) {
        int currentx = oldposition[0];
        int currenty = oldposition[1];

        if (direction == 'W' || direction == 'w') {
            System.out.println("UP");
            if (random[currentx][currenty + 1].equals(Tileset.WALL)) {
                System.out.println("DO NOTHING");
            } else if (random[currentx][currenty + 1].equals(Tileset.WATER)) {
                System.out.println("DO NOTHING");
            } else if ((random[currentx][currenty + 1].equals(Tileset.FLOWER))) {
                System.out.println("YOU WON");
                return 2;
            } else if ((random[currentx][currenty + 1].equals(Tileset.SAND))) {
                System.out.println("YOU LOST");
                return 1;
            } else {
                random[currentx][currenty + 1] = Tileset.PLAYER;
                random[currentx][currenty] = Tileset.FLOOR;
                if (nobackmove) {
                    random[currentx][currenty] = Tileset.WATER;
                }
                oldposition[1] = currenty + 1;
            }

        } else if (direction == 'A' || direction == 'a') {
            System.out.println("LEFT");
            if (random[currentx - 1][currenty].equals(Tileset.WALL)) {
                System.out.println("DO NOTHING");
            } else if (random[currentx - 1][currenty].equals(Tileset.WATER)) {
                  System.out.println("DO NOTHING");
                  } else if ((random[currentx - 1][currenty].equals(Tileset.FLOWER))) {
                     System.out.println("YOU WON");
                    return 2;
                } else if ((random[currentx - 1][currenty].equals(Tileset.SAND))) {
                  System.out.println("YOU LOST");
                  return 1;
            } else {
                random[currentx - 1][currenty] = Tileset.PLAYER;
                random[currentx][currenty] = Tileset.FLOOR;
                oldposition[0] = currentx - 1;
                      if (nobackmove) {
                          random[currentx][currenty] = Tileset.WATER;
                     }
            }

        } else if (direction == 'S' || direction == 's') {
            System.out.println("DOWN");
            if (random[currentx][currenty - 1].equals(Tileset.WALL)) {
                System.out.println("DO NOTHING");
            } else if (random[currentx][currenty - 1].equals(Tileset.WATER)) {
                  System.out.println("DO NOTHING");
                 } else if ((random[currentx][currenty - 1].equals(Tileset.FLOWER))) {
                    System.out.println("YOU WON");
                   return 2;
                } else if ((random[currentx][currenty - 1].equals(Tileset.SAND))) {
                   System.out.println("YOU LOST");
                  return 1;
            } else {
                random[currentx][currenty - 1] = Tileset.PLAYER;
                random[currentx][currenty] = Tileset.FLOOR;
                oldposition[1] = currenty - 1;
                    if (nobackmove) {
                       random[currentx][currenty] = Tileset.WATER;
                  }
            }
        } else if (direction == 'D' || direction == 'd') {
            System.out.println("RIGHT");
            if (random[currentx + 1][currenty].equals(Tileset.WALL)) {
                System.out.println("DO NOTHING");
            } else if (random[currentx + 1][currenty].equals(Tileset.WATER)) {
                  System.out.println("DO NOTHING");
                } else if ((random[currentx + 1][currenty].equals(Tileset.FLOWER))) {
                   System.out.println("YOU WON");
                   return 2;
                } else if ((random[currentx + 1][currenty].equals(Tileset.SAND))) {
                   System.out.println("YOU LOST");
                  return 1;
            } else {
                random[currentx + 1][currenty] = Tileset.PLAYER;
                random[currentx][currenty] = Tileset.FLOOR;
                oldposition[0] = currentx + 1;
                if (nobackmove) {
                    random[currentx][currenty] = Tileset.WATER;
                }
            }
        } else {
          System.out.println("INVALID INPUT");
         System.out.println(direction);
        }
        return 0;
    }

    public void createBlack(TETile[][] tiles) {
        for (int i = 1; i < HEIGHT - 3; i++) {
            tiles[i][0] = Tileset.WATER;

        }
    }

    public void smoothing(TETile[][] tiles, int difficulty) {

        for (int i = 1; i < WIDTH - 2; i++) {
            for (int j = 1; j < HEIGHT - 2; j++) {
                TETile[] temp = new TETile[9];
                int counter = 0;
                for (int a = -1; a < 2; a++) {
                    for (int b = -1; b < 2; b++) {

                        if ((i == 0 & j != 0) || (i == WIDTH - 1 && j != HEIGHT - 1)
                                || (i == 0 && j == 0)) {
                            continue;
                            //special edge case if we're on first column or last column
                        } else if ((i != 0 && j == 0) || (j == HEIGHT - 1 && i != WIDTH - 1)) {
                            //special case if we're on first row or last row
                            continue;
                        } else {
                            temp[counter] = tiles[i + a][j + b];
                        }
                        counter += 1;
                    }
                }
                int prob = RANDOM.nextInt(5);
                int floorcounter = 0;
                for (int z = 0; z < 9; z++) {
                    if (temp[z].description().equals("floor")) {
                        floorcounter += 1;
                    }
                }
                if (tiles[i][j].equals(Tileset.FLOOR) && floorcounter >= 8 && prob <= difficulty) {
                    tiles[i][j] = Tileset.SAND;
                }
            }
        }
    }

    public double makeRoom(TETile[][] tiles, int xcoord, int ycoord, int counter) {
        if (area > 0.3) {
            return 0.0;
        } else if (counter >= 15) {
            return 0.0;
        } else if (area < 0.3) {
            int height = tiles[0].length;
            int width = tiles.length;

            int tempwidth = RANDOM.nextInt(width - xcoord);
            int tempheight = RANDOM.nextInt(height - ycoord);
            if (tempheight <= 2 || tempwidth <= 2) {
                return makeRoom(tiles, xcoord, ycoord, counter + 1);
            }
            if (tempwidth > 8) {
                tempwidth = tempwidth / 2;
            }
            if (tempheight > 8) {
                tempheight = tempheight / 2;
            }
            if (isFree(tiles, xcoord, ycoord, tempwidth, tempheight)) {
                for (int x = 0; x < tempwidth; x += 1) {
                    for (int y = 0; y < tempheight; y += 1) {
                        tiles[xcoord + x][ycoord + y] = Tileset.FLOOR;
                    }
                }
            } else {
                return makeRoom(tiles, 2, 2, counter);
            }
            double a = tempheight * tempwidth;
            double temparea = WIDTH * HEIGHT;
            return a / temparea;
        }
        return 0.0;
    }

    public TETile[][] fillWithEmptyTiles(TETile[][] tiles) {
        int height = tiles[0].length;
        int width = tiles.length;

        for (int x = 0; x < width; x += 1) {
            for (int y = 0; y < height; y += 1) {
                tiles[x][y] = Tileset.NOTHING;
            }
        }
        return tiles;
    }

    public double connectingstuff(TETile[][] tiles) {
        int ydistance = newposition[1] - oldposition[1];
        int xdistance = newposition[0] - oldposition[0];
        int flipacoin = 0;
        int startingx = oldposition[0];
        int startingy = oldposition[1];
        if (ydistance + startingy >= HEIGHT || ydistance + startingy < 0
                || xdistance + startingx >= WIDTH
                || xdistance + startingx < 0) {
            return 0.0;
        }
        //if flip a coin is 0 we'll go horizontal first then go vertical other wise vice versa
        if (flipacoin == 0) {
            if (xdistance > 0 && ydistance > 0) {
                for (int i = 0; i < xdistance; i++) {
                    if (tiles[startingx + i][startingy].equals(Tileset.NOTHING)
                            || tiles[startingx + i][startingy].equals(Tileset.WALL)) {
                        tiles[startingx + i][startingy] = Tileset.FLOOR;
                    }
                }
                for (int i = 0; i < ydistance; i++) {
                    if (tiles[startingx + xdistance][startingy + i].equals(Tileset.NOTHING)
                            || tiles[startingx + xdistance][startingy + i].equals(Tileset.WALL)) {
                        tiles[startingx + xdistance][startingy + i] = Tileset.FLOOR;
                    }
                }
            } else if (xdistance > 0 && ydistance < 0) {
                for (int i = 0; i < xdistance; i++) {
                    if (tiles[startingx + i][startingy].equals(Tileset.NOTHING)
                            || tiles[startingx + i][startingy].equals(Tileset.WALL)) {
                        tiles[startingx + i][startingy] = Tileset.FLOOR;
                    }
                }
                for (int i = 0; i > ydistance; i--) {
                    if (tiles[startingx + xdistance][startingy + i].equals(Tileset.NOTHING)
                            || tiles[startingx + xdistance][startingy + i].equals(Tileset.WALL)) {
                        tiles[startingx + xdistance][startingy + i] = Tileset.FLOOR;
                    }
                }
            } else if (xdistance < 0 && ydistance > 0) {
                for (int i = 0; i > xdistance; i--) {
                    if (tiles[startingx + i][startingy].equals(Tileset.NOTHING)
                            || tiles[startingx + i][startingy].equals(Tileset.WALL)) {
                        tiles[startingx + i][startingy] = Tileset.FLOOR;
                    }
                }
                for (int i = 0; i < ydistance; i++) {
                    if (tiles[startingx + xdistance][startingy + i].equals(Tileset.NOTHING)
                            || tiles[startingx + xdistance][startingy + i].equals(Tileset.WALL)) {
                        tiles[startingx + xdistance][startingy + i] = Tileset.FLOOR;
                    }
                }
            } else {
                //case where they are both negative
                for (int i = 0; i > xdistance; i--) {
                    if (tiles[startingx + i][startingy].equals(Tileset.NOTHING)
                            || tiles[startingx + i][startingy].equals(Tileset.WALL)) {
                        tiles[startingx + i][startingy] = Tileset.FLOOR;
                    }
                }
                for (int i = 0; i > ydistance; i--) {
                    if (tiles[startingx + xdistance][startingy + i].equals(Tileset.NOTHING)
                            || tiles[startingx + xdistance][startingy + i].equals(Tileset.WALL)) {
                        tiles[startingx + xdistance][startingy + i] = Tileset.FLOOR;
                    }
                }
            }
        }
        double a = (double) (Math.abs(ydistance) + Math.abs(xdistance));
        double temparea = (double) WIDTH * HEIGHT;
        return a / temparea;
    }

    public void activate(TETile[][] tiles) {
        if (oldposition[0] == 0.0 && newposition[0] == 0.0) {

            int tempwidth = Math.abs(RANDOM.nextInt(WIDTH));
            int tempheight = Math.abs(RANDOM.nextInt(HEIGHT));
            this.oldposition[0] = tempwidth;
            this.oldposition[1] = tempheight;
            area += makeRoom(tiles, tempwidth, tempheight, 0);
            int anotherwidth = Math.abs(RANDOM.nextInt(WIDTH));
            int anotherheight = Math.abs(RANDOM.nextInt(HEIGHT));
            this.newposition[0] = anotherwidth;
            this.newposition[1] = anotherheight;
            area += makeRoom(tiles, anotherwidth, anotherheight, 0);
            area += connectingstuff(tiles);
            oldposition[0] = newposition[0];
            oldposition[1] = newposition[1];
        } else {
            int anotherwidth = Math.abs(RANDOM.nextInt(WIDTH));
            int anotherheight = Math.abs(RANDOM.nextInt(HEIGHT));
            this.newposition[0] = anotherwidth;
            this.newposition[1] = anotherheight;

            area += makeRoom(tiles, anotherwidth, anotherheight, 0);
            area += connectingstuff(tiles);

        }
    }


}

