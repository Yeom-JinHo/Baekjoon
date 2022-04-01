import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main_1194_염진호{
  static char[][] map;
  static int R,C;
  static boolean[][][] chk;
  // 상 우 하 좌
  static int[] dr ={-1,0,1,0};
  static int[] dc ={0,1,0,-1};
  static class Point{
    int r;
    int c;
    int depth;
    int key;
    public Point(int r,int c,int depth,int key){
      this.r=r;
      this.c=c;
      this.depth=depth;
      this.key=key;
    }
  }
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    // Input 민식이의 위치만 따로 뺀다. bfs시작점을 관리해야해서
    StringTokenizer st = new StringTokenizer(br.readLine());
    R=Integer.parseInt(st.nextToken());
    C=Integer.parseInt(st.nextToken());
    map=new char[R][C];
    chk=new boolean[R][C][1<<6+1];
    Point startP=null;

    for(int r=0;r<R;r++){
      String inp=br.readLine();
      for(int c=0;c<C;c++){
        map[r][c]=inp.charAt(c);
        if(map[r][c]=='0'){
          startP=new Point(r,c,0,0);
        }
      }
    }


    int answer=bfs(startP);
    System.out.println(answer);
    bw.flush();
    bw.close();
    br.close();
  }

  // 아스키 코드로 a~f 97~102
  // A~F 65~70
  static int bfs(Point startP){
    Queue<Point> que = new LinkedList<>();
    que.add(startP);
    chk[startP.r][startP.c][0]=true;

    while(!que.isEmpty()){
      Point now = que.poll();
      if(map[now.r][now.c]=='1'){
        return now.depth;
      }
      for(int i=0;i<4;i++){
        int tr=now.r+dr[i];
        int tc=now.c+dc[i];
        if(tr>=0 && tc>=0 && tr<R && tc<C){
          if(!chk[tr][tc][now.key]){
            // 탈출 이라면~
            // 해당 위치가 열쇠라면
            if(map[tr][tc]>='a' && map[tr][tc]<='f'){
              int ind=(int)map[tr][tc]-97+1;
              int temp=now.key|1<<ind;
              que.add(new Point(tr,tc,now.depth+1,temp));
              chk[tr][tc][temp]=true;
            }
            // 해당 위치가 자물쇠로 잠겨있다면
            else if((map[tr][tc]>='A' && map[tr][tc]<='F')){
              int ind=(int)map[tr][tc]-65+1;
              // 해당 키가 있다면 
              if((now.key&(1<<ind))!=0){
                que.add(new Point(tr,tc,now.depth+1,now.key));
                chk[tr][tc][now.key]=true;
              }
            }
            // 지나갈 수 있는 평지라면hh
            else if(map[tr][tc]=='.'|| map[tr][tc]=='0'|| map[tr][tc]=='1'){
              que.add(new Point(tr,tc,now.depth+1,now.key));
              chk[tr][tc][now.key]=true;
            }
          }
        }
      }
    }
    return -1;
  }
}