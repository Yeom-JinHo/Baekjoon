import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main_1026_염진호{
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N=Integer.parseInt(st.nextToken());
    int[] a=new int[N];
    int[] b=new int[N];

    st=new StringTokenizer(br.readLine());
    for(int i=0; i<N;i++){
      a[i]=Integer.parseInt(st.nextToken());
    }
    st=new StringTokenizer(br.readLine());
    for(int i=0; i<N;i++){
      b[i]=Integer.parseInt(st.nextToken());
    }
    Arrays.sort(a);
    Arrays.sort(b);
    int answer=0;
    for(int i=0;i<N;i++){
      answer+=a[i]*b[N-1-i];
    }
    bw.write(answer+"\n");
    bw.flush();
    bw.close();
    br.close();
  }
}