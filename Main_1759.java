import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_1759 {
  static int L,C;
  static String[] alpha,tmp;// 자음 모음
  static  StringBuilder sb;
  public static void main(String[] args) throws IOException{
    BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    sb = new StringBuilder();
    st=new StringTokenizer(br.readLine());
    L=Integer.parseInt(st.nextToken());
    C=Integer.parseInt(st.nextToken());
    st=new StringTokenizer(br.readLine());
    alpha=new String[C];
    tmp=new String[L];
    for(int i=0;i<C;i++){
      alpha[i]=st.nextToken();
    }
    Arrays.sort(alpha);
    comb(0,0,L,alpha);
    sb.setLength(sb.length()-1);
    System.out.println(sb);
    br.close();
  }
  public static void comb(int count,int start,int r,String[] q){
    if(count==r){
      int consCount=0;
      int vowsCount=0;
      for(int c=0;c<count;c++){
        String tmpString=tmp[c];
        sb.append(tmpString);
        if(tmpString.matches("[aeiou]")){
          consCount+=1;
        }else{
          vowsCount+=1;
        }
      }
      if(consCount<1 || vowsCount<2)
        sb.setLength(sb.length()-r);
      else
        sb.append("\n");
    }else{
      for(int i=start;i<q.length;i++){
        tmp[count]=q[i];
        comb(count+1,i+1,r,q);
      }
    }
  }
}