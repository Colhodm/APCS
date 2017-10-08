/*
 * Ayush Aggarwal, Arjun Mishra, Kedar Tallak
 * Sprite class houses images, with information for the position and dimensions of the image
 * 
 */
import java.awt.Image;
import java.awt.Rectangle;
import java.awt.geom.Rectangle2D;
import java.awt.geom.Rectangle2D.Double;

import javax.swing.ImageIcon;

public class Sprite implements Bounded{

	protected int x;
	protected int y;
	protected int width;
	protected int height;
	protected boolean vis;
	protected Image image;

	public int getWidth() {
		return width;
	}

	public int getHeight() {
		return height;
	}

	public boolean isVis() {
		return vis;
	}

	public Sprite(int x, int y) {

		this.x = x;
		this.y = y;
		vis = true;
	}

	protected void loadImage(String imageName) {

		ImageIcon ii = new ImageIcon(imageName);
		image = ii.getImage();
		getImageDimensions();
	}

	protected void getImageDimensions() {

		width = image.getWidth(null);
		height = image.getHeight(null);
	}    

	public Image getImage() {
		return image;
	}

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}
	
	

	public boolean isVisible() {
		return vis;
	}

	public void setVisible(Boolean visible) {
		vis = visible;
	}

	public Rectangle getBounds() {
		// TODO Auto-generated method stub
		return getHitBox();
	}
	public void move(){
		
	}
	public Rectangle getHitBox(){
		//System.out.println("Bounds: " + getX() + ", " + getY() + " ; " + width + " x " + height);
		return new Rectangle(getX(),getY(),width,height);
	}
}



