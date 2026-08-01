#include <string.h>

int strStr(char* haystack, char* needle) {
int i, j, l1, l2;

if (!haystack || !needle) return -1;

l2 = strlen(needle);
if (l2 == 0) return 0;

l1 = strlen(haystack);

for (i = 0; i <= l1 - l2; i++) {
for (j = 0; j < l2 && haystack[i + j] == needle[j]; j++) {
}
if (j == l2) return i;
}

return -1;
}