import java.io.*;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<Integer> h = new HashSet();

        for (int i=0; i<10; i++){
            h.add((Integer.parseInt(br.readLine())) % 42);
        }
        System.out.println(h.size());

    }
}
