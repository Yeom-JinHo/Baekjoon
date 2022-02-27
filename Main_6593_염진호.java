import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main_6593_염진호{
  static int L,R,C;
  static int[][][] arr;
  static int sl,sr,sc,el,er,ec;
  static int[] dr={0,0,0,0,-1,1};
  static int[] dc={0,0,-1,1,0,0};
  static int[] dl={-1,1,0,0,0,0};
  static class Point{
    int l;
    int r;
    int c;
    public Point(int l,int r,int c){
      super();
      this.l=l;
      this.r=r;
      this.c=c;
    }
  }
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    while(true){
      StringTokenizer st = new StringTokenizer(br.readLine());
      L=Integer.parseInt(st.nextToken());
      R=Integer.parseInt(st.nextToken());
      C=Integer.parseInt(st.nextToken());
      if(L==0 && R==0 && C==0)break;
      arr=new int[L][R][C];
      for(int l=0;l<L;l++){
        for(int r=0;r<R;r++){
          String line=br.readLine();
          for(int c=0;c<C;c++){
            Character inp=line.charAt(c);
            if(inp=='S'){
              sl=l;
              sr=r;
              sc=c;
            }
            if(inp=='E'){
              el=l;
              er=r;
              ec=c;
            }
            if(inp=='#'){
              arr[l][r][c]=-1;
            }
          }
        }
        br.readLine();
      }
      bfs(sl,sr,sc);
      if(arr[el][er][ec]==0){
        bw.write("Trapped!\n");
      }else{
        bw.write("Escaped in "+arr[el][er][ec]+" minute(s).\n");
      }
    }
    bw.flush();
    bw.close();
    br.close();
  }
  static void bfs(int sl,int sr,int sc){
    arr[sl][sr][sc]=0;
    Queue<Point> que =new LinkedList<>();
    que.offer(new Point(sl,sr,sc));

    while(!que.isEmpty()){
      Point now=que.poll();
      for(int i=0;i<6;i++){
        int tr=now.r+dr[i];
        int tc=now.c+dc[i];
        int tl=now.l+dl[i];
        if(tr>=0 && tc>=0 && tl>=0 && tr<R && tc<C && tl<L){
          if(arr[tl][tr][tc]==0){
            arr[tl][tr][tc]=arr[now.l][now.r][now.c]+1;
            que.add(new Point(tl,tr,tc));
          }
        }
      }
    }
  }
}