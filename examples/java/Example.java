import state.*;

public class Example {
    public static void main(String args[]) {
        State st = new State();
        st.set("test", "value");
        st.query("test");
        System.out.println(st.get());
        st.close();
    }
}
