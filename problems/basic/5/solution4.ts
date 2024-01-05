// Accepted: 68ms (93.15%), 45.42MB (83.49%)

// Manacher's algorithm

function longestPalindrome(s: string): string {
    // to check even-number size palindromes, insert dummy characters
    const str = "#" + Array.from(s).join("#") + "#";

    const n = str.length;
    const radii = Array(n).fill(0);
    let center = 0; // center of recent large palindrome
    let rbound = 0; // the greatest index that recent large palindrome have accessed

    for (let i = 0; i < n; ++i) {
        // use the precalculated radius at index mirrored with respect to center
        if (0 < i && i < rbound) {
            // get index mirrored with respect to center
            const mirrored = 2 * center - i;
            // we haven't checked characters beyond rbound
            // so ensure that the radius does not take the index i beyond rbound
            radii[i] = Math.min(radii[mirrored], rbound-i);
        }

        // get the longest palindrome, centered at i
        let left = i - radii[i];
        let right = i + radii[i];
        while (left > 0 && right < n-1 && str[left-1] === str[right+1]) {
            left--;
            right++;
            radii[i]++;
        }

        // update to make next indices use the previous calculation
        if (right > rbound) {
            rbound = right;
            center = i;
        }
    }

    let maxRadius = -1;
    let maxIndex = -1;
    for (let i = 0; i < radii.length; ++i) {
        if (radii[i] > maxRadius) {
            maxRadius = radii[i];
            maxIndex = i;
        }
    }

    const beg = Math.floor((maxIndex - maxRadius) / 2);
    const end = Math.floor((maxIndex + maxRadius) / 2);
    return s.slice(beg, end);
};
