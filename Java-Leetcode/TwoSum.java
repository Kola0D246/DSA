/* Given an array of integers nums and an integer target, return indices of the two nums such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. */

class TwoSum {
    static int[] twoSum(int[] nums, int target){
        int[] result = {-1, -1};
        for (int i=0; i<nums.length-1; i++){
            for (int j=i+1; j<nums.length; j++){
                if (nums[i]+nums[j] == target){
                    result[0] = i;
                    result[1] = j;
                }
            }
        }
        return result;
    }

    // Driver method
    public static void main(String[] args){
        int target = 10;
        int[] nums = {1,2,3,4,5};
        int[] result = twoSum(nums, target);

        if (result[0] == -1) {
            System.out.printf("No two numbers are found in array such that their sum is equal to %d", target);
        } else {
            System.out.printf("desired indices => [%d, %d]", result[0], result[1]);
    }
        }
}
