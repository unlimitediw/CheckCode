import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.jar.JarInputStream;

public class newGUInew extends JDialog {
    private JPanel contentPane;
    private JarInputStream input;
    private JButton buttonSager;

    public newGUInew() {
        setContentPane(contentPane);
        setModal(true);
        getRootPane().setDefaultButton(buttonOK);

        buttonSager.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                onOK();
            }
        });
    }

    private void onOK() {
        System.out.println(input);
    }



    public static void main(String[] args) {
        newGUInew dialog = new newGUInew();
        dialog.pack();
        dialog.setVisible(true);
        System.exit(0);
    }
}
