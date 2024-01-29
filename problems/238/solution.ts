// Accepted: 86ms (74.98%), 54.54MB (64.94%)
function productExceptSelf(nums: number[]): number[] {
    const prefixProds = Array(nums.length).fill(nums[0]);
    for (let i = 1; i < nums.length; ++i) {
        prefixProds[i] = prefixProds[i-1] * nums[i];
    }
    
    const suffixProds = Array(nums.length).fill(nums[nums.length-1]);
    for (let i = nums.length-2; i >= 0; --i) {
        suffixProds[i] = suffixProds[i+1] * nums[i];
    }

    const prods: number[] = Array(nums.length).fill(null)
        .map((_, i) => {
            const prefix = (i > 0) ? prefixProds[i-1] : 1;
            const suffix = (i < nums.length-1) ? suffixProds[i+1] : 1;
            return prefix * suffix;
        });

    return prods;
};
