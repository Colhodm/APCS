/*
 * Ayush Aggarwal, Arjun Mishra, Kedar Tallak
 * teacher.java is just the walls, with a simple move method of moving down the screen
 * 
 */
public class Teacher extends Sprite{


	public Teacher(int x, int y) {
		super(x, y);
		
		loadImage("teacher.jpg");
	
	}
	
	public void move(){
		y += 1;
	}
	

	
	
}
