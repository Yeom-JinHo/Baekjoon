import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main_14938_염진호
{
  static int N,M,R;
  static int[] items;
  static ArrayList<ArrayList<Node>> eList;
  static class Node implements Comparable<Node>{
    int no;
    int w;
    public Node(int no,int w){
      super();
      this.no=no;
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
    N=Integer.parseInt(st.nextToken());
    M=Integer.parseInt(st.nextToken());
    R=Integer.parseInt(st.nextToken());
    items=new int[N+1];
    eList=new ArrayList<>();
    for(int i=0;i<=N; i++){
      eList.add(new ArrayList<>());
    }
    st=new StringTokenizer(br.readLine());
    for(int i=1;i<=N;i++){
      items[i]=Integer.parseInt(st.nextToken());
    }
    for(int i=0;i<R;i++){
      st=new StringTokenizer(br.readLine());
      int from =Integer.parseInt(st.nextToken());
      int to =Integer.parseInt(st.nextToken());
      int l =Integer.parseInt(st.nextToken());
      eList.get(from).add(new Node(to,l));
      eList.get(to).add(new Node(from,l));
    }
    int answer=0;
    for(int i=1;i<=N;i++){
      answer=Math.max(answer, dijkstra(i));
    }
    bw.write(answer+"\n");
    bw.flush();
    bw.close();
    br.close();
  }
  static int dijkstra(int start){
    boolean[] chk = new boolean[N+1];
    int[] distance=new int[N+1];
    Arrays.fill(distance, Integer.MAX_VALUE);
    PriorityQueue<Node> que= new PriorityQueue<>();
    distance[start]=0;
    que.offer(new Node(start,distance[start]));

    while(!que.isEmpty()){
      Node current = que.poll();

      if(chk[current.no])continue;
      chk[current.no]=true;
      
      for(int i=0;i<eList.get(current.no).size();i++){
        Node next =eList.get(current.no).get(i);
        if(!chk[next.no] && distance[next.no]>distance[current.no]+next.w){
          distance[next.no]=distance[current.no]+next.w;
          que.offer(new Node(next.no,distance[next.no]));
        }
      }
    }
    int cnt=0;
    for(int i=1;i<=N;i++){
      if(distance[i]<=M){
        cnt+=items[i];
      }
    }
    return cnt;
  }
}
