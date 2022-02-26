import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main_4485_염진호{
  static int N;
  static int[][] weight;
  static int[] dr={-1,1,0,0};
  static int[] dc={0,0,-1,1};
  static StringBuilder sb;
  static class Node implements Comparable<Node>{
    int r;
    int c;
    int total;
    public Node(int r,int c,int total){
      super();
      this.r=r;
      this.c=c;
      this.total=total;
    }
    @Override
    public int compareTo(Node o) {
      return this.total-o.total;
    }
  }
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st;
    sb=new StringBuilder();
    int cnt=1;
    while(true){
      st = new StringTokenizer(br.readLine());
      N=Integer.parseInt(st.nextToken());
      if(N==0)break;

      weight=new int[N][N];
      
      for(int r=0;r<N;r++){
        st=new StringTokenizer(br.readLine());
        for(int c=0;c<N;c++){
          weight[r][c]=Integer.parseInt(st.nextToken());
        }
      }
      sb.append("Problem ").append(cnt).append(": ").append(dijkstra(0, 0)).append("\n");
      cnt++;
    }
    bw.write(sb.toString());
    bw.flush();
    bw.close();
    br.close();
  }

  static int dijkstra(int sr,int sc){
    boolean[][] chk=new boolean[N][N];
    PriorityQueue<Node> que= new PriorityQueue<>();
    que.offer(new Node(sr,sc,weight[sr][sc]));
    while(!que.isEmpty()){
      Node now = que.poll();
      if(now.r==N-1 && now.c==N-1){
        return now.total;
      }
      chk[now.r][now.c]=true;
      for(int i=0;i<4;i++){
        int tr=now.r+dr[i];
        int tc=now.c+dc[i];
        if(tr>=0 && tc>=0 && tr<N && tc<N){
          if(!chk[tr][tc]){
            que.offer(new Node(tr,tc,now.total+weight[tr][tc]));
          }
        }
      }
    }
    
    return -1;
  }
}