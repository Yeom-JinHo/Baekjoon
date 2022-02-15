import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main{
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    StringTokenizer st = new StringTokenizer(br.readLine());
    int N=Integer.parseInt(st.nextToken());
    int[] dp=new int[5001];
    for(int i=0;i<5001;i++){
      dp[i]=Integer.MAX_VALUE;
    }
    dp[3]=1;
    dp[5]=1;
    for(int i=6;i<=N;i++){
      if(dp[i-3]!=Integer.MAX_VALUE)
        dp[i]=Math.min(dp[i],dp[i-3]+1);
      if(dp[i-5]!=Integer.MAX_VALUE)
        dp[i]=Math.min(dp[i],dp[i-5]+1);
    }
    if(dp[N]!=Integer.MAX_VALUE)
      bw.write(dp[N]+"\n");
    else:
      bw.write("-1"+"\n");
    bw.flush();
    bw.close();
    br.close();
  }
}