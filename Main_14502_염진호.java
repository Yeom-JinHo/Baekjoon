import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main_14502_염진호{
  static int R,C,answer;
  static int[][] map,process;
  static int[] combArr;
  static LinkedList<Point> ableBlock=new LinkedList<>();
  static Queue<Point> que =new LinkedList<>();
  static class Point{
    int r;
    int c;
    public Point(int r,int c){
      this.r=r;
      this.c=c;
    }
  }
  static int[] dr={0,0,-1,1};
  static int[] dc={-1,1,0,0};
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    R=Integer.parseInt(st.nextToken());
    C=Integer.parseInt(st.nextToken());
    map=new int[R][C];
    process=new int[R][C];
    for(int r=0;r<R;r++){
      st=new StringTokenizer(br.readLine());
      for(int c=0;c<C;c++){
        map[r][c]=Integer.parseInt(st.nextToken());
        if(map[r][c]==0){
          ableBlock.add(new Point(r,c));
        }
      }
    }
    combArr=new int[3];
    answer=0;
    comb(0,0);
    
    System.out.println(answer);
    bw.flush();
    bw.close();
    br.close();
  }
  static void comb(int start,int ind){
    if(ind==3){
      for(int r=0;r<R;r++){
        for(int c=0;c<C;c++){
          process[r][c]=map[r][c];
        }
      }
      int cnt=0;
      for(int i=0;i<combArr.length;i++){
        Point p =ableBlock.get(combArr[i]);
        if(map[p.r][p.c]==0){
          process[p.r][p.c]=1;
          cnt+=1;
        }
      }
      if(cnt==3)solve();
      return;
    }
    for(int i=start;i<ableBlock.size();i++){
      combArr[ind]=i;
      comb(i+1, ind+1);
    }
  }
  static void solve(){
    for(int r=0;r<R;r++){
      for(int c=0;c<C;c++){
        if(process[r][c]==2){
          bfs(new Point(r,c));
        }
      }
    }
    int cnt=0;

    for(int r=0;r<R;r++){
      for(int c=0;c<C;c++){
        if(process[r][c]==0){
          cnt+=1;
        }
      }
    }
    answer=Math.max(answer,cnt);
  }

  static void bfs(Point start){

    que.add(start);
    while(!que.isEmpty()){
      Point now =que.poll();

      for(int i=0;i<4;i++){
        int tr = now.r+dr[i];
        int tc= now.c+dc[i];
        if(tr>=0 && tc>=0 && tr<R && tc<C){
          if(process[tr][tc]==0){
            process[tr][tc]=2;
            que.add(new Point(tr, tc));
          }
        }
      }
    }
  }
}