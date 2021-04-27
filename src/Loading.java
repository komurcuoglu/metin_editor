
import java.awt.*;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.BorderLayout;
import javax.swing.JLabel;
import javax.swing.ImageIcon;

public class Loading extends JFrame {
    JPanel contentPane;
    JLabel giflabel = new JLabel();

    public Loading() {
        try {
            contentPane = (JPanel) getContentPane();
            contentPane.setLayout(new BorderLayout());
            setSize(new Dimension(254, 254  ));
            ImageIcon resim = new ImageIcon(this.getClass().getResource("images/load.gif"));
            giflabel.setIcon(resim);
            contentPane.add(giflabel, java.awt.BorderLayout.CENTER);
            setUndecorated(true);
           setBackground(new Color(0f,0f,0f,0f));
            this.setLocationRelativeTo(null);
        } catch (Exception exception) {
            exception.printStackTrace();
        }
    }


}