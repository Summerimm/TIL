import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int mx = 0;
        double[] arr = new double[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++){
            int value = Integer.parseInt(st.nextToken());
            arr[i] = value;

            if (value > mx){
                mx = value;
            }
        }

        for (int i=0; i<N; i++) {
            arr[i] = arr[i] / mx * 100;
        }

        double avg = Arrays.stream(arr).average().orElse(0);
        System.out.println(avg);
    }
}
