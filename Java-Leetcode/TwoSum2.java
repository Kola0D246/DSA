/* Given an array of integers nums and an integer target, return indices of the two nums such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. */

import java.util.HashMap;

class TwoSum2 {
    static int[] twoSum(int[] nums, int target){
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] result = {-1, -1};
        
        for (int i=0; i<nums.length; i++){
            int compliment = target - nums[i];

            if (map.containsKey(compliment)) {      // check if compliment exist
                result[0] = map.get(compliment);    // get compliement index
                result[1] = i;
            } else {
                map.put(nums[i], i);        // store number: index as key: value
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
