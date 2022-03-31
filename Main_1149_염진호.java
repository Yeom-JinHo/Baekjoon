import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_1149_염진호{
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N=Integer.parseInt(st.nextToken());
    int[][] houseColors =new int[N+1][3];
    int[][] dp = new int[N+1][3];
    for(int i=1;i<=N;i++){
      st=new StringTokenizer(br.readLine());
      houseColors[i][0]=Integer.parseInt(st.nextToken());//R
      houseColors[i][1]=Integer.parseInt(st.nextToken());//G
      houseColors[i][2]=Integer.parseInt(st.nextToken());//B
    }

    for(int i=1;i<=N;i++){
      dp[i][0]=Math.min(dp[i-1][1]+houseColors[i][0],dp[i-1][2]+houseColors[i][0]);
      dp[i][1]=Math.min(dp[i-1][0]+houseColors[i][1],dp[i-1][2]+houseColors[i][1]);
      dp[i][2]=Math.min(dp[i-1][0]+houseColors[i][2],dp[i-1][1]+houseColors[i][2]);
    }
    System.out.println(Math.min(dp[N][0],Math.min(dp[N][1], dp[N][2])));
    bw.flush();
    bw.close();
    br.close();
  }
}