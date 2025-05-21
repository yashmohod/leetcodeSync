/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var minReorder = function (n, connections) {



    let visited = []
    let queue = [0]
    let count = 0
    while (queue.length != 0) {
        let cur = queue.shift()
        for (let x = 0; x < n - 1; x++) {
            if (connections[x].includes(cur)) {
                if (connections[x][0] == cur) {
                    if (!queue.includes(connections[x][1])
                        && !visited.includes(connections[x][1])) {
                        queue.push(connections[x][1])
                        visited.push(connections[x][1])
                        count++;
                    }
                } else {
                    if (!queue.includes(connections[x][0])
                        && !visited.includes(connections[x][0])) {
                        queue.push(connections[x][0])
                        visited.push(connections[x][0])
                    }
                }
            }
        }
        visited.push(cur)
    }
    return count;
};
