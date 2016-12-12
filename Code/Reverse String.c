char* reverseString(char* s) {
    int i,len,j;
    char temp;
    len=strlen(s);
    j=len/2;
    for (i=0;i<j;i++)
    {
        temp=s[i];
        s[i]=s[len-i-1];
        s[len-i-1]=temp;
    }
    return s;
}
