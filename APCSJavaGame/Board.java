/*
 * Ayush Aggarwal, Arjun Mishra, Kedar Tallak
 * Board.java is a JPanel object that houses the Sprites, as well as the timer object
 * which controls the movement of the game and collision logic.
 * 
 */
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.Toolkit;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.Timer;
import java.util.TimerTask;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class Board extends JPanel{

	private final class CreateBarrierTask extends TimerTask { //creates barriers with an array of x values eliminating a random val
		
		private int delay;
		public CreateBarrierTask(int delay){
			this.delay = delay;
		}
		@Override
		public void run() {
			ArrayList <Sprite> newObjects = new ArrayList<Sprite>();
			int randomindex = ((int)(Math.random()*8));

			for (int k = 0; k < objects.size();k++ ){

				Rectangle r = new Rectangle(0,0,getWidth(),getHeight());
				if((r.intersects(objects.get(k).getHitBox()))){
					newObjects.add(objects.get(k));
				}
			}
			for (int k = 0; k < randomindex; k++){
				newObjects.add(new Teacher(xvalues[k],0));
			}
			for (int k = randomindex + 1; k < xvalues.length; k++){
				newObjects.add(new Teacher(xvalues[k],0));
			}
			score += .1;

			objects = newObjects;

			System.out.println("GPA: " + String.format("%.1f", score));
			timer.schedule(new CreateBarrierTask(delay - 10), delay);
		}
	}

	private Timer timer;
	private Player player;
	private ArrayList <Sprite> objects;
	private int[] xvalues;
	private double score;
	public final int STARTING = 0;
	public final int PLAYING = 1;
	public final int ENDING = 2;
	private int state;
	private int selectedChar;
	private Sprite char1;
	private Sprite char2;
	private Sprite char3;
	private Sprite[] chars;


	public Board(){//constructor
		super();
		xvalues = new int[]{0,64,128,256,192,320,384,448};
		objects = new ArrayList<Sprite>();
		state = STARTING;
		char1 = new Sprite(100,400);
		char2 = new Sprite(250,400);
		char3 = new Sprite(400,400);
		char1.loadImage("KEd.jpg");
		char2.loadImage("Ayush.jpg");
		char3.loadImage("Arj.jpg");
		chars = new Sprite[3];

		chars[0] = char1;
		chars[1] = char2;
		chars[2] = char3;




	}
	public void addSprite(Sprite newSprite){
		objects.add(newSprite);
	}

	@Override
	public void addNotify() {//start of the timer class, and sets up keylistener


		super.addNotify();
		timer = new Timer();
		System.out.println(getWidth() + " " + getHeight());
		addKeyListener(new KeyListener(){

			@Override
			public void keyTyped(KeyEvent e) {

			}

			@Override
			public void keyPressed(KeyEvent e) {
				if(e.getKeyCode() == KeyEvent.VK_ENTER){
					startGame();
				}
				else if(e.getKeyCode() == KeyEvent.VK_LEFT){
					selectedChar = (selectedChar + chars.length-1) % chars.length;
					repaint();
				}
				else if(e.getKeyCode() == KeyEvent.VK_RIGHT){
					selectedChar = (selectedChar + 1) % chars.length;
					repaint();
				}
				
			}

			@Override
			public void keyReleased(KeyEvent e) {
				// TODO Auto-generated method stub

			}


		});



	}

	public void startGame(){//initializes player selected and tells draw method to draw game screen
		player = new Player(chars[selectedChar].getX(),chars[selectedChar].getY(),this,chars[selectedChar]);
		timer.schedule(new CreateBarrierTask(3000), 100);

		addKeyListener(new KeyListener(){

			@Override
			public void keyTyped(KeyEvent e) {
				player.keyTyped(e);


			}

			@Override
			public void keyPressed(KeyEvent e) {

				player.keyPressed(e);
			}

			@Override
			public void keyReleased(KeyEvent e) {
				player.keyReleased(e);

			}


		});
		timer.scheduleAtFixedRate(new TimerTask(){
			@Override
			public void run() {

				update();
			}
		}, 100,10);
		this.state = PLAYING;
	}

	public void endGame(){ //stops timer and draws end screem
		timer.cancel();
		
		
		this.state = ENDING;
	}

	@Override
	public void paintComponent(Graphics g) {//depending on where in the game, draws the graphics
		super.paintComponent(g);
		if (state == STARTING){
			doStartDrawing(g);
			

		}
		else if (state == PLAYING){



			doDrawing(g);
			Toolkit.getDefaultToolkit().sync();


		}
		else if( state == ENDING){
			doEndDrawing(g);
		}
		setFocusable(true);
	}

	private void doDrawing(Graphics g) {

		g.setColor(Color.WHITE);
		g.fillRect(0, 0, getWidth(), getHeight());
		Graphics2D g2d = (Graphics2D) g;
		g2d.drawImage(player.getImage(), player.getX(), player.getY(), this);
		for(Sprite o : objects){
			g2d.drawImage(o.getImage(), o.getX(), o.getY(), this);
		}
		g.setColor(Color.BLACK);
		g.fillRect(375, 20, 440, 50);
		g.setColor(Color.WHITE);

		g.drawString("GPA: " + String.format("%.1f", score), 400, 50);
	}
	private void doEndDrawing(Graphics g) {

		g.setColor(Color.BLUE);
		g.fillRect(0, 0, getWidth(), getHeight());
		g.setColor(Color.BLACK);
		g.fillRect(190, 20, 130, 50);
		
		g.setColor(Color.WHITE);
		g.drawString("GPA: " + String.format("%.1f", score), 220, 40);
		g.drawString("THANKS FOR PLAYING! EXIT WINDOW TO LEAVE CLASS",100 , 300);
		
	}
	private void doStartDrawing(Graphics g) {
		
		Sprite selected = chars[selectedChar];
		int padding = 10;
		g.setColor(Color.WHITE);
		g.fillRect(0, 0, getWidth(), getHeight());
		g.setColor(Color.BLACK);
		g.drawRect(selected.getX() - padding, selected.getY() - padding, selected.getWidth() 
			+ 2*padding, selected.getHeight() + 2*padding);
		g.drawString("ESCAPE FROM APCS",200 , 80);
		g.drawString("CHOOSE CHARACTER AND AVOID THE WALLS",130 , 120);
		Graphics2D g2d = (Graphics2D) g;
		for (Sprite c : chars){
			g2d.drawImage(c.getImage(),c.getX(),c.getY(),this);
		}
		
	}

	private boolean collides(Bounded a, Bounded b){//how we handle collisions, using the rectangle class intersects method
		if(a.getBounds().intersects(b.getBounds())){
			return true;
		}
		return false;
	}
	private void update() {
		for (Sprite o : objects){
			o.move();
		}
		player.move();
		for (Sprite o : objects)
			if(collides(player, o)) {
				endGame();


			}
		repaint();
	}

}
