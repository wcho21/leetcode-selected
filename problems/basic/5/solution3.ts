// Accepted: 87ms (65.00%), 45.32MB (86.00%)

// sliding window

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

function scanLongestPalindrome(s: string, beg: number, end: number): string {
    const n = s.length;
    let longestBeg = -1;
    let longestEnd = -1;

    // scan palindrome with window, from left to right
    while (end < n) {
        if (!isPalindrome(s, beg, end)) {
            beg++;
            end++;
            continue;
        }

        longestBeg = beg;
        longestEnd = end;

        // move window to right, if end of boundary
        if (beg === 0 || end === n-1) {
            beg++;
            end++;
            continue;
        }

        // expand window
        beg--;
        end++;
    }

    // not found
    if (longestBeg === -1 || longestEnd === -1) {
        return "";
    }

    return s.slice(longestBeg, longestEnd+1);
}

function longestPalindrome(s: string): string {
    const oddLength = scanLongestPalindrome(s, 0, 0);
    const evenLength = scanLongestPalindrome(s, 0, 1);

    return oddLength.length > evenLength.length ? oddLength : evenLength;
};
