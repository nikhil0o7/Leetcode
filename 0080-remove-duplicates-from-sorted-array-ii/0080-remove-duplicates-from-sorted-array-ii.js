/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    
    let ans = 0;
    
    for(let i = 0; i< nums.length; i++){
        if(nums[i] != nums[i+2]){
            nums[ans] = nums[i]
            ans++;
        }
    }
    
    return ans;
};