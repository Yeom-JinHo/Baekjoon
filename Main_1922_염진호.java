import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main_1922_염진호{

  static PriorityQueue<Edge> pq = new PriorityQueue<>();
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
  static int[] parents;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    parents=new int[N+1];
    for(int i=0;i<=N;i++){
      parents[i]=i;
    }
    st = new StringTokenizer(br.readLine());
    int M = Integer.parseInt(st.nextToken());
    for(int i=0;i<M;i++){
      st=new StringTokenizer(br.readLine());
      int a=Integer.parseInt(st.nextToken());
      int b=Integer.parseInt(st.nextToken());
      int w=Integer.parseInt(st.nextToken());
      pq.add(new Edge(a, b, w));
    }
    int answer=0;
    for(int i=0;i<M;i++){
      Edge now =pq.poll();
      if(!union(now.a,now.b)){
        answer+=now.w;
      }
    }
    System.out.println(answer);
    bw.flush();
    bw.close();
    br.close();
  }

  static int findParents(int a){
    if(parents[a]==a){
      return a;
    }
    parents[a]=findParents(parents[a]);
    return parents[a];
  }
  static boolean union(int a, int b){
    int aRoot = findParents(a);
    int bRoot = findParents(b);
    if(aRoot!=bRoot){
      parents[bRoot]=aRoot;
      return false;
    }
    return true;
  }
}