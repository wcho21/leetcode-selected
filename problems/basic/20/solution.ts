// Accepted: 60ms (60.80%), 44.60 (49.60%)

function isValid(s: string): boolean {
    const stack: string[] = [];

    for (const c of s) {
        if ("({[".includes(c)) {
            stack.push(c);
            continue;
        }

        // return false if unmatched closing parenthesis
        if (stack.length === 0) {
            return false;
        }

        const pop = stack.pop();

        if (c === ")" && pop !== "(") {
            return false;
        }
        if (c === "}" && pop !== "{") {
            return false;
        }
        if (c === "]" && pop !== "[") {
            return false;
        }
    }

    // return false if any unmatched opening parenthesis
    if (stack.length !== 0) {
        return false;
    }

    return true;
};
