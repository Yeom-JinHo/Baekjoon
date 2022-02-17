import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_1987_염진호{
  static int R,C,answer;
  static char[][] arr;
  static boolean[] chk;
  static int[] dr={-1,1,0,0};
  static int[] dc={0,0,-1,1};
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    StringTokenizer st = new StringTokenizer(br.readLine());
    R=Integer.parseInt(st.nextToken());
    C=Integer.parseInt(st.nextToken());
    arr=new char[R][C];
    chk=new boolean[26];
    for(int r=0;r<R;r++){
      st=new StringTokenizer(br.readLine());
      arr[r]=st.nextToken().toCharArray();
    }
    answer=0;
    chk[arr[0][0]-'A']=true;
    dfs(0,0,1);
    bw.write(answer+"\n");
    bw.flush();
    bw.close();
    br.close();
  }
  static void dfs(int sr,int sc,int dep){
    answer=Math.max(answer, dep);
    for(int i=0;i<4;i++){
      int tr=sr+dr[i];
      int tc=sc+dc[i];
      if(tr>=0 && tc>=0 && tr<R && tc<C){
        if(!chk[arr[tr][tc]-'A']){
          chk[arr[tr][tc]-'A']=true;
          dfs(tr,tc,dep+1);
          chk[arr[tr][tc]-'A']=false;
        }
      }
    }
  }
}