// Accepted: 3ms (63.16%), 8.80MB (21.05%)

class Solution {
    bool visited[int(2e4+1)]; // visited x
public:
    int minimumOperationsToMakeEqual(int x, int y) {
        // BFS to find minimum distance
        queue<pair<int, int>> queue; // (x, distance)
        visited[x] = true;
        queue.push({x, 0});

        while (queue.size() > 0) {
            auto [x, n] = queue.front();
            queue.pop();

            if (x == y) {
                return n;
            }

            if (!visited[x+1]) {
                visited[x+1] = true;
                queue.push({x+1, n+1});
            }
            if (x > 1 && !visited[x-1]) {
                visited[x-1] = true;
                queue.push({x-1, n+1});
            }
            if (x % 5 == 0 && !visited[x/5]) {
                visited[x/5] = true;
                queue.push({x/5, n+1});
            }
            if (x % 11 == 0 && !visited[x/11]) {
                visited[x/11] = true;
                queue.push({x/11, n+1});
            }
        }

        return -1;
    }
};
