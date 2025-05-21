/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function (isConnected) {
    let visited = []
    let count = 0
    for (let x = 0; x < isConnected.length; x++) {
        let toVisit = [x]
        if (!visited.includes(x)) {
            while (toVisit.length != 0) {
                let curRoom = toVisit.shift()
                for (let y = 0; y < isConnected.length; y++) {
                    if (isConnected[x][y] == 1  && !visited.includes(x)) {
                        toVisit.push(y)
                    }
                }
                if (!visited.includes(curRoom)) {
                    visited.push(curRoom)
                }
            }
            count++;
        }
    }
    return count;
};
