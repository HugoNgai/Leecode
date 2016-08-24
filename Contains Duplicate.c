bool containsDuplicate(int* nums, int numsSize) {
    /*   O(n^2)  */
    
    int i,j;
    
    for (i=0;i<numsSize;i++)
        for (j=i+1;j<numsSize;j++)
            {
                if (nums[i]==nums[j])
                    return true;
            }
            
    return false;
    
    
}
