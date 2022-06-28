import com.mysql.jdbc.PreparedStatement;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.*;

public class Contactos {
    private JPanel Main;
    private JTextField textName;
    private JTextField texTelefono;
    private JTextField textEmail;
    private JButton guardarButton;
    private JTable table1;
    private JButton modificarButton;
    private JButton eliminarButton;
    private JButton buscarButton;
    private JTextField textid;
    private JScrollPane table_1;

    public static void main(String[] args) {
        JFrame frame = new JFrame("Contactos");
        frame.setContentPane(new Contactos().Main);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
    Connection con;
    PreparedStatement pst;
    public void connect()
    {
        try {
        Class.forName("com.mysql.jdbc.Driver");
        con = DriverManager.getConnection("jdbc:mysql://localhost/dbcontactos", "root","");
        System.out.println("Successs");
        }
         catch (ClassNotFoundException ex)
        {
            ex.printStackTrace();

        }

    }
    void table_load()
    {
        try
        {
            pst = (PreparedStatement) con.prepareStatement("select * from datos contactos");
            ResultSet rs = pst.executeQuery();
            table_1.setModel(DbUtils.resultSetToTableModel(rs));
        }
        catch (SQLException e)
        {
            e.printStackTrace();
        }
    }
    


    public Contactos() {
        connect();
        table_load();
        guardarButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                String nombre,telefono,email;

                nombre=textName.getText();
                telefono=texTelefono.getText();
                e-mail=textEmail.getText();

                try {
                    pst = (PreparedStatement) con.prepareStatement("insert into datos contactos(nombre,telefono,email)values(?,?,?)");
                    pst.setString(1, nombre);
                    pst.setString(2, telefono);
                    pst.setString(3, email);
                    pst.executeUpdate();
                    JOptionPane.showMessageDialog(null, "Record Addedddd!!!!!");
                    //table_load();
                    textName.setText("");
                    texTelefono.setText("");
                    textEmail.setText("");
                    textName.requestFocus();
                }

                catch (SQLException e1)
                {

                    e1.printStackTrace();
                }



            }
        });
        buscarButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                try {

                    String empid = textid.getText();

                    pst = con.prepareStatement("select nombre,telefono,e-mail from datos contactos where id = ?");
                    pst.setString(1, empid);
                    ResultSet rs = pst.executeQuery();

                    if(rs.next()==true)
                    {
                        String emnombre = rs.getString(1);
                        String emtelefono = rs.getString(2);
                        String ememail = rs.getString(3);

                        textName.setText(emnombre);
                        texTelefono.setText(emtelefono);
                        textEmail.setText(ememail);

                    }
                    else
                    {
                        textName.setText("");
                        texTelefono.setText("");
                        textEmail.setText("");
                        JOptionPane.showMessageDialog(null,"Invalid datos contactos No");
            }
        });
    }
}
modificarButton.addActionListener(new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {

        String empid, nombre,telefono,e-mail;

        nombre=textName.getText();
        telefono=texTelefono.getText();
        e-mail=textEmail.getText();
        empid=textid.getText();
    }
        try {
            pst = con.prepareStatement("update datos contactos set empname = ?,telefono = ?,e-mail = ? where id = ?");
            pst.setString(1, empname);
            pst.setString(2, telefono);
            pst.setString(3,email);
            pst.setString(4, empid);

            pst.executeUpdate();
            JOptionPane.showMessageDialog(null, "Record Updateee!!!!!");
            table_load();
            textName.setText("");
            texTelefono.setText("");
            textEmail.setText("");
            textName.requestFocus();
        }

        catch (SQLException e1)
        {
            e1.printStackTrace();
        }
    }

        eliminarButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String empid;
                empid = txtid.getText();

                try {
                    pst = con.prepareStatement("delete from datos contactos  where id = ?");

                    pst.setString(1, empid);

                    pst.executeUpdate();
                    JOptionPane.showMessageDialog(null, "Record Deleteeeeee!!!!!");
                    table_load();
                    textName.setText("");
                    texTelefono.setText("");
                    textEmail.setText("");
                    textName.requestFocus();
                }

                catch (SQLException e1)
                {

                    e1.printStackTrace();
                }
            }
        });
    }
});