public class Main {

    public static void main(String[] args) {
        Solution A = new Solution();
        int[] a = {1,7,0,5,2,3,6,4};
        A.sort(a,a.length);
        for(int i : a){
            System.out.println(i);
        }
    }

    public static void SwapWithZero(int[] array, int len, int n){
        int nIdx = 0;
        int zeroIdx = 0;
        for(int i = 0; i <len;i++){
            if (array[i] == n) nIdx = i;
            if (array[i] == 0) zeroIdx = i;
        }
        array[zeroIdx] = n;
        array[nIdx] = 0;
    }
}
