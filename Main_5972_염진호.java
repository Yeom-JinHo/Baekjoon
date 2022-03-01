import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main_5972_염진호{
  static int N,M;
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
    eList =new ArrayList<>();
    for(int i=0;i<=N;i++){
      eList.add(new ArrayList<>());
    }
    for(int i=0;i<M;i++){
      st=new StringTokenizer(br.readLine());
      int from=Integer.parseInt(st.nextToken());
      int to=Integer.parseInt(st.nextToken());
      int w=Integer.parseInt(st.nextToken());
      eList.get(from).add(new Node(to,w));
      eList.get(to).add(new Node(from,w));
    }
    dijkstra();
    bw.flush();
    bw.close();
    br.close();
  }
  static void dijkstra(){
    boolean[] chk = new boolean[N+1];
    int[] distance=new int[N+1];
    Arrays.fill(distance,Integer.MAX_VALUE);
    PriorityQueue<Node> que=new PriorityQueue<>();
    distance[1]=0;
    que.offer(new Node(1,distance[1]));

    while(!que.isEmpty()){
      Node current =que.poll();

      if(current.no==N)break;
      if(chk[current.no])continue;
      chk[current.no]=true;
      for(int i=0;i<eList.get(current.no).size();i++){
        Node next=eList.get(current.no).get(i);
        if(!chk[next.no] && distance[next.no]>distance[current.no]+next.w){
          distance[next.no]=distance[current.no]+next.w;
          que.offer(new Node(next.no,distance[next.no]));
        }
      }
    }
    System.out.println(distance[N]);
  }
}