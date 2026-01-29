char * mergeAlternately(char * word1, char * word2){
    int l1 = strlen(word1);
    int l2 = strlen(word2);
    char *res = (char *)malloc(l1 + l2 + 1);
    if (!res) return NULL; // safety
    int c = 0;
    while (*word1 != '\0' || *word2 != '\0') {
        if(*word1 != '\0'){
            res[c] = *word1;
            word1++;
            c++;
        }
        if(*word2 != '\0'){
            res[c] = *word2;
            word2++;
            c++;
        } 
    }
    res[c] = '\0';
    return res;
}
