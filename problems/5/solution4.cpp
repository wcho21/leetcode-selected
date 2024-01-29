// Accepted: 7ms (94.02%), 7.35MB (70.13%)

// Manacher's algorithm

constexpr int MAX_S_LEN = 1001;

        }

        int center = 0;
        int rbound = 0;

        for (int i = 0; i < n; ++i) {
            if (0 < i && i < rbound) {
                int mirrored = 2*center - i;
                radii[i] = min(radii[mirrored], rbound-i);
            }

            int left = i - radii[i];
            int right = i + radii[i];
            while (left > 0 && right < n-1 && str[left-1] == str[right+1]) {
                left--;
                right++;
                radii[i]++;
            }

            if (right > rbound) {
                rbound = right;
                center = i;
            }
        }

        int maxRadius = -1;
        int maxIndex = -1;
        for (int i = 0; i < n; ++i) {
            if (radii[i] > maxRadius) {
                maxRadius = radii[i];
                maxIndex = i;
            }
        }

        int beg = (maxIndex - maxRadius) / 2;
        int end = (maxIndex + maxRadius) / 2;
        int len = end - beg;
        return s.substr(beg, len);
    }
};
