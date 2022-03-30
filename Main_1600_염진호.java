import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

class Main{
  static int K,R,C;
  static int[][] arr;
  static int[][][] visitCount;
  // 좌측 상단부터
  static int[] hdr={-1,-2,-2,-1,1,2,2,1};
  static int[] hdc={-2,-1,1,2,2,1,-1,-2};
  // 상 우 좌 하
  static int[] dr={-1,0,0,1};
  static int[] dc={0,1,-1,0};
  static Deque<Point> que=new LinkedList<>();
  static class Point{
    int r;
    int c;
    int k;
    public Point(int r,int c, int k){
      this.r=r;
      this.c=c;
      this.k=k;
    }
  }
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    K=Integer.parseInt(st.nextToken());
    st=new StringTokenizer(br.readLine());
    C=Integer.parseInt(st.nextToken());
    R=Integer.parseInt(st.nextToken());

    arr=new int[R][C];
    visitCount=new int[R][C][K+1];

    for(int r=0;r<R;r++){
      st=new StringTokenizer(br.readLine());
      for(int c=0;c<C;c++){
        arr[r][c]=Integer.parseInt(st.nextToken());
      }
    }
    // 여기서 부터 시작
    que.add(new Point(0,0,K));
    int answer=-1;
    while(!que.isEmpty()){
      Point now=que.pollFirst();
      if(now.r==R-1 && now.c==C-1){
        answer=visitCount[now.r][now.c][now.k];
        break;
      }
      // 아직 말이 가능하다면~ 
      if(now.k>=1){
        move(now,1);
        move(now,0);
      }else{
        move(now,0);
      }
    }
    if(answer==-1){
      System.out.println(-1);
    }else{
      System.out.println(answer);
    }
    bw.flush();
    bw.close();
    br.close();
  }
  // 현재 좌표를 주고 말과 원숭기를 구분하기 위해 플래그
  // flag 말이면 1 원숭이면 0
  static void move(Point now,int flag){
    if(flag==1){
      for(int i=0;i<hdr.length;i++){
        int tr=now.r+hdr[i];
        int tc=now.c+hdc[i];
        if(tr>=0 && tc>=0 && tr<R && tc<C){
          if(visitCount[tr][tc][now.k-flag]==0 && arr[tr][tc]==0){
            que.add(new Point(tr,tc,now.k-1));
            visitCount[tr][tc][now.k-1]=visitCount[now.r][now.c][now.k]+1;
          }
        }
      }
    }else{
      for(int i=0;i<dr.length;i++){
        int tr=now.r+dr[i];
        int tc=now.c+dc[i];
        if(tr>=0 && tc>=0 && tr<R && tc<C){
          if(visitCount[tr][tc][now.k]==0 && arr[tr][tc]==0){
            que.add(new Point(tr,tc,now.k));
            visitCount[tr][tc][now.k]=visitCount[now.r][now.c][now.k]+1;
          }
        }
      }
    }
  }
}