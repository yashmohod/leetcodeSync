/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) {
    *returnSize = candiesSize;

    int largest = candies[0];
    for (int i = 1; i < candiesSize; i++) {
        if (candies[i] > largest) largest = candies[i];
    }

    bool* res = (bool*)malloc(sizeof(bool) * candiesSize);
    for (int i = 0; i < candiesSize; i++) {
        res[i] = (candies[i] + extraCandies >= largest);
    }

    return res;
}
