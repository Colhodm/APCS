/*
 * Ayush Aggarwal, Arjun Mishra, Kedar Tallak
 * Player.java holds the image and logic of the Sprite that is the character of the game
 * including its position, which changes by the user
 * 
 */
import java.awt.Image;
import java.awt.Rectangle;
import java.awt.event.KeyEvent;
import java.util.HashMap;

public class Player implements Bounded {
	public static final int UP = 0;
	public static final int DOWN = 1;
	public static final int LEFT = 2;
	public static final int RIGHT = 3;
	private int dy, dx;
	private double x;
	private double y;
	private int direction;
	private Sprite[] playerImages;
	private HashMap <Integer , Boolean> keysPressed;
	private Board theBoard;
	private int width;
	private int height;

	public Player(int x, int y, Board board, Sprite character){
		theBoard = board;
		playerImages = new Sprite[4];
		this.x = x;
		this.y = y;
		playerImages[UP] = character;
		width = playerImages[UP].width;
		height = playerImages[UP].height;
		keysPressed = new HashMap<Integer , Boolean>();
		keysPressed.put(KeyEvent.VK_UP, false);
		keysPressed.put(KeyEvent.VK_DOWN, false);
		keysPressed.put(KeyEvent.VK_LEFT, false);
		keysPressed.put(KeyEvent.VK_RIGHT, false);

	}
	public Image getImage() {
		return playerImages[UP].getImage();
	}
	public int getX(){
		return (int) Math.round(x);
	}
	public int getY(){
		return (int) Math.round(y);
	}
	public void move() {//takes input from player and changes direction
		double speed = 2;
		final double SQRT2_2 = Math.sqrt(2)/2;//normalizes speed so it isn't double when two keys pressed
		
		if (keysPressed.get(KeyEvent.VK_DOWN) && keysPressed.get(KeyEvent.VK_LEFT)){
			y += speed*SQRT2_2;
			x -= speed*SQRT2_2;
		}
		else if (keysPressed.get(KeyEvent.VK_DOWN) && keysPressed.get(KeyEvent.VK_RIGHT)){
			y += speed*SQRT2_2;
			x += speed*SQRT2_2;
		}
		else if (keysPressed.get(KeyEvent.VK_UP) && keysPressed.get(KeyEvent.VK_LEFT)){
			y -= speed*SQRT2_2;
			x -= speed*SQRT2_2;
		}
		else if (keysPressed.get(KeyEvent.VK_UP) && keysPressed.get(KeyEvent.VK_RIGHT)){
			y -= speed*SQRT2_2;
			x += speed*SQRT2_2;
		}
		else if (keysPressed.get(KeyEvent.VK_UP))
			y -= speed;
		else if (keysPressed.get(KeyEvent.VK_DOWN))
			y += speed;
		else if (keysPressed.get(KeyEvent.VK_LEFT))
			x -= speed;
		else if (keysPressed.get(KeyEvent.VK_RIGHT))
			x += speed;
		if(x > theBoard.getWidth() - 48){//to keep player on screen
			x = theBoard.getWidth() - 48;
		}
		else if(x < 0){
			x = 0;
		}
		if(y> theBoard.getHeight() - 48){
			y = theBoard.getHeight() - 48;
		}
		else if(y < 0){
			y = 0;
		}
		
	}
	
	public void keyTyped(KeyEvent e){
		//System.err.println("Typed CAlled");
		int key = e.getKeyCode();
	}
	
	public void keyPressed(KeyEvent e) {//input from users
		int key = e.getKeyCode();
		keysPressed.put(e.getKeyCode(), true);
		if(e.getKeyCode() == KeyEvent.VK_UP){
			direction = UP;
		}
		else if(e.getKeyCode() == KeyEvent.VK_DOWN){
			direction = DOWN;
		}
		else if(e.getKeyCode() == KeyEvent.VK_LEFT){
			direction = LEFT;
		}
		else if(e.getKeyCode() == KeyEvent.VK_RIGHT){
			direction = RIGHT;
		}
	}
	public void keyReleased(KeyEvent e) {
		keysPressed.put(e.getKeyCode(), false);
	}
	public Rectangle getBounds(){
		return new Rectangle(getX(), getY(), width, height);
	}
}