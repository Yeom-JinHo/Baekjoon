import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main_17135_염진호{
  static int R,C,D;
  static int[][] arr,tmp;
  static int answer;
  // 가장 왼쪽
  static int[] dr={0,-1,0};
  static int[] dc={-1,0,1};
  static int[] combArr=new int[3];
  static class Point{
    int r;
    int c;
    int l;
    public Point(int r,int c,int l){
      this.r=r;
      this.c=c;
      this.l=l;
    }
  }
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    R=Integer.parseInt(st.nextToken());
    C=Integer.parseInt(st.nextToken());
    D=Integer.parseInt(st.nextToken());

    arr=new int[R+1][C];
    tmp=new int[R+1][C];
    for(int r=0;r<R;r++){
      st=new StringTokenizer(br.readLine());
      for(int c=0;c<C;c++){
        arr[r][c]=Integer.parseInt(st.nextToken());
      }
    }

    answer=0;
    comb(0,0);
    System.out.println(answer);
    bw.flush();
    bw.close();
    br.close();
  }

  static void dieCount(){
    for(int r=0;r<R;r++){
      for(int c=0;c<C;c++){
        tmp[r][c]=arr[r][c];
      }
    }
    int count=0;

    for(int r=R;r>=0;r--){
      // 배열을 내리는게 아니라 궁수가 전진한다.
      for(int i=0;i<3;i++){
        boolean[][] chk =new boolean[R][C];
        Queue<Point> que =new LinkedList<>();
        que.add(new Point(r,combArr[i],0));

        while(!que.isEmpty()){
          Point now =que.poll();

          if(now.l>D)continue;
          if(now.l!=0 && tmp[now.r][now.c]>=1){
            tmp[now.r][now.c]+=1;
            break;
          }

          for(int d=0;d<3;d++){
            int tr=now.r+dr[d];
            int tc=now.c+dc[d];
            if(tr>=0 && tc>=0 && tr<R && tc<C){
              if(!chk[tr][tc] && tr!=r){
                chk[tr][tc]=true;
                que.add(new Point(tr,tc,now.l+1));
              }
            }
          }
        }
      }
      for(int rr=0;rr<R;rr++){
        for(int cc=0;cc<C;cc++){
          if(tmp[rr][cc]>=2){
            count+=1;
            tmp[rr][cc]=0;
          }
        }
      }
    }

    answer=Math.max(answer,count);
  }
  static void comb(int start,int ind){
    if(ind==3){
      dieCount();
      return;
    }
    for(int i=start;i<C;i++){
      combArr[ind]=i;
      comb(i+1,ind+1);
    }
  }
}