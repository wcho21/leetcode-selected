// Accepted: 115ms (35.87%), 57.48MB (10.88%)

function lengthOfLongestSubstring(s: string): number {
    let left = 0;
    let right = 0;
    const lastOccur = new Map<number, number>();
    let longest = 0;

    while (right < s.length) {
        const ch = s[right];

        if (lastOccur[ch] === undefined || lastOccur[ch] < left) { // no repeating character contained
            longest = Math.max(longest, right-left+1);
        } else {
            left = lastOccur[ch]+1;
        }

        lastOccur[ch] = right;
        ++right;
    }

    return longest;
};
