import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main_1197_염진호{
  static class Edge implements Comparable<Edge>{
    int a;
    int b;
    int w;
    public Edge(int a,int b,int w){
      this.a=a;
      this.b=b;
      this.w=w;
    }
    @Override
    public int compareTo(Edge o) {
      // TODO Auto-generated method stub
      return this.w-o.w;
    }
  }
  static PriorityQueue<Edge> que= new PriorityQueue<>();
  static int V,E;
  static int[] parent;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    V=Integer.parseInt(st.nextToken());
    E=Integer.parseInt(st.nextToken());
    parent=new int[V+1];
    for(int i=0;i<=V;i++){
      parent[i]=i;
    }
    for(int i=0;i<E;i++){
      st=new StringTokenizer(br.readLine());
      int a=Integer.parseInt(st.nextToken());
      int b=Integer.parseInt(st.nextToken());
      int w=Integer.parseInt(st.nextToken());
      que.add(new Edge(a, b, w));
    }
    int answer=0;
    for(int i=0;i<E;i++){
      Edge now =que.poll();
      if(!union(now.a,now.b)){
        answer+=now.w;
      }
    }
    System.out.println(answer);
    bw.flush();
    bw.close();
    br.close();
  }
  static boolean union(int a,int b){
    int aRoot =findParent(a);
    int bRoot =findParent(b);
    if(aRoot==bRoot){
      return true;
    }else{
      parent[bRoot]=aRoot;
      return false;
    }
  }
  static int findParent(int a){
    if(parent[a]==a){
      return a;
    }
    parent[a]=findParent(parent[a]);
    return parent[a];
  }
}