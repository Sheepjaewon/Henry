import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class Calculator {

    private JFrame frame;
    private JLabel label;
    private JButton[] numberButtons;
    private JButton[] operatorButtons;

    public Calculator() {
        frame = new JFrame("계산기");
        frame.setSize(300, 300);
        frame.setLayout(new FlowLayout());

        label = new JLabel("0");
        frame.add(label);

        numberButtons = new JButton[10];
        for (int i = 0; i < numberButtons.length; i++) {
            numberButtons[i] = new JButton(String.valueOf(i));
            numberButtons[i].addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    updateLabel(e.getSource());
                }
            });
            frame.add(numberButtons[i]);
        }

        operatorButtons = new JButton[4];
        operatorButtons[0] = new JButton("+");
        operatorButtons[1] = new JButton("-");
        operatorButtons[2] = new JButton("*");
        operatorButtons[3] = new JButton("/");
        for (int i = 0; i < operatorButtons.length; i++) {
            operatorButtons[i].addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    updateLabel(e.getSource());
                }
            });
            frame.add(operatorButtons[i]);
        }

        frame.setVisible(true);
    }

    private void updateLabel(Object source) {
        String text = label.getText();
        String buttonText = ((JButton) source).getText();

        if (buttonText.equals("=")) {
            int result = calculate(text);
            label.setText(String.valueOf(result));
        } else {
            label.setText(text + buttonText);
        }
    }

    private int calculate(String expression) {
        int result = 0;
        int operand1 = Integer.parseInt(expression.substring(0, expression.length() - 1));
        char operator = expression.charAt(expression.length() - 1);

        switch (operator) {
            case '+':
                result = operand1 + 1;
                break;
            case '-':
                result = operand1 - 1;
                break;
            case '*':
                result = operand1 * 1;
                break;
            case '/':
                result = operand1 / 1;
                break;
        }

        return result;
    }

    public static void main(String[] args) {
        new Calculator();
    }
}
