import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main_16236_염진호{
  static int N;
  static int[][] arr;
  static boolean[][] chk;
  static int[] dr={-1,0,0,1};  // 상 좌 우 하
  static int[] dc={0,-1,1,0};
  static int babySize;
  static int eatFish;
  static int answer;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N=Integer.parseInt(st.nextToken());
    arr=new int[N][N];
    chk=new boolean[N][N];
    babySize=2;

    for(int r=0;r<N;r++){
      st=new StringTokenizer(br.readLine());
      for(int c=0;c<N;c++){
        arr[r][c]=Integer.parseInt(st.nextToken());
      }
    }
    eatFish=0;
    answer=0;
    int prev=eatFish;
    int next=eatFish;
    boolean dfsChk=false;
    do {
      prev=eatFish;
      dfsChk=false;
      for(int r=0;r<N;r++){
        for(int c=0;c<N;c++){
          if(arr[r][c]==9 && !dfsChk){
            chk=new boolean[N][N];
            chk[r][c]=true;
            bfs(r,c);
            dfsChk=true;
          }
        }
      }
      next=eatFish;
      if(eatFish==babySize){
        babySize+=1;
        eatFish=0;
      }
    } while (prev!=next);
    bw.write(answer+"\n");
    bw.flush();
    bw.close();
    br.close();
  }
  static void bfs(int sr,int sc){
    Queue <int[]> que=new LinkedList<>();
    que.add(new int[]{sr,sc,0});
    int prevDep=0;

    LinkedList <int[]> yamyamList=new LinkedList<>();

    while(!que.isEmpty()){
      int[] now=que.poll();
      int r=now[0];
      int c=now[1];
      int dep=now[2];

      if(prevDep!=dep){
        if(!yamyamList.isEmpty()){
          Collections.sort(yamyamList,new Comparator<int[]>() {
            public int compare(int[] a,int[] b){
              return a[0]==b[0]?a[1]-b[1]:a[0]-b[0];
            }
          });
          int[] yam=yamyamList.poll();
          arr[sr][sc]=0;
          arr[yam[0]][yam[1]]=9;
          eatFish+=1;
          answer+=yam[2];
          return;
        }else{
          prevDep=dep;
        }
      }

      for(int i=0;i<4;i++){
        int tr=r+dr[i];
        int tc=c+dc[i];
        if(tr>=0 && tc>=0 && tr<N && tc<N ){
          // 자기보다 큰 물고기는 지나갈 수 없다.
          if(!chk[tr][tc] && arr[tr][tc]<=babySize){
            // 얌얌 리스트 저장
            if(arr[tr][tc]<babySize && arr[tr][tc]!=0){
              yamyamList.add(new int[]{tr,tc,dep+1});
            }
            que.add(new int[]{tr,tc,dep+1});
            chk[tr][tc]=true;
          }
        }
      }
    }     
  }
}