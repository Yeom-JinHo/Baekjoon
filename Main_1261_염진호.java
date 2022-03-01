import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main_1261_염진호{
  static int R,C;
  static int[][] arr;
  static int[] dr={0,0,-1,1};
  static int[] dc={-1,1,0,0};
  static class Node implements Comparable<Node>{
    int r;
    int c;
    int w;
    public Node(int r,int c,int w){
      super();
      this.r=r;
      this.c=c;
      this.w=w;
    }
    @Override
    public int compareTo(Node o) {
      // TODO Auto-generated method stub
      return this.w-o.w;
    }
  }
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    C=Integer.parseInt(st.nextToken());
    R=Integer.parseInt(st.nextToken());
    arr=new int[R][C];
    for(int r=0;r<R;r++){
      String line=br.readLine();
      for(int c=0;c<C;c++){
        arr[r][c]=line.charAt(c)-'0';
      }
    }
    bw.write(dijkstra()+"\n");
    bw.flush();
    bw.close();
    br.close();
  }
  static int dijkstra(){
    boolean[][] chk = new boolean[R][C];
    PriorityQueue<Node> que= new PriorityQueue<>();
    que.offer(new Node(0,0,0));

    while(!que.isEmpty()){
      Node current=que.poll();

      if(chk[current.r][current.c]) continue;
      if(current.r==R-1 && current.c==C-1)
        return current.w;

      chk[current.r][current.c]=true;
      for(int i=0;i<4;i++){
        int tr=current.r+dr[i];
        int tc=current.c+dc[i];
        if(tr>=0 && tc>=0 && tr<R && tc<C){
          if(!chk[tr][tc]){
            que.offer(new Node(tr,tc,current.w+arr[tr][tc]));
          }
        }
      }
    }
    return -1;
  }
}