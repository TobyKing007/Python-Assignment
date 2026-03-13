public class MeasuresOfDispersion   {

    public static double calculateMean(int[] numbers) {

    double sum = 0;

    for (int num : numbers) {
        sum += num;
    }

    return sum / numbers.length;
        
        }



    public static double calculateVariance(int[] numbers, double mean) {

    double sumOfSquareDifference = 0;

    for (int num : numbers) {
       double difference = num - mean;
       double squareOfDifference = difference * difference;
       sumOfSquareDifference += squareOfDifference;
    }

    return sumOfSquareDifference / numbers.length;
}

    
    public static double calculateStandardDeviation (double variance)       {

    return Math.sqrt(variance);


    }








        }








        
