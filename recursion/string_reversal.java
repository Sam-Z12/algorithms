package recursion;

class Main {
    public static void main(String[] args) {
        printer("Hi");
        printer(reverseString("hello"));
        System.out.println(isPalindrome("kayak"));
        System.out.println(findBinary(233, ""));
        System.out.println(recursiveSummation(10));
        int[] Nums = {-1, 0, 1, 2, 3, 4, 7, 9 ,10, 20};
        System.out.println(binarySearch(Nums, 0, Nums.length-1, 10));
    }

    public static String reverseString(String input){
        if (input.equals("")) {
                    return "";
                }
                return reverseString(input.substring(1)) + input.charAt(0);
    }


    public static boolean isPalindrome(String input) {
        if (input.length()  == 0 || input.length() == 1) {
            return true;
        }
        if (input.charAt(0) == input.charAt(input.length()-1)){
            return isPalindrome(input.substring(1, input.length()-1));
        }

        return false;
    }

    public static void printer(String input){
        System.out.println(input);
    }

    public static String findBinary(int decimal, String result){
        if (decimal == 0)
            return result;

        result = decimal % 2 + result;
        return findBinary(decimal / 2, result);
    }

    public static int recursiveSummation(int inputNumber){
        if (inputNumber <= 1)
            return inputNumber;

        return inputNumber + recursiveSummation(inputNumber - 1);
    }

    public static int binarySearch(int[] A, int left, int right, int x){
        if (left > right) {
            return -1;
        }

        int mid = (left + right) / 2;

        if (x == A[mid]) {
            return mid;
        }

        if (x < A[mid]){
            return binarySearch(A, left, mid-1, x);
        }

        return binarySearch(A, mid+1, right, x);

    }


    public static long fib(long n){
        if ((n == 0) || (n == 1))
            return n;
        else 
            return fib(n-1) + fib(n-2);
    }



}