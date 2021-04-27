
import java.awt.*;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.BorderLayout;
import javax.swing.JLabel;
import javax.swing.ImageIcon;

public class LogoEkrani extends JFrame {
    JPanel contentPane;
    JLabel giflabel = new JLabel();

    public LogoEkrani() {
        try {
            contentPane = (JPanel) getContentPane();
            contentPane.setLayout(new BorderLayout());
            setSize(new Dimension(344, 295  ));
            ImageIcon resim = new ImageIcon(this.getClass().getResource("images/lica344x295.png"));
            giflabel.setIcon(resim);
            contentPane.add(giflabel, java.awt.BorderLayout.CENTER);
            this.setLocationRelativeTo(null);
            setUndecorated(true);
        } catch (Exception exception) {
            exception.printStackTrace();
        }
    }


}