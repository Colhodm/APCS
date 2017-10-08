/*
 * Ayush Aggarwal, Arjun Mishra, Kedar Tallak
 * EscapeFromAPCS.java is the main which constructs the Board and starts the game
 * 
 */
import java.awt.EventQueue;
import javax.swing.JFrame;



public class EscapeFromAPCS extends JFrame {
	
	public EscapeFromAPCS() {

		initUI();
	}

	private void initUI() {

		add(new Board());

		setSize(512, 600);
		setResizable(false);

		setTitle("Escape From APCS");
		setLocationRelativeTo(null);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	

	

	public static void main(String[] args) {
		

		EventQueue.invokeLater(new Runnable() {
			@Override
			public void run() {

				EscapeFromAPCS ex = new EscapeFromAPCS();
				ex.setVisible(true);
				
				
			}
		});
	}

}



