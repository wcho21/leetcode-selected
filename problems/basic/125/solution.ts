// Accepted: 75ms (33.59%), 54.59MB (5.18%)

function isPalindrome(s: string): boolean {
    const filtered = Array.from(s.toLowerCase()).filter(ch => /^[a-zA-Z0-9]$/.test(ch));
    const reversed = filtered.slice().reverse();

    return filtered.join("") === reversed.join("");
};
