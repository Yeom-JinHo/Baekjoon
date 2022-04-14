import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Main_14950_염진호{
  static int N,M,T;
  static int[] parents;
  static class Edge implements Comparable<Edge>{
    int a;
    int b;
    int c;
    public Edge(int a,int b,int c){
      this.a=a;
      this.b=b;
      this.c=c;
    }
    public int compareTo(Edge o) {
      return this.c-o.c;
    }
  }
  static PriorityQueue<Edge> eQue= new PriorityQueue<>();
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N=Integer.parseInt(st.nextToken());
    M=Integer.parseInt(st.nextToken());
    T=Integer.parseInt(st.nextToken());

    parents=new int[N+1];
    for(int n=0;n<=N;n++){
      parents[n]=n;
    }
    for(int m=0;m<M;m++){
      st=new StringTokenizer(br.readLine());
      int a=Integer.parseInt(st.nextToken());
      int b=Integer.parseInt(st.nextToken());
      int c=Integer.parseInt(st.nextToken());
      eQue.add(new Edge(a, b, c));
    }
    int answer=0;
    int road=0;
    while(!eQue.isEmpty()){
      Edge now =eQue.poll();
      if(!union(now.a,now.b)){
        answer+=now.c+road*T;
        road++;
      }
    }
    System.out.println(answer);
    bw.flush();
    bw.close();
    br.close();
  }
  static boolean union(int a, int b){
    int aRoot=findParent(a);
    int bRoot=findParent(b);

    if(aRoot!=bRoot){
      parents[aRoot]=parents[bRoot];
      return false;
    }else{
      return true;
    }
  }
  static int findParent(int a){
    if(parents[a]==a){
      return a;
    }
    parents[a]=findParent(parents[a]);
    return parents[a];
  }
}