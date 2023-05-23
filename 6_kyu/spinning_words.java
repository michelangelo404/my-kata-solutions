//Stop gninnipS My sdroW!

import java.io.*;

public class SpinWords {

  public String spinWords(String sentence) {
    String out = null;
    String[] array = sentence.split(" ");
    
    for (int i = 0; i <= array.length - 1; i++) {
      if(array[i].length() >= 5) {
        array[i] = new StringBuffer(array[i]).reverse().toString();
      }
    }
      return String.join(" ", array);
  }
}

