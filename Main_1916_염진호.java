import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main_1916_염진호{
  static int N,M,S,E;
  static ArrayList<ArrayList<Node>> wList;
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
      return this.w-o.w;
    }
  }
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N=Integer.parseInt(st.nextToken());
    M=Integer.parseInt(br.readLine());
    wList=new ArrayList<ArrayList<Node>>();
    for(int i=0;i<=N;i++){
      wList.add(new ArrayList<Node>());
    }
    for(int i=0;i<M;i++){
      st=new StringTokenizer(br.readLine());
      int from=Integer.parseInt(st.nextToken());
      int to=Integer.parseInt(st.nextToken());
      int w=Integer.parseInt(st.nextToken());
      wList.get(from).add(new Node(to,w));
    }
    st=new StringTokenizer(br.readLine());
    S=Integer.parseInt(st.nextToken());
    E=Integer.parseInt(st.nextToken());
    dijstra();
    bw.flush();
    bw.close();
    br.close();
  }
  static void dijstra(){
    int[] distance=new int[N+1];
    boolean[] chk =new boolean[N+1];
    PriorityQueue<Node> que=new PriorityQueue<>();
    Arrays.fill(distance, Integer.MAX_VALUE);
    distance[S]=0;
    que.offer(new Node(S,distance[S]));

    while(!que.isEmpty()){
      Node current= que.poll();
      if(chk[current.no])continue;
      chk[current.no]=true;

      for(int i=0;i<wList.get(current.no).size();i++){
        Node next=wList.get(current.no).get(i);
        if(!chk[next.no]){
          distance[next.no] =Math.min(distance[next.no] ,distance[current.no]+ next.w);
          que.offer(new Node(next.no,distance[next.no]));
        };
      }
    }
    System.out.println(distance[E]);
  }
}