public class test{
    public static int remove(int[] nums) {
        int i=0;
        for(int j=0;j<=nums.length-1;j++) {
            if (nums[i] != nums[j]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i+1;
    }
    public static void main(String[] args) {
        int[] nums={1,2,3,3,4,5,6,7,7};
        remove(nums);
    }
}