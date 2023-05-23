//Delete occurrences of an element if it occurs more than n times

import org.apache.commons.lang3.*;
import java.util.Arrays;

public class EnoughIsEnough {

	public static int[] deleteNth(int[] elements, int maxOccurrences) {
    int occ = 0;
		for(int el:elements) {
      occ = 0;
      for(int i = 0; i < elements.length; i++) {
        if(el == elements[i]) {
          occ++;
          if(occ > maxOccurrences)
            elements = ArrayUtils.remove(elements, i);

        }
      }

    }
    System.out.println(Arrays.toString(elements));
		return elements;
	}

}

