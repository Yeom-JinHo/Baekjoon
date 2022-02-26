import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main_7576_염진호{
  static int R,C;
  static int[][] arr;
  static Queue<Tomato> que;
  static int[] dr={-1,1,0,0};
  static int[] dc={0,0,-1,1};
  static class Tomato{
    int r;
    int c;
    int date;
    public Tomato(int r,int c,int date){
      super();
      this.r=r;
      this.c=c;
      this.date=date;
    }
  }
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    C=Integer.parseInt(st.nextToken());
    R=Integer.parseInt(st.nextToken());

    arr=new int[R][C];
    que=new LinkedList<>();
    for(int r=0;r<R;r++){
      st=new StringTokenizer(br.readLine());
      for(int c=0;c<C;c++){
        arr[r][c]=Integer.parseInt(st.nextToken());
      }
    }
    for(int r=0;r<R;r++){
      for(int c=0;c<C;c++){
        if(arr[r][c]==1){
          que.add(new Tomato(r, c, 1));
        }
      }
    }
    bfs();

    int answer=0;
    for(int r=0;r<R;r++){
      for(int c=0;c<C;c++){
        if(arr[r][c]==-1)continue;
        if(arr[r][c]==0)answer=Integer.MAX_VALUE;
        answer=Math.max(answer,arr[r][c]);
      }
    }
    if(answer==Integer.MAX_VALUE){
      answer=0;
    }
    bw.write(answer-1+"\n");
    bw.flush();
    bw.close();
    br.close();
  }

  static void bfs(){
    while(!que.isEmpty()){
      Tomato now=que.poll();
      for(int i=0;i<4;i++){
        int tr=now.r+dr[i];
        int tc=now.c+dc[i];
        if(tr>=0 && tc>=0 && tr<R && tc<C){
          if(arr[tr][tc]==0){
            arr[tr][tc]=now.date+1;
            que.add(new Tomato(tr, tc, now.date+1));
          }
        }
      }
    }
  }
}