import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
 
class Main_14891_염진호{
  static int[][] wheels=new int[4][8];
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = null;
    for(int i=0;i<4;i++){
      String line =br.readLine();
      for(int j=0;j<8;j++){
        wheels[i][j]=line.charAt(j)-'0';
      }
    }
    st=new StringTokenizer(br.readLine());
    int K =Integer.parseInt(st.nextToken());
    for(int k=0;k<K;k++){
      for(int i=0;i<4;i++){
      }
      st=new StringTokenizer(br.readLine());
      int n=Integer.parseInt(st.nextToken());
      int d=Integer.parseInt(st.nextToken());
      chkTurn(n-1, d, true, true);
    }
    int answer=0;
    for(int i=0;i<4;i++){
      if(wheels[i][0]==1){
        answer+=Math.pow(2, i);
      }
    }
    System.out.println(answer);
    bw.flush();
    bw.close();
    br.close();
  }
  //   현재 톱니휠 번호를 받고 방향을 지정한후
  // 바퀴를 회전하기 전 양 옆 바퀴를 확인한뒤 
  // 계산을 줄이기 위해 왼쪽이나 오른쪽 옆을 검사할 필요를 있는지 저장한다
  static void chkTurn(int cur,int dir,boolean chkL,boolean chkR){
    int prev = cur - 1;
    int next = cur + 1;
 
    if (chkL&&prev >= 0) {// 왼쪽을 검사할 필요가 있고 왼쪽의 바퀴가 존재할 경우
      int l = wheels[prev][2];//왼쪽에 있는 3시 방향의 상태
      int r = wheels[cur][6]; //오른쪽에 있는 9시 방향 상태
      if (l != r) {
        chkTurn(prev, -dir, true, false);  // 두 값이 다르다면 왼쪽 바퀴는 반대 방향으로 회전 전 검사
      }
    }
    if (chkR&&next <= 3) { // 오른쪽을 검사할 필요가 있고 오른쪽 바퀴가 존재할 경우
      int l = wheels[cur][2]; // 왼쪽에 있는 3시 방향의 상태
      int r = wheels[next][6];// 오른쪽에 있는 9시 방향 상태
      if (l != r) {
        chkTurn(next, -dir, false, true);// 두값이 다르다면 오른쪽 바퀴는 반대 방향으로 회전 전에 검사
      }
    }
 
    turn(cur, dir); // 현재 바퀴휠을 dir방향으로 돌린다.
  }
 
  static void turn(int n,int d){
    int[] tmp=new int[8];
    for (int k = 0; k < 8; k++) {
      tmp[k] = wheels[n][k]; // 임시배열에 돌리기 전의 톱니 상태를 저장한다.
    }
    if (d == 1) {   //시계 방향이라면
      for (int k = 0; k < 8; k++) {
        wheels[n][k] = tmp[(k + 7) % 8]; //총 8개이니 7을 더해주고 8을 나눈다.
      }
    }
    else{
      for (int k = 0; k < 8; k++) { // 반시계 방향이라면
        wheels[n][k] = tmp[(k + 1) % 8]; // 총 8개이니 1을 더해주고 8을 나눈다.
      }
    }
  }
}