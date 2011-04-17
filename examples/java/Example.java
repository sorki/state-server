import state.*;

public class Example {
    public static void main(String args[]) {
        State st = new State();

        if(st.query("test")) {
            System.out.println(st.get());
        }

        st.set("test", "value");

        if(st.query("test")) {
            System.out.println(st.get());
        }

        st.close();
    }
}
