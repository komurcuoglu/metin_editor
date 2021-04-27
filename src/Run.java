
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.Timer;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author HÜSEYİN AFSİN
 */
public class Run {public static int gecenzaman=0;
public   static Timer zamanlayici=null;
    public static void main(String[] args) {
    Editor editor=new Editor();
        Toolkit.getDefaultToolkit().getImage(Editor.class.getResource("images/logo.png"));

        Loading baslat= new Loading();
        LogoEkrani logoEkrani =new LogoEkrani();
        logoEkrani.setVisible(true);
     zamanlayici=new Timer(2000, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {gecenzaman++;
                System.out.println(gecenzaman);

                // baslat.setVisible(true);
                if (gecenzaman==3) {
                    logoEkrani.setVisible(false);
                    baslat.setVisible(true);

                }
                if (gecenzaman==6){
                    baslat.setVisible(false);
                    zamanlayici.stop();
                    editor.setVisible(true);
                }
            }
        });

        zamanlayici.start();




    }

}
