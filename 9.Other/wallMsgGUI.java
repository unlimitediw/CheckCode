import javax.swing.*;
import javax.swing.JPanel;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class wallMsgGUI {
    private JButton ShowWall;
    private JPanel GUIPanel;
    private JTextField userIDText;
    private JTextArea textArea1;

    public wallMsgGUI() {
        ShowWall.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                wallMsgSQL thisMsg = new wallMsgSQL(Integer.valueOf(userIDText.getText()).intValue());
                System.out.println(thisMsg.outputString);
                textArea1.setText(thisMsg.outputString);
            }
        });
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("wallMsgGUI");
        frame.setContentPane(new wallMsgGUI().GUIPanel);
        frame.setVisible(true);
    }
}
