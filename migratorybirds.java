 /* You have been asked to help study the population of birds 
  *migrating across the continent. Each type of bird you are interested 
  *in will be identified by an integer value. Each time a particular kind of bird is spotted
  *its id number will be added to your array of sightings. You would like
  *to be able to find out which type of bird is most common given a list of sightings. 
  *Your task is to print the type number of that bird and if two or more types of birds are equally common,
  *choose the type with the smallest ID number.
  */
  
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class Solution {

    // Function to return most common spotted bird using a HashMap
    static int migratoryBirds(List<Integer> arr) {
        int valueCheck = 0;
        
        HashMap<Integer, Integer> birdMap =  new HashMap<Integer, Integer>();
        int listSize = arr.size();
        // Track bird numbers by storing bird occurence in a hashmap
        for (int i = 0; i< listSize; i++) {
            int key = arr.get(i);  
            // check for multiple sightings and increment associated value
            if (birdMap.containsKey(key)) {
                valueCheck = birdMap.get(key);
                valueCheck += 1;
                birdMap.put(key, valueCheck);
            } else {
                birdMap.put(key, 1);
            }
        }
        // return max value key
        int key = Collections.max(birdMap.entrySet(), Map.Entry.comparingByValue()).getKey();
        return key;

    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int arrCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        int result = migratoryBirds(arr);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}