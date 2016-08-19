void moveZeroes(int* nums, int numsSize) {
    int i,numzero=0;
    for (i=0;i<numsSize;i++)
    {
        if (nums[i]!=0)
            nums[numzero++]=nums[i];
    }
    
    for (i=numzero;i<numsSize;i++)
        nums[i]=0;
}
