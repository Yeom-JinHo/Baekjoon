import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.StringTokenizer;

class Main{
  static int N,M,answer;
  static int[][] arr;
  static boolean first;
  // 상 우 하 좌 
  static int[]dr={-1,0,1,0};
  static int[] dc={0,1,0,-1};
  static LinkedList<int[]> cctvs=new LinkedList<>();
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    StringTokenizer st = new StringTokenizer(br.readLine());
    N= Integer.parseInt(st.nextToken());
    M= Integer.parseInt(st.nextToken());
    arr=new int[N][M];
    first=true;
    answer=Integer.MAX_VALUE;
    for(int r=0;r<N;r++){
      st=new StringTokenizer(br.readLine());
      for(int c=0;c<M;c++){
        arr[r][c]=Integer.parseInt(st.nextToken());
        if(arr[r][c]>0 && arr[r][c]<6){
          cctvs.add(new int[]{r,c});
        }
      }
    }
    dfs(0);
    calMin();
    bw.write(answer+"\n");
    bw.flush();
    bw.close();
    br.close();
  }

  static void dfs(int cnt){
    if(cnt>=cctvs.size()){
      calMin();
      return;
    }
    int[] cctv=cctvs.get(cnt);
    int r=cctv[0];
    int c=cctv[1];
    int[][] tmp=new int[N][M];
    deepCopy(tmp,arr);
    // CCTV 
    for(int d=0;d<4;d++){
      switch(arr[r][c]){
        case 1:
          watch(r, c,d);
          break;
        case 2: 
          watch(r, c, d);
          watch(r, c, (d+2)%4);
          break;
        case 3:
          watch(r, c, d);
          watch(r, c, (d+1)%4);
          break;
        case 4:
          watch(r, c, d);
          watch(r, c, (d+1)%4);
          watch(r, c, (d+2)%4);
          break;
        case 5:
          watch(r, c, d);
          watch(r, c, (d+1)%4);
          watch(r, c, (d+2)%4);
          watch(r, c, (d+3)%4);
          break;
      }
      dfs(cnt+1);
      deepCopy(arr,tmp);
    }
  }
  static void calMin(){
    int cnt=0;
    for(int r=0;r<N;r++){
      for(int c=0;c<M;c++){
        if(arr[r][c]==0){
          cnt+=1;
        }
      }
    }
    answer=Math.min(answer,cnt);
  }
  static void deepCopy(int[][]a,int[][]b){
    for(int r=0;r<N;r++){
      for(int c=0;c<M;c++){
        a[r][c]=b[r][c];
      }
    }
  }
  static void watch(int r,int c,int dir){
    int tr= r+dr[dir];
    int tc= c+dc[dir];
    while(true){
      if(tr<0 || tc<0 || tr>=N || tc>=M){
        break;
      }
      if(arr[tr][tc]==6){
        break;
      }
      if(arr[tr][tc]==0){
        arr[tr][tc]=-1;
      }
      tr=tr+dr[dir];
      tc=tc+dc[dir];
    }
  }
}