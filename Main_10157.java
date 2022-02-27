import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_10157_염진호{
  static int R,C,K;
  static int[][] chk;
  static int[] dr={0,1,0,-1};
  static int[] dc={1,0,-1,0};
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    R=Integer.parseInt(st.nextToken());
    C=Integer.parseInt(st.nextToken());
    st=new StringTokenizer(br.readLine());
    K=Integer.parseInt(st.nextToken());

    chk=new int[R][C];
    chk[0][0]=1;

    int d=0;
    int r=0;
    int c=0;
    while(true){
      if(chk[r][c]==K){
        bw.write(r+1+" ");
        bw.write(c+1+"\n");
        break;
      }
      if(chk[r][c]==R*C){
        bw.write(0+"\n");
        break;
      }
      int tr=r+dr[d];
      int tc=c+dc[d];
      if(tr>=0 && tc>=0 && tr<R && tc<C && chk[tr][tc]==0){
          chk[tr][tc]=chk[r][c]+1;
          r=tr;
          c=tc;
      }else{
        d=(d+1)%4;
      }
    }
    bw.flush();
    bw.close();
    br.close();
  }
}