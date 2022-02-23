import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_2527_염진호{
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st;
    for(int i=0; i<4;i++){
      st= new StringTokenizer(br.readLine());
      int min_X_1=Integer.parseInt(st.nextToken());
      int min_Y_1=Integer.parseInt(st.nextToken());
      int max_X_1=Integer.parseInt(st.nextToken());
      int max_Y_1=Integer.parseInt(st.nextToken());

      int min_X_2=Integer.parseInt(st.nextToken());
      int min_Y_2=Integer.parseInt(st.nextToken());
      int max_X_2=Integer.parseInt(st.nextToken());
      int max_Y_2=Integer.parseInt(st.nextToken());

      // 9구역으로 나눠보자
      // 1 |2| 3
      // 4 |X| 5
      // 6 |7| 8
      
      // 1 4 6 처리
      if(min_X_1>=max_X_2){

        // 선분 or 점
        if(min_X_1==max_X_2){
          // 1 처리
          if(max_Y_1<=min_Y_2){
            if(max_Y_1==min_Y_2){
              bw.write("c"+"\n");
              continue;
            }
            bw.write("d"+"\n");
            continue;
          }
          // 6 처리
          if(min_Y_1>=max_Y_2){
            if(min_Y_1==max_Y_2){
              bw.write("c"+"\n");
              continue;
            }
            bw.write("d"+"\n");
            continue;
          }
          // 자동으로 4처리 가능
          bw.write("b"+"\n");
          continue;
        }
        bw.write("d"+"\n");
        continue;
      }
      // 9구역으로 나눠보자
      // 1 |2| 3
      // 4 |X| 5
      // 6 |7| 8

      // 3 5 8 처리
      if(max_X_1<=min_X_2){

        if(max_X_1==min_X_2){
          //3 처리
          if(max_Y_1<=min_Y_2){
            if(max_Y_1==min_Y_2){
              bw.write("c"+"\n");
              continue;
            }
            bw.write("d"+"\n");
            continue;
          }
          //8 처리
          if(min_Y_1>=max_Y_2){
            if(min_Y_1==max_Y_2){
              bw.write("c"+"\n");
              continue;
            }
            bw.write("d"+"\n");
            continue;
          }
          // 자동으로 5처리
          bw.write("b"+"\n");
          continue;
        }
        bw.write("d"+"\n");
        continue;
      }
      // 9구역으로 나눠보자
      // 1 |2| 3
      // 4 |X| 5
      // 6 |7| 8

      // 2 처리
      if (max_Y_1<=min_Y_2){        
        if(max_Y_1==min_Y_2){
          bw.write("b"+"\n");
          continue;
        }
        bw.write("d"+"\n");
        continue;
      }

      // 7 처리
      if (min_Y_1>=max_Y_2){
        if(min_Y_1==max_Y_2){
          bw.write("b"+"\n");
          continue;
        }
        bw.write("d"+"\n");
        continue;
      }

      bw.write("a"+"\n");
      continue;
    }
    bw.flush();
    bw.close();
    br.close();
  }
}