import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main_9205_염진호{
  static class Point{
    int r;
    int c;
    public Point(int r,int c){
      this.r=r;
      this.c=c;
    }
  }
  static boolean[] chk;
  static LinkedList<Point> pointList;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int T=Integer.parseInt(st.nextToken());
    for(int t=0;t<T;t++){
      st=new StringTokenizer(br.readLine());
      int N=Integer.parseInt(st.nextToken());
      chk=new boolean[N+2];
      pointList=new LinkedList<>();
      
      for(int n=0;n<N+2;n++){
        st=new StringTokenizer(br.readLine());
        int r =Integer.parseInt(st.nextToken());
        int c =Integer.parseInt(st.nextToken());
        pointList.add(new Point(r, c));
      }
      chk[0]=true;
      if(dfs(pointList.get(0))){
        System.out.println("happy");
      }else{
        System.out.println("sad");
      }
    }
    bw.flush();
    bw.close();
    br.close();
  }
  static boolean dfs(Point start){
    if(start.r==pointList.get(pointList.size()-1).r && start.c==pointList.get(pointList.size()-1).c){
      return true;
    }
    for(int i=1;i<pointList.size();i++){
      Point next=pointList.get(i);
      int d=Math.abs(start.r-next.r)+Math.abs(start.c-next.c);
      if(d<=1000 && !chk[i]){
        chk[i]=true;
        if(dfs(next)){
          return true;
        }
      }
    }
    return false;
  }
  static boolean bfs(Point start){
    Queue<Point> que =new LinkedList<>();
    boolean[] chk = new boolean[pointList.size()];
    chk[0]=true;
    que.add(new Point(start.r, start.c));
    while(!que.isEmpty()){
      Point now =que.poll();
      if(now.r==pointList.get(pointList.size()-1).r && now.c==pointList.get(pointList.size()-1).c){
        return true;
      }
      for(int i=1;i<pointList.size();i++){
        Point next=pointList.get(i);
        int d=Math.abs(now.r-next.r)+Math.abs(now.c-next.c);
        if(d<=1000 && !chk[i]){
          chk[i]=true;
          que.add(next);
        }
      }
    }
    return false;
  }
}