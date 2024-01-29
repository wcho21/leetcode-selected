// Accepted: 62ms (40.00%) 45.29MB (20.00%)

function validUtf8(data: number[]): boolean {
    // continue if valid; otherwise early return false
    let i = 0;
    while (i < data.length) {
        // continue if valid one-byte prefix
        if (((data[i] >>> 7) & 0b1) === 0) {
            i += 1;
            continue;
        }

        // return false if invalid second byte
        if (i+1 >= data.length || ((data[i+1] >>> 6) & 0b11) !== 0b10) {
            return false;
        }

        // continue if valid two-byte prefix
        if (((data[i] >>> 5) & 0b111) === 0b110) {
            i += 2;
            continue;
        }

        // return false if invalid third byte
        if (i+2 >= data.length || ((data[i+2] >>> 6) & 0b11) !== 0b10) {
            return false;
        }

        // continue if valid three-byte prefix
        if (((data[i] >>> 4) & 0b1111) === 0b1110) {
            i += 3;
            continue;
        }

        // return false if invalid fourth byte
        if (i+3 >= data.length || ((data[i+3] >>> 6) & 0b11) !== 0b10) {
            return false;
        }

        // continue if valid four-byte prefix
        if (((data[i] >>> 3) & 0b11111) === 0b11110) {
            i += 4;
            continue;
        }

        return false;
    }

    return true;
};
