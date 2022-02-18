import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_10819_염진호 {
  static int N,answer;
  static int[] inp,tmp;
  static boolean[] chk;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N=Integer.parseInt(st.nextToken());
    inp=new int[N];
    tmp=new int[N];
    chk=new boolean[N];
    answer=0;
    st=new StringTokenizer(br.readLine());
    for(int i=0;i<N;i++){
      inp[i]=Integer.parseInt(st.nextToken());
    }
    per(0);
    bw.write(answer+"\n");
    bw.flush();
    bw.close();
    br.close();
  }
  static void per(int cnt){
    if(cnt==N){
      int val=0;
      for(int i=0; i<N-1;i++){
        val+=Math.abs(tmp[i]-tmp[i+1]);
      }
      answer=Math.max(answer, val);
    }else{
      for(int i=0;i<N;i++){
        if(!chk[i]){
          chk[i]=true;
          tmp[cnt]=inp[i];
          per(cnt+1);
          chk[i]=false;
        }
      }
    }
  }
}