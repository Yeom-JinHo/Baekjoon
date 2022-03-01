import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main_11779_염진호{
  static int N,M;
  static ArrayList<ArrayList<Node>> eList;
  static StringBuilder sb;
  static class Node implements Comparable<Node>{
    int no;
    int w;
    ArrayList<Integer> path;
    public Node(int no,int w,ArrayList<Integer> path){
      super();
      this.no=no;
      this.w=w;
      this.path=path;
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
    StringTokenizer st;
    sb=new StringBuilder();
    N=Integer.parseInt(br.readLine());
    M=Integer.parseInt(br.readLine());
    eList=new ArrayList<>();
    for(int i=0;i<=N;i++){
      eList.add(new ArrayList<>());
    }
    for(int i=0;i<M;i++){
      st = new StringTokenizer(br.readLine());
      int from=Integer.parseInt(st.nextToken());
      int to=Integer.parseInt(st.nextToken());
      int w=Integer.parseInt(st.nextToken());
      eList.get(from).add(new Node(to,w,null));
    }
    st=new StringTokenizer(br.readLine());
    int start=Integer.parseInt(st.nextToken());
    int end =Integer.parseInt(st.nextToken());
    dijkstra(start,end);
    sb.setLength(sb.length()-1);
    bw.write(sb.toString()+"\n");
    bw.flush();
    bw.close();
    br.close();
  }
  static void dijkstra(int start,int end){
    int[] distance=new int[N+1];
    boolean[] chk=new boolean[N+1];
    PriorityQueue<Node> que= new PriorityQueue<>();

    Arrays.fill(distance, Integer.MAX_VALUE);
    distance[start]=0;
    que.offer(new Node(start,distance[start],new ArrayList<Integer>(Arrays.asList(start))));

    while(!que.isEmpty()){
      Node current = que.poll();

      if(chk[current.no])continue;
      if(current.no==end){
        System.out.println(distance[current.no]);
        System.out.println(current.path.size());
        for(int i=0;i<current.path.size();i++){
          sb.append(current.path.get(i)+" ");
        }
      }

      chk[current.no]=true;

      for(int i=0;i<eList.get(current.no).size();i++){
        Node next=eList.get(current.no).get(i);
        if(!chk[next.no] && distance[next.no]>distance[current.no]+next.w){
          distance[next.no]=distance[current.no]+next.w;
          ArrayList<Integer> nextPath=(ArrayList<Integer>) current.path.clone();
          nextPath.add(next.no);
          que.offer(new Node(next.no,distance[next.no],nextPath));
        }
      }
    }

  }
}