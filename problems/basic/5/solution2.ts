// Accepted: 385ms (26.82%), 87.96MB (8.92%)

// dynamic programing

function longestPalindrome(s: string): string {
    const n = s.length;

    // DP table: [i][j]: i to j is palindrome
    const palindrome = Array(n).fill(null);
    for (let i = 0; i < n; ++i) {
        palindrome[i] = Array(n).fill(false);
    }

    let longestBeg = 0;
    let longestEnd = 0;

    // base case 1: length of 1
    for (let i = 0; i < n; ++i) {
        palindrome[i][i] = true;
    }

    // base case 2: length of 2
    for (let i = 0; i < n-1; ++i) {
        if (s[i] === s[i+1]) {
            palindrome[i][i+1] = true;
            longestBeg = i;
            longestEnd = i+1;
        }
    }

    // tabulation: length of n, from length of n-1
    for (let diff = 2; diff < n; ++diff) {
        for (let beg = 0; beg < n; ++beg) {
            const end = beg + diff;
            if (end >= n) {
                continue;
            }

            if (!palindrome[beg+1][end-1]) {
                continue;
            }
            if (s[beg] !== s[end]) {
                continue;
            }

            palindrome[beg][end] = true;
            longestBeg = beg
            longestEnd = end
        }
    }

    return s.slice(longestBeg, longestEnd+1);
};
