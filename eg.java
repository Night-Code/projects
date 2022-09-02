import java.util.*;
import java.io.*;
class eg
{
  public static void main(String args[]) throws FileNotFoundException
  {

    File obj=new File("abcd.txt");
    Scanner ob=new Scanner(obj);
    String d=ob.nextLine();
    System.out.println(d);
    throw new FileNotFoundException("exception");
  }

}
