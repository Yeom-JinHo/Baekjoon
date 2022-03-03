import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main_9694_염진호{
  static int N,M;
  static ArrayList<ArrayList<Node>> eList;
  // static boolean[] chk;
  // static int[] distance;
  static StringBuilder sb;
  static class Node implements Comparable<Node>{
    int no;
    int w;
    ArrayList<Integer> path;
    Node(int no,int w,ArrayList<Integer> path){
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
    StringTokenizer st = new StringTokenizer(br.readLine());
    sb=new StringBuilder();
    int T=Integer.parseInt(st.nextToken());
    for(int tc=1;tc<=T;tc++){
      st=new StringTokenizer(br.readLine());
      N=Integer.parseInt(st.nextToken());
      M=Integer.parseInt(st.nextToken());
      eList=new ArrayList<>();
      for(int i=0;i<M;i++){
        eList.add(new ArrayList<>());
      }
      for(int i=0;i<N;i++){
        st=new StringTokenizer(br.readLine());
        int from=Integer.parseInt(st.nextToken());
        int to=Integer.parseInt(st.nextToken());
        int w=Integer.parseInt(st.nextToken());
        eList.get(from).add(new Node(to,w,null));
        eList.get(to).add(new Node(from,w,null));
      }
      sb.append("Case #"+tc+":");
      dijkstra();
    }
    bw.write(sb.toString());
    bw.flush();
    bw.close();
    br.close();
  }
  static void dijkstra(){
    boolean[] chk= new boolean[M];
    int[] distance = new int[M];
    Arrays.fill(distance, Integer.MAX_VALUE);

    PriorityQueue<Node> que = new PriorityQueue<>();
    distance[0]=0;
    
    que.offer(new Node(0,distance[0],new ArrayList<>(Arrays.asList(0))));

    while(!que.isEmpty()){
      Node current =que.poll();
      if(chk[current.no])continue;
      if(current.no==M-1){
        while(!current.path.isEmpty()){
          sb.append(" "+current.path.get(0));
          current.path.remove(0);
        }
        sb.append("\n");
        return;
      };

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
    sb.append(-1+"\n");
  }
}