import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main_1719_염진호{
  static int N,M;
  static ArrayList<ArrayList<Node>> eList;
  static StringBuilder sb;
  static class Node implements Comparable<Node>{
    int no;
    int w;
    int prev;
    public Node(int no,int w,int prev){
      super();
      this.no=no;
      this.w=w;
      this.prev=prev;
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
    sb=new StringBuilder();
    N=Integer.parseInt(st.nextToken());
    M=Integer.parseInt(st.nextToken());
    eList=new ArrayList<>();
    for(int i=0;i<=N;i++){
      eList.add(new ArrayList<>());
    }
    for(int i=0;i<M;i++){
      st=new StringTokenizer(br.readLine());
      int from=Integer.parseInt(st.nextToken());
      int to=Integer.parseInt(st.nextToken());
      int w=Integer.parseInt(st.nextToken());
      eList.get(from).add(new Node(to,w,from));
      eList.get(to).add(new Node(from,w,to));
    }
    for(int i=1;i<=N;i++){
      dijkstra(i);
    }
    bw.write(sb.toString());
    bw.flush();
    bw.close();
    br.close();
  }
  static void dijkstra(int start){
    boolean[] chk =new boolean[N+1];
    int[] distance=new int[N+1];
    int[] parent=new int[N+1];
    PriorityQueue<Node> que =new PriorityQueue<>();
    Arrays.fill(distance, Integer.MAX_VALUE);
    distance[start]=0;
    parent[start]=start;
    que.offer(new Node(start,distance[start],start));

    while(!que.isEmpty()){
      Node current=que.poll();

      if(chk[current.no])continue;
      chk[current.no]=true;
      parent[current.no]=current.prev;
      for(int i=0;i<eList.get(current.no).size();i++){
        Node next=eList.get(current.no).get(i);
        if(!chk[next.no] && distance[next.no]>distance[current.no]+next.w){
          distance[next.no]=distance[current.no]+next.w;
          que.offer(new Node(next.no,distance[next.no],current.no));
        }
      }
    }
    for(int i=1;i<=N;i++){
      if(i==start){
        sb.append("-");
      }else{
        sb.append(findParent(i, start, parent));
      }
      sb.append(" ");
    }
    sb.setLength(sb.length()-1);
    sb.append("\n");
  }
  static int findParent(int now,int root,int[] parent){
    if(parent[now]==root){
      return now;
    }
    return findParent(parent[now], root, parent);
  }
}