package state;

import java.net.*;
import java.io.*;
import java.lang.String;


public class State {
    // TODO (minor): constructor should accept host&port
    private boolean no_error = false;
    private Socket socket;
    private DataOutputStream os;
    private BufferedReader is;
    private String out;

    State() {
        try {
                this.socket = new Socket("localhost", 12300);
                this.os = new DataOutputStream(
                    new BufferedOutputStream(this.socket.getOutputStream(), 4096)
                );
                this.is = new BufferedReader(
                    new InputStreamReader(this.socket.getInputStream())
                );
            } catch (UnknownHostException e) {
                this.err(e);
            } catch(IOException e) {
                this.err(e);
            }
            this.no_error = true;
    }

    private void err(Exception e) {
        this.no_error = false;
        e.printStackTrace();
    }

    private void fetch_output() {
        try {
            this.out = this.is.readLine();
        } catch(IOException e) {
            this.err(e);
            return;
        }
    }

    private boolean post_msg(String msg) {
        try {
            this.os.writeBytes(msg);
            this.os.writeBytes("\n");
            this.os.flush();
        } catch(IOException e) {
            this.err(e);
            return false;
        }

        this.fetch_output();
        return true;
    }

    public String get() {
        return this.out;
    }

    public void close() {
        try {
            this.os.close();
            this.is.close();
            this.socket.close();
        } catch(IOException e) {
            this.err(e);
        }
    }

    public boolean query(String varname) {
        if(! this.no_error) return false;

        return post_msg(varname);
    }

    public boolean set(String varname, String value) {
        if(! this.no_error) return false;

        return post_msg(varname + " " + value);
    }

    public static void main(String args[]) {
        State st = new State();
        st.set("test", "value");
        st.query("test");
        System.out.println(st.get());
        st.close();
    }
}
