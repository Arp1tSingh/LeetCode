int compare(const void* a, const void* b) {
    int diff = (*(int**)a)[0] - (*(int**)b)[0];
    return diff != 0 ? diff : (*(int**)a)[1] - (*(int**)b)[1];
}

int** merge(int** intervals, int intervalsSize, int* intervalsColSize,
            int* returnSize, int** returnColumnSizes) {

    qsort(intervals, intervalsSize, sizeof(int*), compare);

    
    int** result = (int**)malloc(intervalsSize * sizeof(int*));
    *returnColumnSizes = (int*)malloc(intervalsSize * sizeof(int));
    *returnSize = 0;

    int* last = NULL;

    for (int i = 0; i < intervalsSize; i++) {
        int start = intervals[i][0];
        int end   = intervals[i][1];

        if (last == NULL || last[1] < start) {
            
            result[*returnSize] = intervals[i];
            (*returnColumnSizes)[*returnSize] = 2;
            last = result[(*returnSize)++];
        } else {
            
            if (end > last[1])
                last[1] = end;
        }
    }

    return result;
}