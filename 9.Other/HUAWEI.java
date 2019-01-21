public class HUAWEI {
    public void sort(int[] array, int len) {
        // 完成这个函数
        int start = 0;
        for(int i = 0; i< len;i++){
            if (i > start){
                if (array[i] == 0){
                    array[i] = array[start];
                    array[start] = 0;
                    start += 1;
                }
            }
        }
    }
}
