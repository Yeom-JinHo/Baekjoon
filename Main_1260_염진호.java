import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main_1260_염진호{
  static int N,M,V;
  static StringBuilder sb= new StringBuilder();
  static int[][] arr;
  static boolean[] chked;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N=Integer.parseInt(st.nextToken());
    M=Integer.parseInt(st.nextToken());
    V=Integer.parseInt(st.nextToken());
    arr=new int[N+1][N+1];
    chked=new boolean[N+1];
    for(int i=0;i<M;i++){
      st=new StringTokenizer(br.readLine());
      int to =Integer.parseInt(st.nextToken());
      int from=Integer.parseInt(st.nextToken());
      arr[to][from]=1;
      arr[from][to]=1;
    }
    dfs(V);
    sb.setLength(sb.length()-1);
    sb.append("\n");
    chked=new boolean[N+1];
    bfs(V);
    sb.setLength(sb.length()-1);
    sb.append("\n");
    bw.write(sb.toString());
    bw.flush();
    bw.close();
    br.close();
  }
  static void dfs(int now){
    chked[now]=true;
    sb.append(now+" ");
    for(int i=1;i<=N;i++){
      if(!chked[i] && arr[now][i]==1){
        dfs(i);
      }
    }
  }
  static void bfs(int start){
    Queue<Integer> que= new LinkedList<Integer>();
    que.add(start);
    chked[start]=true;
    while(!que.isEmpty()){
      int nowN=que.poll();
      sb.append(nowN+" ");
      for(int i=1;i<=N;i++){
        if(!chked[i] && arr[nowN][i]==1){
          chked[i]=true;
          que.add(i);
        }
      }
    }
  }
}