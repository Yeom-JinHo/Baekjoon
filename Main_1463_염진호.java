import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_1463_염진호{
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N=Integer.parseInt(st.nextToken());
    int[] dp=new int[N+1];
    dp[1]=0;
    for(int i=2;i<=N;i++){
      int min=dp[i-1]+1;
      if(i%3==0){
        min=Math.min(dp[i/3]+1,min);
      }
      if(i%2==0){
        min=Math.min(dp[i/2]+1,min);
      }
      dp[i]=min;
    }
    System.out.println(dp[N]);
    bw.flush();
    bw.close();
    br.close();
  }
}