import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main_11430_염진호{
  static int N;
  static int[][] arr;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N=Integer.parseInt(st.nextToken());
    arr=new int[N][N];
    for(int i=0;i<N;i++){
      st=new StringTokenizer(br.readLine());
      for(int j=0;j<N;j++){
        arr[i][j]=Integer.parseInt(st.nextToken());
      }
    }
    for(int i=0;i<N;i++){
      dijkstra(i);
    }
    bw.flush();
    bw.close();
    br.close();
  }
  static void dijkstra(int start){
    boolean[] chk=new boolean[N];
    Queue<Integer> que =new LinkedList<>();
    que.add(start);

    while(!que.isEmpty()){
      int current=que.poll();
      for(int i=0;i<N;i++){
        if(!chk[i] && arr[current][i]==1){
          chk[i]=true;
          que.add(i);
        }
      }
    }
    for(int i=0;i<N;i++){
      System.out.printf("%d ",chk[i]?1:0);
    }
    System.out.println();
  }
}