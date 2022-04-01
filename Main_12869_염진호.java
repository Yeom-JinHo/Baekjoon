import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_12869_염진호{
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int[][] attacks ={{9,3,1},{9,1,3},{1,3,9},{1,9,3},{3,1,9},{3,9,1}};
    int MAX_SIZE =61;
    int N =Integer.parseInt(st.nextToken());
    int[][][] dp =new int[MAX_SIZE][MAX_SIZE][MAX_SIZE];
    int [] scv=new int[3];
    st=new StringTokenizer(br.readLine());
    for(int i=0;i<N;i++){
      scv[i]=Integer.parseInt(st.nextToken());
    }

    for(int r=0; r<MAX_SIZE;r++){
      for(int c=0; c<MAX_SIZE;c++){
        for(int d=0; d<MAX_SIZE;d++){
          dp[r][c][d]=Integer.MAX_VALUE;
        }
      }
    }
    for(int r=0; r<MAX_SIZE;r++){
      for(int c=0; c<MAX_SIZE;c++){
        for(int d=0; d<MAX_SIZE;d++){
          if(r==0 && c==0 && d==0){
            dp[0][0][0]=0;
            continue;
          }
          int minValue=MAX_SIZE;
          for(int i=0;i<attacks.length;i++){
            int tr=r-attacks[i][0]>=0?r-attacks[i][0]:0;
            int tc=c-attacks[i][1]>=0?c-attacks[i][1]:0;
            int td=d-attacks[i][2]>=0?d-attacks[i][2]:0;
            minValue=Math.min(minValue,dp[tr][tc][td]+1);
          }
          dp[r][c][d]=minValue;
        }
      }
    }
    System.out.println(dp[scv[0]][scv[1]][scv[2]]);
    bw.flush();
    bw.close();
    br.close();
  }
}