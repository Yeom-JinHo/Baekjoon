import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

class Main_10973{
  static int[] arr;
  static int N;
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N=Integer.parseInt(st.nextToken());
    arr=new int[N];
    st=new StringTokenizer(br.readLine());
    for(int i=0;i<N;i++){
      arr[i]=Integer.parseInt(st.nextToken());
    }
    if(prevPer()){
      for(int a :arr){
        bw.write(a+" ");
      }
    }else{
      bw.write(String.valueOf(-1));
    }
    bw.write("\n");
    bw.flush();
    bw.close();
    br.close();
  }
  static boolean prevPer(){
    int i=N-1;
    while(i>0 && arr[i-1]<=arr[i]){
      i--;
    }
    if(i==0)
      return false;
    
    int j=N-1;
    while(arr[i-1]<=arr[j]){
      j--;
    }
    swap(i-1,j);
    int k=N-1;
    while(i<k){
      swap(i++,k--);
    }
    return true;
  }
  static void swap(int a, int b){
    int tmp=arr[a];
    arr[a]=arr[b];
    arr[b]=tmp;
  }
}