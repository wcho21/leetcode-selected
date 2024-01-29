// Accepted: 239ms (40.53%), 44.23 (98.53%)

// brute force

function isPalindrome(s: string, beg: number, end: number): boolean {
    let left = beg;
    let right = end;

    while (left <= right) {
        if (s[left] !== s[right]) {
            return false;
        }
        left++;
        right--;
    }

    return true;
}

function longestPalindrome(s: string): string {
    const n = s.length;
    let longestBeg = 0;
    let longestEnd = 0;

    for (let beg = 0; beg < n; ++beg) {
        for (let end = 0; end < n; ++end) {
            if (end - beg <= longestEnd - longestBeg) {
                continue;
            }
            if (!isPalindrome(s, beg, end)) {
                continue;
            }

            longestBeg = beg;
            longestEnd = end;
        }
    }

    return s.slice(longestBeg, longestEnd+1);
};
