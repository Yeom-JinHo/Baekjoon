import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class JOL_1681_염진호{
  static int N,answer;
  static int[][] arr;
  static boolean[] chk;
  static int[] path;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N=Integer.parseInt(st.nextToken());
    arr=new int[N][N];
    chk=new boolean[2*N];
    path=new int[N-1];
    answer=Integer.MAX_VALUE;
    for(int r=0;r<N;r++){
      st=new StringTokenizer(br.readLine());
      for(int c=0;c<N;c++){
        arr[r][c]=Integer.parseInt(st.nextToken());
      }
    }
    chk[0]=true;
    dfs(0,0,0,0);
    bw.write(answer+"\n");
    bw.flush();
    bw.close();
    br.close();
  }
  static void dfs(int start,int dep,int total,int reverse){
    if(total>=answer)return;
    if(start==0 && reverse==N){
        answer=Math.min(answer,total);
        return;
    }
    if(dep==N-1){
      chk[start+N]=true;
      dfs(start,dep+1,total,N);
      return;
    }
    for(int i=0+reverse;i<N+reverse;i++){
      if(!chk[i] && arr[start][i%N]!=0){
        chk[i]=true;
        dfs(i%N,dep+1,total+arr[start][i%N],reverse);
        chk[i]=false;
      }
    }
  }
}